-- Modelo 3: Unión de las tablas 'seller' de los esquemas laptop, mini_pc y pc
{{ config(materialized='view') }}

WITH laptop_seller AS (
    SELECT * EXCLUDE(permalink), 'laptop' AS product_type
    FROM {{ source('laptop', 'seller') }}
),
mini_pc_seller AS (
    SELECT  * EXCLUDE(permalink), 'mini_pc' AS product_type
    FROM {{ source('mini_pc', 'seller') }}
),
pc_seller AS (
    SELECT * EXCLUDE(permalink), 'pc' AS product_type
    FROM {{ source('pc', 'seller') }}
)

SELECT * FROM laptop_seller
UNION ALL
SELECT * FROM mini_pc_seller
UNION ALL
SELECT * FROM pc_seller