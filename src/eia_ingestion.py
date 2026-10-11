import requests
from dotenv import load_dotenv
import os 
from pathlib import Path
from google.cloud import bigquery
from datetime import date, timedelta



env_path= Path(__file__).resolve().parent.parent/".env"
load_dotenv(env_path)

API_KEY = os.getenv("EIA_API_KEY")


url = 'https://api.eia.gov/v2/electricity/rto/daily-fuel-type-data/data/'

params = {
    "api_key" : API_KEY,
    "frequency": "daily",
    "data[0]": "value",
    "sort[0][column]": "period",
    "sort[0][direction]": "desc",
    "offset":0,
    "length": 1
} # para conseguir el ultimo dia con datos

response = requests.get(url, params=params) ## (Haz una petición GET a esta url, utilizando estos params.)  

print(response.status_code)
latest_period= response.json()["response"]["data"][0]["period"] 
print(f"Latest available date: {latest_period}") # ultimo dia con datos en EIA API


# Define the recovery window
latest_date = date.fromisoformat(latest_period)
start_date = latest_date - timedelta(days=6) # ventana de 7 dias previos

print(f"Retrieving data from {start_date} to {latest_date}")


# Connect to BigQuery
client = bigquery.Client(project="energy-data-platform-504806")

table_id = "energy-data-platform-504806.raw.eia_daily_fuel_type_raw"


# Process each day separately within the recovery window (importante, 5000 registros por llamada max)
current_date = start_date

while current_date <= latest_date:

    current_period = str(current_date)

    print(f"\nProcessing {current_period}")


    # ---------------------------------------------------------------
    # Request data from EIA for this specific day
    # ---------------------------------------------------------------

    # Define the API parameters for one day
    params = {
        "api_key": API_KEY,
        "frequency": "daily",
        "data[0]": "value",
        "start": current_period,
        "end": current_period,
        "offset": 0,
        "length": 5000
    }

    # Request the data from EIA
    response = requests.get(url, params=params)

    print(f"EIA status code: {response.status_code}")

    data = response.json()["response"]["data"]

    # Count the records returned by EIA for this day
    eia_rows = len(data)

    print(f"EIA records: {eia_rows}")

    # -------------------------------------------------------------------
    # Check which records already exist in the RAW table
    # -------------------------------------------------------------------

    # Define the SQL query to get the existing record keys for this date
    query = f"""
    SELECT
        respondent,
        fueltype,
        timezone
    FROM `{table_id}`
    WHERE period = '{current_period}'
    """

    # Run the SQL query in BigQuery
    result = client.query(query).result()

    # Store the existing record keys
    existing_keys = {
        (row.respondent, row.fueltype, row.timezone)
        for row in result
    }

    # Display how many records already exist for this date
    print(f"RAW records: {len(existing_keys)}")


    # -------------------------------------------------------------------
    # Transform EIA records into the RAW table structure
    # -------------------------------------------------------------------

    records = []

    for row in data:

        record = {
            "period": row["period"],
            "respondent": row["respondent"],
            "respondent_name": row["respondent-name"],
            "fueltype": row["fueltype"],
            "type_name": row["type-name"],
            "timezone": row["timezone"],
            "timezone_description": row["timezone-description"],
            "value": float(row["value"]),
            "value_units": row["value-units"],
        }

        records.append(record)


    # -------------------------------------------------------------------
    # Identify records that are not yet in the RAW table
    # -------------------------------------------------------------------

    # Keep only records whose key does not already exist in RAW
    records_to_load = [
        record
        for record in records
        if (
            record["respondent"],
            record["fueltype"],
            record["timezone"]
        ) not in existing_keys
    ]

    # Display how many new records were found
    print(f"New records to load: {len(records_to_load)}")


    # -------------------------------------------------------------------
    # Load only the new records
    # -------------------------------------------------------------------

    if records_to_load:

        # Define how BigQuery should load the records
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_APPEND"
        )

        # Load the new records into the RAW table
        job = client.load_table_from_json(
            records_to_load,
            table_id,
            job_config=job_config
        )

        # Wait for the load to finish
        job.result()

        print(f"Loaded {len(records_to_load)} new records for {current_period}")

    else:

        # Skip the load because all records already exist in RAW
        print(f"Skipped {current_period}: all records already exist")


    # Move to the next day
    current_date += timedelta(days=1)