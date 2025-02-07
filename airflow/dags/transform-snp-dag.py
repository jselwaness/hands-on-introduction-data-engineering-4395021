from datetime import datetime,date
from airflow.operators.python import PythonOperator
from airflow import DAG
import pandas as pd

with DAG(
    dag_id='transform_SnP',
    schedule_interval=None,
    catchup=False,
    start_date=datetime(24,1,1)
) as dag:

    def transform_data():
        """Aggregate the S&P companies by sector"""
        df = pd.read_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/manual-snp-extract.csv',header=0)
        sector_df = df.groupby('Sector',as_index=False).count()
        sector_df = sector_df.drop(columns=['Symbol'])
        sector_df.columns=['Sector','Count']
        sector_df['Date']=date.today()
        sector_df.to_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/manual-snp-transform.csv',index=False)
    
    transform_task=PythonOperator(
        task_id='transform_SnP_task',
        python_callable=transform_data,
        dag=dag,
        
    )