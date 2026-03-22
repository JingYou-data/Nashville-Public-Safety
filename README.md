![Nashville Public Safety](https://capsule-render.vercel.app/api?type=waving&color=0:4A90E2,100:50E3C2&height=160&section=header&text=From%20Calls%20to%20Crimes:%20Nashville%20Public%20Safety%20Analysis&fontColor=ffffff&fontSize=25)

# 🚔 From Calls to Crimes: Analyzing Public Safety Trends in Nashville

<p align="center">
  <img src="https://img.shields.io/badge/Python-Pandas%20%7C%20Folium%20%7C%20GeoPandas-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black">
  <img src="https://img.shields.io/badge/Records-1M%2B-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Period-2018–2021-orange?style=for-the-badge">
</p>

> **Geospatial and time-series analysis of 911 calls and police-reported crime data across Nashville — identifying hotspots, shift patterns, and ZIP-level growth trends to support smarter public safety planning.**

---

## 📌 Project Overview

| | |
|---|---|
| **Data Sources** | Metro Nashville Police Department + HubNashville Open Data |
| **Period** | 2018 – 2021 |
| **Records** | 1M+ rows across 4 datasets |
| **Analysis Types** | Geospatial mapping, time-series, crime confirmation, ZIP growth trends |
| **Tools** | Python, Pandas, Folium, GeoPandas, Power BI, PostgreSQL, Docker |

---

## 📊 Datasets

| Dataset | Description | Source |
|---|---|---|
| MNPD Crime Incidents (2018–2021) | Crime type, time, and ZIP code | Metro Nashville Open Data |
| 911 Calls for Service (2018–2021) | Citizen-reported safety and service calls | HubNashville |
| Fines and Violations | Public sanitation fines and collection outcomes | HubNashville |
| Geospatial Boundaries | ZIP code and precinct shapefiles | MNPD Open Data |

---

## 🔍 Key Questions

| Question | Insight Delivered |
|---|---|
| What are the most frequent incident types by ZIP code? | Resource allocation by neighborhood |
| How do 911 calls correlate with confirmed crimes? | Identify high-confirmation call types |
| What times of day show the highest activity? | Optimize shift scheduling |
| Which ZIP codes show the most growth? | Anticipate suburban safety demand |
| How have call volumes shifted over 4 years? | Longitudinal trend analysis |

---

## 💡 Key Insights

### 🗺️ Nashville ZIP Code Map

<img src="https://raw.githubusercontent.com/JingYou-data/Nashville-Public-Safety/main/visuals/nashville_zip_map.png" width="700">

Geographic context for public safety analysis — spatial patterns across Nashville neighborhoods.

---

### 🚨 Crime Confirmation Patterns

<img src="https://raw.githubusercontent.com/JingYou-data/Nashville-Public-Safety/main/visuals/call_types_confirmation.png" width="700">

**Theft** has the highest confirmation rate at **55.3%**, followed by **Missing Person (23.1%)** and **Escaped Prisoner (21.4%)** — representing the most resource-intensive response categories.

---

### 📈 ZIP Code Growth Trends (2019 vs 2018)

<img src="https://raw.githubusercontent.com/JingYou-data/Nashville-Public-Safety/main/visuals/zip_growth_trend.png" width="700">

| Period | Finding | Key ZIPs |
|---|---|---|
| 2019 vs 2018 | **37135 (Nolensville)** highest growth rate (+2.0) — strong suburban development | 37135, 37203, 37209 |
| 2020 vs 2019 | **37086** and **37143** showed 100%+ increase — population shifts and local events | 37086, 37143, 37232 |
| 2021 vs 2020 | Continued high growth in fast-developing suburban and business zones | 37208, 37210, 37207 |

---

### 🔹 Call Trends by Shift (2018–2021)

| Shift | Hours | Pattern |
|---|---|---|
| Shift A | 6 AM – 2 PM | Highest volume, especially Spring — most staffing demand |
| Shift B | 2 PM – 10 PM | Steady decline after 2019 |
| Shift C | 10 PM – 6 AM | Lowest volume, mirrors general trends |

---

### 🔥 Geospatial Hotspots

<img src="visuals/heatmap_nashville.png" width="700">

Downtown, East Nashville, and South Nashville show the highest incident density. Business corridors drive strong demand for patrol and security response.

---

## 💬 Recommendations

| Finding | Recommended Action |
|---|---|
| Morning shifts peak in volume | Increase staffing 6 AM–2 PM, especially Spring |
| High-growth suburban ZIPs | Prioritize 37135 and 37208 for expanded coverage |
| High-confirmation crime types | Reallocate resources toward Theft and Missing Person calls |
| Low-confirmation call types | Review and refine to reduce unnecessary response burden |

---

## 📁 Repository Structure

```
Nashville-Public-Safety/
├── data/
│   ├── raw/                    # Original datasets
│   └── cleaned/                # Processed data files
├── notebooks/
│   └── analysis.ipynb          # Main analysis notebook
├── visuals/
│   ├── nashville_zip_map.png
│   ├── call_types_confirmation.png
│   ├── zip_growth_trend.png
│   └── heatmap_nashville.png
├── dashboard/                  # Power BI report file
└── README.md
```

---

## 🚀 Future Work

- [ ] Expand to **2022–2024** data for post-COVID trend analysis
- [ ] Build **interactive Streamlit dashboard** for real-time ZIP filtering
- [ ] Add **predictive model** for call volume forecasting by shift and season
- [ ] Integrate **Census demographic data** for socioeconomic context

---

## 👤 Author

**Jing You** — Data Analytics & Engineering
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jing--you84-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jing-you84/)
[![GitHub](https://img.shields.io/badge/GitHub-JingYou--data-181717?style=flat&logo=github&logoColor=white)](https://github.com/JingYou-data)
[![Portfolio](https://img.shields.io/badge/Portfolio-jingyou--data.github.io-blue?style=flat)](https://jingyou-data.github.io)

---

*Capstone Project · Nashville Software School · Data: Metro Nashville Open Data Portal 2018–2021*
