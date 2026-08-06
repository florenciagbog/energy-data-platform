## Business Requirements	
	
* BR-01	The system shall automatically retrieve energy market data every day. 
* BR-02	Historical data shall be preserved.
* BR-03	Business users shall be able to explore historical trends.
* BR-04	The solution shall not require manual execution.
* BR-05	Data shall be available before 7:00 AM.
* BR-06	Business users shall be able to access curated data through dashboards.
	
	
	
## Non Functional Requirements	
	
* NFR-01	Pipeline execution must complete in less than 10 minutes.
* NFR-02	System shall be available every day.
* NFR-03	Data shall be stored in Google Cloud.
* NFR-04	Pipeline shall be fully automated.
* NFR-05	Failures shall be logged.
	
	
## Scope	
	
### Included	
* Daily ingestion	
* BigQuery	
* dbt	
* Streamlit	
* Power BI	
	
	
### Excluded	
* Real-time streaming	
* Machine Learning	
* Alerts	
* User authentication	