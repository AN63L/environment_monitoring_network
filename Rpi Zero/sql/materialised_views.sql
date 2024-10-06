-- TEMPERATURE-- 
-- AVERAGE for today
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.temperature_daily_average
AS (
	SELECT AVG(temperature), created_at::date
	FROM metrics.sensor_1
	WHERE created_at >= CURRENT_DATE
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 7 days
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.temperature_weekly_average
AS (
	SELECT AVG(temperature), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '7' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 30 days (grouped by day)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.temperature_monthly_average
AS (
	SELECT AVG(temperature), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '30' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 365 days (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.temperature_yearly_average
AS (
	SELECT AVG(temperature), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '365' day
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
--  AVERAGE ALL TIME (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.temperature_all_time_average
AS (
	SELECT AVG(temperature), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;

------------------------------------------
-- HUMIDITY-- 
-- AVERAGE for today
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.humidity_daily_average
AS (
	SELECT AVG(humidity), created_at::date
	FROM metrics.sensor_1
	WHERE created_at >= CURRENT_DATE
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 7 days
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.humidity_weekly_average
AS (
	SELECT AVG(humidity), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '7' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 30 days (grouped by day)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.humidity_monthly_average
AS (
	SELECT AVG(humidity), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '30' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 365 days (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.humidity_yearly_average
AS (
	SELECT AVG(humidity), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '365' day
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
--  AVERAGE ALL TIME (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.humidity_all_time_average
AS (
	SELECT AVG(humidity), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;

------------------------------------------
-- Pressure-- 
-- AVERAGE for today
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pressure_daily_average
AS (
	SELECT AVG(pressure), created_at::date
	FROM metrics.sensor_1
	WHERE created_at >= CURRENT_DATE
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 7 days
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pressure_weekly_average
AS (
	SELECT AVG(pressure), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '7' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 30 days (grouped by day)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pressure_monthly_average
AS (
	SELECT AVG(pressure), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '30' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 365 days (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pressure_yearly_average
AS (
	SELECT AVG(pressure), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '365' day
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
--  AVERAGE ALL TIME (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pressure_all_time_average
AS (
	SELECT AVG(pressure), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;

------------------------------------------
-- Gas resistance-- 
-- AVERAGE for today
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.gas_resistance_daily_average
AS (
	SELECT AVG(gas_resistance), created_at::date
	FROM metrics.sensor_1
	WHERE created_at >= CURRENT_DATE
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 7 days
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.gas_resistance_weekly_average
AS (
	SELECT AVG(gas_resistance), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '7' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 30 days (grouped by day)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.gas_resistance_monthly_average
AS (
	SELECT AVG(gas_resistance), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '30' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 365 days (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.gas_resistance_yearly_average
AS (
	SELECT AVG(gas_resistance), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '365' day
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
--  AVERAGE ALL TIME (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.gas_resistance_all_time_average
AS (
	SELECT AVG(gas_resistance), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
------------------------------------------
-- PM 1.0-- 
-- AVERAGE for today
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_1_daily_average
AS (
	SELECT AVG(pm_1), created_at::date
	FROM metrics.sensor_1
	WHERE created_at >= CURRENT_DATE
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 7 days
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_1_weekly_average
AS (
	SELECT AVG(pm_1), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '7' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 30 days (grouped by day)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_1_monthly_average
AS (
	SELECT AVG(pm_1), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '30' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 365 days (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_1_yearly_average
AS (
	SELECT AVG(pm_1), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '365' day
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
--  AVERAGE ALL TIME (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_1_all_time_average
AS (
	SELECT AVG(pm_1), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
------------------------------------------
-- PM 10-- 
-- AVERAGE for today
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_10_daily_average
AS (
	SELECT AVG(pm_10), created_at::date
	FROM metrics.sensor_1
	WHERE created_at >= CURRENT_DATE
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 7 days
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_10_weekly_average
AS (
	SELECT AVG(pm_10), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '7' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 30 days (grouped by day)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_10_monthly_average
AS (
	SELECT AVG(pm_10), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '30' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 365 days (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_10_yearly_average
AS (
	SELECT AVG(pm_10), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '365' day
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
--  AVERAGE ALL TIME (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_10_all_time_average
AS (
	SELECT AVG(pm_10), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
------------------------------------------
-- PM 2.5-- 
-- AVERAGE for today
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_2_daily_average
AS (
	SELECT AVG(pm_2), created_at::date
	FROM metrics.sensor_1
	WHERE created_at >= CURRENT_DATE
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 7 days
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_2_weekly_average
AS (
	SELECT AVG(pm_2), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '7' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 30 days (grouped by day)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_2_monthly_average
AS (
	SELECT AVG(pm_2), created_at::date
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '30' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 365 days (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_2_yearly_average
AS (
	SELECT AVG(pm_2), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	WHERE created_at > CURRENT_DATE - interval '365' day
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
--  AVERAGE ALL TIME (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.pm_2_all_time_average
AS (
	SELECT AVG(pm_2), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_1
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
------------------------------------------
-- Rain percentage-- 
-- AVERAGE for today
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.rain_percentage_daily_average
AS (
	SELECT AVG(rain_percentage), created_at::date
	FROM metrics.sensor_2
	WHERE created_at >= CURRENT_DATE
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 7 days
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.rain_percentage_weekly_average
AS (
	SELECT AVG(rain_percentage), created_at::date
	FROM metrics.sensor_2
	WHERE created_at > CURRENT_DATE - interval '7' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 30 days (grouped by day)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.rain_percentage_monthly_average
AS (
	SELECT AVG(rain_percentage), created_at::date
	FROM metrics.sensor_2
	WHERE created_at > CURRENT_DATE - interval '30' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 365 days (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.rain_percentage_yearly_average
AS (
	SELECT AVG(rain_percentage), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_2
	WHERE created_at > CURRENT_DATE - interval '365' day
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
--  AVERAGE ALL TIME (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.rain_percentage_all_time_average
AS (
	SELECT AVG(rain_percentage), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_2
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
------------------------------------------
-- Soil moist percentage-- 
-- AVERAGE for today
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.soil_moist_percentage_daily_average
AS (
	SELECT AVG(soil_moist_percentage), created_at::date
	FROM metrics.sensor_2
	WHERE created_at >= CURRENT_DATE
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 7 days
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.soil_moist_percentage_weekly_average
AS (
	SELECT AVG(soil_moist_percentage), created_at::date
	FROM metrics.sensor_2
	WHERE created_at > CURRENT_DATE - interval '7' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 30 days (grouped by day)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.soil_moist_percentage_monthly_average
AS (
	SELECT AVG(soil_moist_percentage), created_at::date
	FROM metrics.sensor_2
	WHERE created_at > CURRENT_DATE - interval '30' day
	GROUP BY created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 365 days (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.soil_moist_percentage_yearly_average
AS (
	SELECT AVG(soil_moist_percentage), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_2
	WHERE created_at > CURRENT_DATE - interval '365' day
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
--  AVERAGE ALL TIME (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.soil_moist_percentage_all_time_average
AS (
	SELECT AVG(soil_moist_percentage), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
	FROM metrics.sensor_2
	GROUP BY txn_month, txn_year
	ORDER BY txn_month, txn_year ASC
) WITH DATA;
------------------------------------------
-- Rain frequency-- 
-- AVERAGE for today
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.is_raining_frequency_daily_average
AS (
	SELECT is_raining, COUNT(is_raining), created_at::date
	FROM metrics.sensor_2
	WHERE created_at >= CURRENT_DATE
	GROUP BY is_raining, created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 7 days
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.is_raining_frequency_weekly_average
AS (
	SELECT is_raining, COUNT(is_raining), created_at::date
    FROM metrics.sensor_2
    WHERE created_at > CURRENT_DATE - interval '7' day
    GROUP BY is_raining, created_at::date
    ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 30 days (grouped by day)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.is_raining_frequency_monthly_average
AS (
    SELECT is_raining, COUNT(is_raining), created_at::date
    FROM metrics.sensor_2
    WHERE created_at > CURRENT_DATE - interval '30' day
    GROUP BY is_raining, created_at::date
    ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 365 days (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.is_raining_frequency_yearly_average
AS (
	SELECT is_raining, COUNT(is_raining), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
    FROM metrics.sensor_2
    WHERE created_at > CURRENT_DATE - interval '365' day
    GROUP BY is_raining, txn_month, txn_year
    ORDER BY txn_month, txn_year ASC
) WITH DATA;
--  AVERAGE ALL TIME (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.is_raining_frequency_all_time_average
AS (
	SELECT is_raining, COUNT(is_raining), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
    FROM metrics.sensor_2
    GROUP BY is_raining, txn_month, txn_year
    ORDER BY txn_month, txn_year ASC
) WITH DATA;
------------------------------------------
-- Soil moisture frequency-- 
-- AVERAGE for today
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.is_soil_moist_frequency_daily_average
AS (
	SELECT is_soil_moist, COUNT(is_soil_moist), created_at::date
	FROM metrics.sensor_2
	WHERE created_at >= CURRENT_DATE
	GROUP BY is_soil_moist, created_at::date
	ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 7 days
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.is_soil_moist_frequency_weekly_average
AS (
	SELECT is_soil_moist, COUNT(is_soil_moist), created_at::date
    FROM metrics.sensor_2
    WHERE created_at > CURRENT_DATE - interval '7' day
    GROUP BY is_soil_moist, created_at::date
    ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 30 days (grouped by day)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.is_soil_moist_frequency_monthly_average
AS (
    SELECT is_soil_moist, COUNT(is_soil_moist), created_at::date
    FROM metrics.sensor_2
    WHERE created_at > CURRENT_DATE - interval '30' day
    GROUP BY is_soil_moist, created_at::date
    ORDER BY created_at::date DESC
) WITH DATA;
-- AVERAGE for last 365 days (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.is_soil_moist_frequency_yearly_average
AS (
	SELECT is_soil_moist, COUNT(is_soil_moist), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
    FROM metrics.sensor_2
    WHERE created_at > CURRENT_DATE - interval '365' day
    GROUP BY is_soil_moist, txn_month, txn_year
    ORDER BY txn_month, txn_year ASC
) WITH DATA;
--  AVERAGE ALL TIME (grouped by month and year)
CREATE MATERIALIZED VIEW IF NOT EXISTS metrics.is_soil_moist_frequency_all_time_average
AS (
	SELECT is_soil_moist, COUNT(is_soil_moist), date_part('month',date_trunc('month', created_at)) AS txn_month, date_part('year',date_trunc('year', created_at)) AS txn_year
    FROM metrics.sensor_2
    GROUP BY is_soil_moist, txn_month, txn_year
    ORDER BY txn_month, txn_year ASC
) WITH DATA;