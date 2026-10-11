-- This SQL script is executed in Google BigQuery.
-- It creates the RAW table for daily EIA fuel type data.
CREATE TABLE `energy-data-platform-504806.raw.eia_daily_fuel_type_raw` (
    period DATE,
    respondent STRING,
    respondent_name STRING,
    fueltype STRING,
    type_name STRING,
    timezone STRING,
    timezone_description STRING,
    value NUMERIC,
    value_units STRING
)
PARTITION BY period;