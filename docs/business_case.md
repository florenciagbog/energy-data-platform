# Business Case	
	
## Background	
	
The Analytics department currently relies on manually downloading external energy market data whenever it is required for reporting and trend analysis. This process is time-consuming, inconsistent across teams, and does not maintain historical records, making it difficult to perform reliable long-term analysis.	
To improve data availability and eliminate manual effort, the company has decided to integrate energy market data from the U.S. Energy Information Administration (EIA) into its analytics platform.	
The solution must be scalable, automated, maintainable, and require no manual intervention after deployment. Business users should be able to consume the curated data through both a web application and reporting dashboards.	
	
## Implementation Plan	
	
Phase	Objective
1. Business Requirements	Understand the business problem, define project scope, and identify reporting requirements.
2. Source System Analysis	Explore the EIA API, understand the available datasets, evaluate the schema, and define the extraction strategy.
3. Data Model Design	Design the analytical data model, including RAW, staging, dimensions, facts, and marts.
4. Cloud Infrastructure Setup	Configure the Google Cloud environment, including BigQuery, Cloud Run, Cloud Scheduler, IAM, and supporting services.
5. Data Ingestion Pipeline	Develop the Python pipeline to extract data from the EIA API and load it into the RAW layer in BigQuery.
6. Pipeline Automation	Schedule and automate the daily execution of the ingestion pipeline using Google Cloud services.
7. Data Transformation	Build the transformation layer with dbt, including testing, documentation, and analytical models.
8. Data Validation & Monitoring	Implement data quality checks, logging, error handling, and pipeline monitoring.
9. Data Consumption Layer	Develop the Streamlit application and Power BI dashboard connected to the curated analytical model.
10. Production Readiness	Finalize documentation, deployment process, repository structure, and prepare the solution for production.