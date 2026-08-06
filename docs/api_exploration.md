# API Exploration

## Overview

The objective of this phase was to evaluate the EIA (U.S. Energy Information Administration) API, understand its capabilities, and determine the most appropriate dataset for the business requirements defined in this project.

---

## API Exploration Notes

| Question | Answer |
|----------|--------|
| **Which datasets are available?** | The EIA API provides several energy domains, including Electricity, Natural Gas, Petroleum, Coal, Densified Biomass, Nuclear Plant Generator Outages, Energy Outlook & Projections, Total Energy, State Energy Data System (SEDS), CO₂ Emissions, and International Energy. |
| **Which dataset best fits this project?** | **Selected dataset:** Electricity → Balancing Authority Areas Hourly Operating Data → **Daily Generation by Energy Source**. This dataset provides daily electricity generation broken down by balancing authority and fuel type, making it suitable for historical trend analysis and dimensional modeling. |
| **How do you query a dataset?** | The EIA API follows a hierarchical route structure. Requests are built by navigating the API route and ending with the `/data` endpoint. Query parameters such as `api_key`, `frequency`, `data[]`, `facets`, `start`, `end`, `sort`, `offset`, and `length` are passed as URL parameters. |
| **How is the data retrieved?** | Responses are returned in **JSON** format by default. XML output is also supported by specifying the `out=xml` parameter. |
| **How does pagination work?** | The API returns a maximum of **5,000 rows** per JSON request (300 rows for XML). Pagination is handled using the `offset` and `length` parameters. The response also includes the total number of matching records (`response.total`). |
| **Are there any rate limits?** | The API applies rate limiting to prevent excessive traffic. If too many requests are submitted within a short period, the API key is temporarily suspended and automatically reactivated after a cooldown period. The EIA documentation does not specify fixed numeric limits. |
| **How frequently is the data refreshed?** | The refresh frequency depends on the selected dataset. **Daily Generation by Energy Source** is updated daily, making it suitable for an automated daily ingestion pipeline. |

---

# Selected Dataset

**Domain**

- Electricity

**Category**

- Balancing Authority Areas Hourly Operating Data

**Dataset**

- Daily Generation by Energy Source

---

# Business Grain

One record represents the amount of electricity generated for a given **day**, **balancing authority**, **fuel type**, and **time zone**.

---

# Business Entities

| Entity | Description |
|---------|-------------|
| Date | Reporting date. |
| Balancing Authority | Organization responsible for balancing electricity supply and demand within its service area. |
| Fuel Type | Energy source used to generate electricity (Coal, Natural Gas, Nuclear, Solar, Wind, etc.). |
| Time Zone | Time zone associated with the balancing authority. |
| Generation | Amount of electricity generated during the reporting period. |

---

# Measures

- Electricity Generation

---

# Dimensions

- Date
- Balancing Authority
- Fuel Type
- Time Zone

---

# Unit of Measure

- Megawatt-hours (MWh)

---

# Design Decision

This dataset was selected because it supports the project's business objective of building a cloud-native data platform capable of automatically ingesting daily operational electricity data for historical analysis and reporting.

Its daily refresh frequency, dimensional structure, and operational focus make it well suited for implementing an end-to-end Data Engineering solution using Google Cloud Platform.