   select price
    from {{ ref('search') }}
    where price < 0