CREATE TABLE cloud_resources (
    date DATE,
    department VARCHAR(50),
    resource_id VARCHAR(50),
    cloud_service VARCHAR(50),
    resource_type VARCHAR(50),
    region VARCHAR(50),
    cpu_usage_percent DECIMAL(5,2),
    memory_usage_percent DECIMAL(5,2),
    storage_usage_gb DECIMAL(10,2),
    usage_hours DECIMAL(10,2),
    cost_usd DECIMAL(10,2)
);
SELECT COUNT(*)
FROM cloud_resources;

COPY cloud_resources
FROM 'E:/Cloud-Resource-Cost-Analysis/cloud_resource_usage_cost_analysis.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);

SELECT *
FROM cloud_resources
LIMIT 5;

-- 1. TOTAL CLOUD COST
SELECT
    ROUND(SUM(cost_usd), 2) AS total_cloud_cost
FROM cloud_resources;


-- 2. DEPARTMENT-WISE COST
SELECT
    department,
    ROUND(SUM(cost_usd), 2) AS total_cost
FROM cloud_resources
GROUP BY department
ORDER BY total_cost DESC;


-- 3. CLOUD SERVICE-WISE COST
SELECT
    cloud_service,
    ROUND(SUM(cost_usd), 2) AS total_cost
FROM cloud_resources
GROUP BY cloud_service
ORDER BY total_cost DESC;


-- 4. REGION-WISE COST
SELECT
    region,
    ROUND(SUM(cost_usd), 2) AS total_cost
FROM cloud_resources
GROUP BY region
ORDER BY total_cost DESC;


-- 5. RESOURCE TYPE-WISE COST
SELECT
    resource_type,
    ROUND(SUM(cost_usd), 2) AS total_cost
FROM cloud_resources
GROUP BY resource_type
ORDER BY total_cost DESC;


-- 6. DEPARTMENT + SERVICE COST
SELECT
    department,
    cloud_service,
    ROUND(SUM(cost_usd), 2) AS total_cost
FROM cloud_resources
GROUP BY department, cloud_service
ORDER BY total_cost DESC;


-- 7. TOP 10 EXPENSIVE RESOURCES
SELECT
    resource_id,
    department,
    cloud_service,
    resource_type,
    region,
    cost_usd
FROM cloud_resources
ORDER BY cost_usd DESC
LIMIT 10;


-- 8. UNDERUTILIZED RESOURCES
SELECT
    resource_id,
    department,
    cloud_service,
    cpu_usage_percent,
    memory_usage_percent,
    cost_usd
FROM cloud_resources
WHERE cpu_usage_percent < 20
  AND memory_usage_percent < 40
ORDER BY cost_usd DESC;


-- 9. UNDERUTILIZED RESOURCE COUNT + COST
SELECT
    COUNT(*) AS underutilized_resources,
    ROUND(SUM(cost_usd), 2) AS underutilized_cost
FROM cloud_resources
WHERE cpu_usage_percent < 20
  AND memory_usage_percent < 40;


-- 10. DEPARTMENT-WISE UTILIZATION
SELECT
    department,
    ROUND(AVG(cpu_usage_percent), 2) AS avg_cpu_usage,
    ROUND(AVG(memory_usage_percent), 2) AS avg_memory_usage,
    ROUND(AVG(usage_hours), 2) AS avg_usage_hours
FROM cloud_resources
GROUP BY department
ORDER BY avg_cpu_usage DESC;


-- 11. MONTHLY CLOUD COST
SELECT
    DATE_TRUNC('month', date)::DATE AS month,
    ROUND(SUM(cost_usd), 2) AS total_cost
FROM cloud_resources
GROUP BY month
ORDER BY month;


-- 12. OVERALL PROJECT KPIs
SELECT
    COUNT(*) AS total_resources,
    ROUND(SUM(cost_usd), 2) AS total_cloud_cost,
    ROUND(AVG(cost_usd), 2) AS average_cost,
    ROUND(MAX(cost_usd), 2) AS highest_cost,
    ROUND(AVG(cpu_usage_percent), 2) AS average_cpu_usage,
    ROUND(AVG(memory_usage_percent), 2) AS average_memory_usage,
    ROUND(SUM(usage_hours), 2) AS total_usage_hours
FROM cloud_resources;
