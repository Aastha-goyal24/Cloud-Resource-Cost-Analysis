import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_excel("cloud_resource_usage_cost_analysis.xlsx")

print("\n========== DATASET LOADED ==========")
print("Rows and Columns:", df.shape)


# ============================================================
# 2. BASIC DATA EXPLORATION
# ============================================================

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DATA INFORMATION ==========")
df.info()

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())


# ============================================================
# 3. CHECK MISSING VALUES
# ============================================================

print("\n========== MISSING VALUES ==========")
missing_values = df.isnull().sum()
print(missing_values)


# ============================================================
# 4. CHECK DUPLICATE ROWS
# ============================================================

print("\n========== DUPLICATE ROWS ==========")
duplicates = df.duplicated().sum()
print("Number of duplicate rows:", duplicates)


# ============================================================
# 5. DEPARTMENT-WISE TOTAL COST
# ============================================================

department_cost = (
    df.groupby("Department")["Cost_USD"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== COST BY DEPARTMENT ==========")
print(department_cost)


# ============================================================
# 6. CLOUD SERVICE-WISE TOTAL COST
# ============================================================

service_cost = (
    df.groupby("Cloud_Service")["Cost_USD"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== COST BY CLOUD SERVICE ==========")
print(service_cost)


# ============================================================
# 7. DEPARTMENT + SERVICE COST ANALYSIS
# ============================================================

department_service_cost = (
    df.groupby(["Department", "Cloud_Service"])["Cost_USD"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== COST BY DEPARTMENT AND SERVICE ==========")
print(department_service_cost)


# ============================================================
# 8. REGION-WISE COST ANALYSIS
# ============================================================

region_cost = (
    df.groupby("Region")["Cost_USD"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== COST BY REGION ==========")
print(region_cost)


# ============================================================
# 9. RESOURCE TYPE-WISE COST
# ============================================================

resource_type_cost = (
    df.groupby("Resource_Type")["Cost_USD"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== COST BY RESOURCE TYPE ==========")
print(resource_type_cost)


# ============================================================
# 10. AVERAGE CPU USAGE BY DEPARTMENT
# ============================================================

avg_cpu_department = (
    df.groupby("Department")["CPU_Usage_Percent"]
    .mean()
    .sort_values(ascending=False)
)

print("\n========== AVERAGE CPU USAGE BY DEPARTMENT ==========")
print(avg_cpu_department)


# ============================================================
# 11. AVERAGE MEMORY USAGE BY DEPARTMENT
# ============================================================

avg_memory_department = (
    df.groupby("Department")["Memory_Usage_Percent"]
    .mean()
    .sort_values(ascending=False)
)

print("\n========== AVERAGE MEMORY USAGE BY DEPARTMENT ==========")
print(avg_memory_department)


# ============================================================
# 12. AVERAGE USAGE HOURS BY DEPARTMENT
# ============================================================

avg_hours_department = (
    df.groupby("Department")["Usage_Hours"]
    .mean()
    .sort_values(ascending=False)
)

print("\n========== AVERAGE USAGE HOURS BY DEPARTMENT ==========")
print(avg_hours_department)


# ============================================================
# 13. MONTHLY COST ANALYSIS
# ============================================================

df["Month"] = df["Date"].dt.to_period("M")

monthly_cost = (
    df.groupby("Month")["Cost_USD"]
    .sum()
)

print("\n========== MONTHLY CLOUD COST ==========")
print(monthly_cost)


# ============================================================
# 14. MONTHLY AVERAGE COST
# ============================================================

monthly_average_cost = (
    df.groupby("Month")["Cost_USD"]
    .mean()
)

print("\n========== MONTHLY AVERAGE COST ==========")
print(monthly_average_cost)


# ============================================================
# 15. HIGH-COST RESOURCES
# ============================================================

high_cost_threshold = df["Cost_USD"].quantile(0.90)

high_cost_resources = df[
    df["Cost_USD"] >= high_cost_threshold
].sort_values("Cost_USD", ascending=False)

print("\n========== HIGH-COST RESOURCES ==========")
print("High cost threshold:", round(high_cost_threshold, 2))
print(high_cost_resources[
    [
        "Resource_ID",
        "Department",
        "Cloud_Service",
        "Resource_Type",
        "CPU_Usage_Percent",
        "Memory_Usage_Percent",
        "Usage_Hours",
        "Cost_USD"
    ]
].head(20))


# ============================================================
# 16. UNDERUTILIZED RESOURCES
# ============================================================
# Low CPU + Low Memory but still generating cost

underutilized_resources = df[
    (df["CPU_Usage_Percent"] < 20) &
    (df["Memory_Usage_Percent"] < 40)
].copy()

underutilized_resources = underutilized_resources.sort_values(
    "Cost_USD",
    ascending=False
)

print("\n========== UNDERUTILIZED RESOURCES ==========")
print("Number of underutilized resources:",
      len(underutilized_resources))

print(
    underutilized_resources[
        [
            "Resource_ID",
            "Department",
            "Cloud_Service",
            "Resource_Type",
            "CPU_Usage_Percent",
            "Memory_Usage_Percent",
            "Usage_Hours",
            "Cost_USD"
        ]
    ].head(20)
)


# ============================================================
# 17. TOTAL COST OF UNDERUTILIZED RESOURCES
# ============================================================

underutilized_total_cost = underutilized_resources["Cost_USD"].sum()

print("\n========== UNDERUTILIZED RESOURCE COST ==========")
print(
    "Total cost of underutilized resources:",
    round(underutilized_total_cost, 2)
)


# ============================================================
# 18. COST VS CPU CORRELATION
# ============================================================

cpu_cost_correlation = df[
    ["CPU_Usage_Percent", "Cost_USD"]
].corr()

print("\n========== CPU VS COST CORRELATION ==========")
print(cpu_cost_correlation)


# ============================================================
# 19. COST VS USAGE HOURS CORRELATION
# ============================================================

hours_cost_correlation = df[
    ["Usage_Hours", "Cost_USD"]
].corr()

print("\n========== USAGE HOURS VS COST CORRELATION ==========")
print(hours_cost_correlation)


# ============================================================
# 20. OVERALL PROJECT KPIs
# ============================================================

total_cost = df["Cost_USD"].sum()
average_cost = df["Cost_USD"].mean()
highest_cost = df["Cost_USD"].max()
average_cpu = df["CPU_Usage_Percent"].mean()
average_memory = df["Memory_Usage_Percent"].mean()
total_usage_hours = df["Usage_Hours"].sum()

print("\n========== OVERALL PROJECT KPIs ==========")

print("Total Cloud Cost:", round(total_cost, 2))
print("Average Resource Cost:", round(average_cost, 2))
print("Highest Resource Cost:", round(highest_cost, 2))
print("Average CPU Usage:", round(average_cpu, 2), "%")
print("Average Memory Usage:", round(average_memory, 2), "%")
print("Total Usage Hours:", round(total_usage_hours, 2))


# ============================================================
# 21. VISUALIZATION - DEPARTMENT COST
# ============================================================

plt.figure(figsize=(8, 5))

department_cost.plot(kind="bar")

plt.title("Cloud Cost by Department")
plt.xlabel("Department")
plt.ylabel("Total Cost (USD)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ============================================================
# 22. VISUALIZATION - SERVICE COST
# ============================================================

plt.figure(figsize=(8, 5))

service_cost.plot(kind="bar")

plt.title("Cloud Cost by Cloud Service")
plt.xlabel("Cloud Service")
plt.ylabel("Total Cost (USD)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ============================================================
# 23. VISUALIZATION - REGION COST
# ============================================================

plt.figure(figsize=(8, 5))

region_cost.plot(kind="bar")

plt.title("Cloud Cost by Region")
plt.xlabel("Region")
plt.ylabel("Total Cost (USD)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ============================================================
# 24. VISUALIZATION - MONTHLY COST TREND
# ============================================================

plt.figure(figsize=(10, 5))

monthly_cost.plot(kind="line", marker="o")

plt.title("Monthly Cloud Cost Trend")
plt.xlabel("Month")
plt.ylabel("Total Cost (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# 25. VISUALIZATION - CPU VS COST
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["CPU_Usage_Percent"],
    df["Cost_USD"],
    alpha=0.4
)

plt.title("CPU Usage vs Cloud Cost")
plt.xlabel("CPU Usage (%)")
plt.ylabel("Cost (USD)")
plt.tight_layout()
plt.show()


# ============================================================
# 26. VISUALIZATION - USAGE HOURS VS COST
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Usage_Hours"],
    df["Cost_USD"],
    alpha=0.4
)

plt.title("Usage Hours vs Cloud Cost")
plt.xlabel("Usage Hours")
plt.ylabel("Cost (USD)")
plt.tight_layout()
plt.show()


# ============================================================
# 27. SAVE IMPORTANT ANALYSIS RESULTS
# ============================================================

with pd.ExcelWriter(
    "cloud_analysis_results.xlsx",
    engine="openpyxl"
) as writer:

    department_cost.to_frame(
        "Total_Cost"
    ).to_excel(
        writer,
        sheet_name="Department_Cost"
    )

    service_cost.to_frame(
        "Total_Cost"
    ).to_excel(
        writer,
        sheet_name="Service_Cost"
    )

    region_cost.to_frame(
        "Total_Cost"
    ).to_excel(
        writer,
        sheet_name="Region_Cost"
    )

    monthly_cost.to_frame(
        "Total_Cost"
    ).to_excel(
        writer,
        sheet_name="Monthly_Cost"
    )

    underutilized_resources.to_excel(
        writer,
        sheet_name="Underutilized"
    )


print("\n========== ANALYSIS COMPLETED ==========")
print("Results saved to cloud_analysis_results.xlsx")
