WITH productos_con_procesador_i7 AS 
(
SELECT 
    _dlt_parent_id

FROM {{ ref('search_attributes')}} a 
WHERE id = 'PROCESSOR_LINE'
AND value_name = 'Core i7'
)


SELECT 
    a.id product_id,
    a.title,
    seller__nickname as vendedor,
    a.product_type as tipo_de_producto,
    seller_reputation__power_seller_status as reputacion,
    condition,
    address__state as provincia,
    available_quantity as cantidad_disponible,
    price as precio


FROM {{ ref('search')}} a 
LEFT JOIN {{ ref('seller')}} b ON a.seller__id = b.id

WHERE a._dlt_id IN (SELECT * FROM productos_con_procesador_i7)