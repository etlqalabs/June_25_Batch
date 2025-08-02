# Order by ( arranging the data in ascending or descending order )
# Group by ( grouping the row level data in to summary level data )
# Merge ( similar SQL Join ( inner, left,right, outer join )
# Concat ( Appending the dataframes on top of another dataframe or side by side - similar to Union)

from sqlalchemy import create_engine
import pandas as pd
mysql_connection = create_engine("mysql+pymysql://root:Admin%40143@localhost:3308/junebatchdb")
sql_query = """select * from emp"""
df = pd.read_sql(sql_query,mysql_connection)
