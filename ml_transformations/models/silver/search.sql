-- Modelo 1: Unión de las tablas 'search' de los esquemas laptop, mini_pc y pc
{{ config(materialized='table') }}

WITH laptop_search AS (
    SELECT id, title, condition, catalog_product_id, listing_type_id, category_id, domain_id, price, original_price, 
           sale_price__price_id, sale_price__amount, available_quantity, seller__id, seller__nickname, _dlt_load_id, _dlt_id, 'laptop' AS product_type
    FROM {{ source('laptop', 'search') }}
),
mini_pc_search AS (
    SELECT id, title, condition, catalog_product_id, listing_type_id, category_id, domain_id, price, original_price, 
           sale_price__price_id, sale_price__amount, available_quantity, seller__id, seller__nickname, _dlt_load_id, _dlt_id, 'mini_pc' AS product_type
    FROM {{ source('mini_pc', 'search') }}
),
pc_search AS (
    SELECT id, title, condition, catalog_product_id, listing_type_id, category_id, domain_id, price, original_price, 
           sale_price__price_id, sale_price__amount, available_quantity, seller__id, seller__nickname, _dlt_load_id, _dlt_id, 'pc' AS product_type
    FROM {{ source('pc', 'search') }}
),

search as (

SELECT id, title, condition, catalog_product_id, listing_type_id, category_id, domain_id, price, original_price, 
       sale_price__price_id, sale_price__amount, available_quantity, seller__id, seller__nickname, _dlt_load_id, _dlt_id, product_type 
FROM laptop_search
UNION ALL
SELECT id, title, condition, catalog_product_id, listing_type_id, category_id, domain_id, price, original_price, 
       sale_price__price_id, sale_price__amount, available_quantity, seller__id, seller__nickname, _dlt_load_id, _dlt_id, product_type 
FROM mini_pc_search
UNION ALL
SELECT id, title, condition, catalog_product_id, listing_type_id, category_id, domain_id, price, original_price, 
       sale_price__price_id, sale_price__amount, available_quantity, seller__id, seller__nickname, _dlt_load_id, _dlt_id, product_type 
FROM pc_search

)
select 
       a.id, 
       a.title,
       a.condition, 
       a.catalog_product_id, 
       a.listing_type_id, 
       a.category_id, 
       b.name as category_name,  
       a.domain_id, 
       a.price, 
       a.original_price, 
       a.sale_price__price_id, 
       a.sale_price__amount, 
       a.available_quantity, 
       a.seller__id, 
       a.seller__nickname, 
       a._dlt_load_id, 
       a._dlt_id, 
       a.product_type

from search a
left join {{ref('mla_categories')}} b
       on a.category_id = b.id