import polars as pl

# Sample DataFrame
data = {"Name": ["Alice", "Bob", "Charlie", "David"]}
df = pl.DataFrame(data)

# Convert values in the "Name" column to lowercase
df = (df
      .with_columns(pl.col("Name").str.to_lowercase().suffix("_lower"))
      .with_columns(pl.col("Name").str.to_uppercase().suffix("_upper"))     
      .with_columns(pl.col("Name").str.to_titlecase().suffix("_title"))
      .with_columns(pl.col("Name").str.lengths().suffix("_length"))    
      .with_columns(pl.col("Name").str.starts_with("A").suffix("_A"))
      .with_columns(pl.col("Name").str.contains("li").suffix("_li"))
      .with_columns(pl.col("Name").str.ends_with("e").suffix("_e"))
      .with_columns(pl.col("Name").str.replace("i", "I").suffix("_I"))
      .with_columns(pl.col("Name").str.lstrip('A|B|C|D').suffix('_left_strip_A|B|C|D'))
      .with_columns(pl.col("Name").str.rstrip('e|b|d').suffix('_Right_strip_e|b|d'))
      .with_columns(pl.col("Name").str.count_match('D').suffix('_count'))
      )

# Show the DataFrame
print(df)
