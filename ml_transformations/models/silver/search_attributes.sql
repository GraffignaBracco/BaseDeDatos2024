-- Modelo 2: Unión de las tablas 'search__attributes' de los esquemas laptop, mini_pc y pc
{{ config(materialized='view') }}

WITH laptop_search_attributes AS (
    SELECT id, value_name, _dlt_parent_id, _dlt_id, 'laptop' AS product_type
    FROM {{ source('laptop', 'search__attributes') }}
),
mini_pc_search_attributes AS (
    SELECT id, value_name, _dlt_parent_id, _dlt_id, 'mini_pc' AS product_type
    FROM {{ source('mini_pc', 'search__attributes') }}
),
pc_search_attributes AS (
    SELECT id, value_name, _dlt_parent_id, _dlt_id, 'pc' AS product_type
    FROM {{ source('pc', 'search__attributes') }}
)

SELECT id, value_name, _dlt_parent_id, _dlt_id, product_type FROM laptop_search_attributes
UNION ALL
SELECT id, value_name, _dlt_parent_id, _dlt_id, product_type FROM mini_pc_search_attributes
UNION ALL
SELECT id, value_name, _dlt_parent_id, _dlt_id, product_type FROM pc_search_attributes