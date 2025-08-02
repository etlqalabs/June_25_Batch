
from sqlalchemy import create_engine
import pandas as pd
import cx_Oracle

oracle_connection = create_engine("oracle+cx_oracle://system:admin@localhost:1521/xe")
mysql_connection = create_engine("mysql+pymysql://root:Admin%40143@localhost:3308/junebatchdb")

sql_query_orcl = """select * from emp"""
df_src = pd.read_sql(sql_query_orcl,oracle_connection)


sql_query_mysql = """select * from emp"""
df_tgt = pd.read_sql(sql_query_mysql,mysql_connection)


status = df_tgt['eno'].isin(df_src['empno'])
df_ans = df_tgt[~status]
if df_ans.empty:
    print("All are matching")
else:
    print("not matching records ",df_ans)
