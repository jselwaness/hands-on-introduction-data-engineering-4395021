
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

# default_args={
# 	'owner': 'James',
# 	'depends_on_past': False,
# 	'email_on_failure':False,
# 	'email_on_retry':False,
# 	'retries': 0,
# 	'catchup': False,
# 	'start_date': datetime()
# }

with DAG(
	dag_id='extract_dag',
	schedule_interval=None,
    start_date=datetime(2024,1,1),
	catchup=False) as dag:

	extract_task = BashOperator(
		task_id='extract_task',
		bash_command='wget -c https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/main/data/top-level-domain-names.csv -O /workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/airflow-extract-data.csv',
		dag=dag
	)
