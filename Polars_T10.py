
# %%timeit
import polars as pl
from polars import (
    col,
    sum)

df = pl.scan_csv(
    source="C:\\Users\\user\\Desktop\\Car_Sales.csv",
    separator=',',
    encoding='utf8-lossy',
    has_header=True)\
    .groupby(['brand', 'name', 'bodyType', 'color', 'fuelType'])\
    .agg(sum("price").alias("Total Price"))\
    .filter((col("bodyType") == "sedan") & (col("color") == "blue"))

context = pl.SQLContext()
context.register("Car_Sales_df", df)

df2 = context.query("""
select * 
from Car_Sales_df
where 
brand = 'Toyota' and 
color = 'blue' and 
bodyType = 'sedan' and 
fuelType = 'Gasoline' and 
name = 'Crown Majesta'
"""
                    )

print(df2)
