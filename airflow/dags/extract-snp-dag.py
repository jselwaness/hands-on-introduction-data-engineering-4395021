from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

with DAG(
    dag_id='extract_SnP',
    schedule_interval=None,
    catchup=False,
    start_date=datetime(24,1,1)
) as dag:
    
    extract_task=BashOperator(
        task_id='extract_SnP_task',
        bash_command='wget -c https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/main/data/constituents.csv -O /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/manual-snp-extract.csv',
        dag=dag
    )