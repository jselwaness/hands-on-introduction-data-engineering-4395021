from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

with DAG(
    dag_id='load_SnP',
    schedule_interval=None,
    catchup=False,
    start_date=datetime(24,1,1)
) as dag:
    
    load_task=BashOperator(
        task_id='load_SnP_task',
        bash_command='echo -e ".separator ","\n.import --skip 1 /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/manual_snp_transform.csv sp_500_sector_count" | sqlite3 /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/challenge-load-db.db',
        dag=dag
    )