# Cloud Resource Usage & Cost Analysis

## 📌 Project Overview

This project analyzes cloud resource usage and associated costs across different departments, cloud services, resource types, and regions.

The main goal of this project is to understand cloud spending patterns, identify high-cost areas, analyze resource utilization, and identify potential opportunities for cloud cost optimization.

The project uses Python for data exploration and analysis, PostgreSQL and SQL for structured data analysis, and Power BI for interactive data visualization.

---

## 🎯 Project Objectives

* Analyze overall cloud resource expenditure
* Identify departments with the highest cloud costs
* Compare costs across different cloud services
* Analyze regional and resource-type spending
* Understand CPU and memory utilization
* Identify potentially underutilized resources
* Analyze monthly and yearly cloud cost trends
* Create an interactive Power BI dashboard
* Provide recommendations for cloud cost optimization

---

## 📂 Dataset

The dataset contains 12,000 cloud resource records and 11 attributes.

### Dataset Columns

| Column               | Description                           |
| -------------------- | ------------------------------------- |
| Date                 | Date of resource usage                |
| Department           | Department using the cloud resource   |
| Resource_ID          | Unique identifier of the resource     |
| Cloud_Service        | Type of cloud service                 |
| Resource_Type        | Type of cloud resource                |
| Region               | Geographic cloud region               |
| CPU_Usage_Percent    | CPU utilization percentage            |
| Memory_Usage_Percent | Memory utilization percentage         |
| Storage_Usage_GB     | Storage used in GB                    |
| Usage_Hours          | Number of hours the resource was used |
| Cost_USD             | Cost associated with the resource     |

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* Matplotlib
* PostgreSQL
* SQL
* Power BI
* Microsoft Excel
* Visual Studio Code

---

## 🔄 Project Workflow

```text
Raw Dataset
     ↓
Data Exploration using Python
     ↓
Data Analysis using Python
     ↓
Data Storage in PostgreSQL
     ↓
SQL Analysis
     ↓
Power BI Visualization
     ↓
Insights & Recommendations
```

---

## 🐍 Python Analysis

Python was used for data loading, exploration, statistical analysis, and visualization.

### Libraries Used

```python
import pandas as pd
import matplotlib.pyplot as plt
```

### Data Exploration

Pandas was used to understand the structure and characteristics of the dataset.

The following functions were used:

* `head()` - to view the first few records
* `shape` - to identify the number of rows and columns
* `columns` - to inspect column names
* `info()` - to understand data types and missing values
* `describe()` - to obtain statistical summaries

The dataset contains:

* 12,000 records
* 11 columns
* No missing values in the analyzed columns

### Python Analysis Performed

Python was used to calculate and analyze:

* Department-wise cloud cost
* Cloud service-wise cloud cost
* Basic statistical measures
* Resource usage patterns

Matplotlib was used to create visualizations for understanding cloud cost patterns.

---

## 🐘 PostgreSQL & SQL Analysis

PostgreSQL was used to store the cloud resource dataset and perform structured SQL analysis.

A database named `cloud_cost_analysis` was used for the project.

A table named `cloud_resources` was created to store the dataset.

The dataset was imported into PostgreSQL and contains 12,000 records.

### SQL Analysis Performed

SQL queries were used to perform the following analysis:

* Total cloud expenditure
* Department-wise cost
* Cloud service-wise cost
* Region-wise cost
* Resource type-wise cost
* Department and cloud service cost comparison
* Top 10 most expensive resources
* Underutilized resources
* Underutilized resource count and associated cost
* Department-wise CPU and memory utilization
* Monthly cloud cost
* Overall project KPIs

---

## 📊 Power BI Dashboard

Power BI was used to create an interactive dashboard for visualizing cloud resource usage and cost information.

![Power BI Dashboard](screenshots/dashboard.png)

### Dashboard Includes

* Total Cloud Cost
* Total Resources
* Average Cost
* Department-wise Cost
* Region-wise Cost
* Cloud Service-wise Cost
* Monthly Cloud Cost
* Year-wise Cloud Cost
* Department Filter
* Resource-level Details

The dashboard allows users to interact with the data using filters and compare cloud spending across different departments, services, and regions.

---

## 💡 Key Insights

### 1. Department-wise Spending

The IT department has the highest cloud expenditure with approximately:

**$201,801.80**

Finance and Operations are the next highest-spending departments.

### 2. Cloud Service Spending

Database services have the highest total cost:

**$307,462.61**

Compute is the second-highest cost category with:

**$244,568.62**

This indicates that Database and Compute services are major contributors to overall cloud expenditure.

### 3. Resource Utilization

Resource utilization was analyzed using CPU usage, memory usage, storage usage, and usage hours.

Resources with relatively low CPU and memory utilization can be reviewed for possible optimization.

### 4. Cost Trends

Monthly and yearly cost analysis was performed to understand how cloud expenditure changes over time.

This analysis can help identify changes in spending patterns and monitor unexpected increases in cloud costs.

---

## 💡 Recommendations

Based on the analysis, the following recommendations can be considered:

* Review high-cost resources in the IT department to understand the reasons behind their higher expenditure.
* Focus cost optimization efforts on Database and Compute services because they contribute significantly to overall spending.
* Regularly monitor CPU and memory utilization to identify underutilized resources.
* Consider resizing, scheduling, consolidating, or removing resources with consistently low utilization.
* Monitor monthly cloud expenditure through the Power BI dashboard.

---

## 🏆 Project Outcome

This project provides a data-driven view of cloud resource consumption and associated costs.

By combining Python, SQL, PostgreSQL, and Power BI, the project demonstrates an end-to-end data analytics workflow:

**Data → Exploration → Analysis → SQL → Visualization → Insights → Recommendations**

The project helps identify major cloud spending areas and potential opportunities for improving resource utilization and controlling cloud costs.

---

## 🧠 Skills Demonstrated

* Data Analysis
* Exploratory Data Analysis (EDA)
* Python
* Pandas
* Matplotlib
* SQL
* PostgreSQL
* Power BI
* Data Visualization
* Dashboard Development
* Business Insights
* Cloud Cost Analysis
* Cost Optimization Analysis
