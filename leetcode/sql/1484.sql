# 1484. Group Sold Products By The Date
# group_concat : 여러 row의 값을 하나로 합칠 때(mysql)
select sell_date
    , count(distinct product) as num_sold
    , group_concat(distinct product order by product) as products
  from Activities t1
group by 1
order by 1