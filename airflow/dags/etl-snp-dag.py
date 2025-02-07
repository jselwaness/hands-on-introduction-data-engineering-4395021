from datetime import datetime, date
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG
import pandas as pd

with DAG(
    dag_id='ETL_SnP',
    schedule_interval=None,
    catchup=False,
    start_date=datetime(24,1,1)
) as dag:
    
    extract_task=BashOperator(
        task_id='extract_SnP_task',
        bash_command='wget -c https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/main/data/constituents.csv -O /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/etl-snp-extract.csv',
        dag=dag
    )

    def transform_data():
        """Aggregate the S&P companies by sector"""
        df = pd.read_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/etl-snp-extract.csv',header=0)
        sector_df = df.groupby('Sector',as_index=False).count()
        sector_df = sector_df.drop(columns=['Symbol'])
        sector_df.columns=['Sector','Count']
        sector_df['Date']=date.today()
        sector_df.to_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/etl-snp-transform.csv',index=False)
    
    transform_task=PythonOperator(
        task_id='transform_SnP_task',
        python_callable=transform_data,
        dag=dag

    )
    
    load_task=BashOperator(
        task_id='load_SnP_task',
        bash_command='echo -e ".separator ","\n.import --skip 1 /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/etl-snp-transform.csv sp_500_sector_count" | sqlite3 /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/challenge-load-db.db',
        dag=dag
    )

    extract_task >> transform_task >> load_task