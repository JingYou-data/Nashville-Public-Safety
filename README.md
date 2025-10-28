![Nashville Public Safety](https://capsule-render.vercel.app/api?type=waving&color=0:4A90E2,100:50E3C2&height=160&section=header&text=From%20Calls%20to%20Crimes:%20Nashville%20Public%20Safety%20Analysis&fontColor=ffffff&fontSize=25)

# 🚔 From Calls to Crimes: Analyzing Public Safety Trends in Nashville

**Capstone Project | Nashville Software School (NSS)**  
Analyzing 911 call patterns and police-reported crime incidents in Nashville from 2018 to 2024 to uncover public safety insights and trends.

---

## 📖 Executive Summary
This project explores relationships between **emergency service calls** and **crime reports** across Nashville.  
By combining data from multiple city departments, it identifies **geographic hotspots**, **temporal trends**, and **service response inefficiencies** to support policy and operational improvements.

---

## 🧭 Motivation
- Understand how public complaints (service calls) correlate with police crime data  
- Detect spatial and temporal patterns of recurring safety incidents  
- Support evidence-based decision-making for Nashville’s community programs  

---

## 📊 Datasets
| Dataset | Description | Source |
|----------|--------------|--------|
| Metro Police Department Incidents (2018–2021) | Crime data by type, time, and ZIP code | Metro Nashville Open Data Portal |
| 911 Calls for Service (2018–2021) | Citizen-reported safety and service issues | HubNashville |
| Fines and Violations | Public sanitation fines and collection outcomes | HubNashville |
| Geospatial Boundaries | ZIP code and district shapefiles | MNPD Open Data |

---

## ⚙️ Technologies Used
**Languages:** Python, SQL  
**Libraries:** Pandas, Folium, Matplotlib, GeoPandas  
**Tools:** Power BI, PostgreSQL, Docker, Jupyter Notebook  

---

## 🔍 Key Questions
1. What are the most common types of calls and crime incidents in Nashville?  
2. Which ZIP codes and neighborhoods experience the highest public safety issues?  
3. How do missed pickups, fines, and response times vary between metro and contractors?  
4. Are there specific time patterns (weekdays, seasons) linked to recurring incidents?  

---

## 🗺️ Visualizations
- 🧭 **Folium Heatmap**: Hotspots of crime and 911 calls across ZIP codes  
- 📈 **Power BI Dashboard**: Interactive view of trends, routes, and fines  
- 🕒 **Time-Series Charts**: Monthly and daily trends of incidents  
- 🧮 **ZIP Comparison Matrix**: Contractor vs Metro performance metrics  

---

## 💡 Insights
- ZIP **37207** shows consistent concentration of reported incidents and missed pickups  
- **Contractor routes** had 20–30% longer average response times  
- Majority of complaints occurred **midday (10AM–3PM)** on weekdays  
- Fines increased sharply during post-holiday months, indicating seasonal volume impact  

---

## 🧠 Challenges
- Cleaning multi-source data with inconsistent geospatial boundaries  
- Resolving duplicate IDs and timestamp inconsistencies  
- Integrating shapefiles with CSVs for Folium visualization  

---

## 🚀 Future Work
- Automate data ingestion with **Docker + AWS**  
- Develop real-time dashboard for 911 service monitoring  
- Expand coverage to include population-adjusted safety indicators  

---

## 📈 Repository Structure
