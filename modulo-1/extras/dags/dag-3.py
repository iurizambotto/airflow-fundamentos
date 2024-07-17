# Este DAG simula o ambiente de produção, executando um script Python qualquer

from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'catchup': False, # Não executa DAGs em atraso
    'start_date': datetime(2024, 7, 17),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'python_script_execution_task_decorator',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)


@task(dag=dag)
def ingest():
    # Faz a ingestão dos dados, script Python qualquer.
    # Geralmente em um ambiente de produção, este script é mais complexo e faz a ingestão de dados de diversas fontes diferentes, podendo ser uma API Rest, Webscraping, arquivos CSV, bancos de dados, etc.
    pass


@task(dag=dag)
def transform():
    # Faz a transformação dos dados, script Python qualquer.
    # Geralmente em um ambiente de produção, este script é mais complexo e faz a transformação dos dados, como limpeza, normalização, agregação, etc.
    pass


@task(dag=dag)
def load():
    # Faz o carregamento dos dados, script Python qualquer.
    # Geralmente em um ambiente de produção, este script é mais complexo e faz o carregamento dos dados em um banco de dados, data lake, data warehouse, etc.
    pass

t_ingest = ingest()
t_transform = transform()
t_load = load()

t_ingest >> t_transform >> t_load

