# Este DAG simula o ambiente de produção, executando um script Python qualquer

from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.operators.ec2 import EC2StartInstanceOperator, EC2StopInstanceOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'catchup': False, # Não executa DAGs em atraso
    'start_date': datetime(2024, 7, 17),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'python_script_execution',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)

def ingest():
    # Faz a ingestão dos dados, script Python qualquer.
    # Geralmente em um ambiente de produção, este script é mais complexo e faz a ingestão de dados de diversas fontes diferentes, podendo ser uma API Rest, Webscraping, arquivos CSV, bancos de dados, etc.
    pass


def transform():
    # Faz a transformação dos dados, script Python qualquer.
    # Geralmente em um ambiente de produção, este script é mais complexo e faz a transformação dos dados, como limpeza, normalização, agregação, etc.
    pass


def load():
    # Faz o carregamento dos dados, script Python qualquer.
    # Geralmente em um ambiente de produção, este script é mais complexo e faz o carregamento dos dados em um banco de dados, data lake, data warehouse, etc.
    pass

t_ingest = PythonOperator(
    task_id='ingest',
    python_callable=ingest,
    dag=dag
)

t_transform = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag
)

t_load = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag
)


t_ingest >> t_transform >> t_load
