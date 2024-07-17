# Este exemplo demonstra como criar uma conexão SSH no Airflow e usar o SSHOperator para executar um comando SSH em uma máquina remota.

from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.operators.ec2 import EC2StartInstanceOperator, EC2StopInstanceOperator
from airflow.providers.ssh.operators.ssh import SSHOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'catchup': False, # Não executa DAGs em atraso
    'start_date': datetime(2024, 7, 17),
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
}

ec2_dag = DAG(
    'ec2_start_and_ssh_execution',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)

# Para criar conexão SSH
ssh_conn_id = 'my_ssh_conn'
ssh_username = 'ec2-user'
ssh_keyfile = '/path/to/your/private/key.pem'

t_ec2_start = EC2StartInstanceOperator(
    task_id='ec2_start',
    instance_id=['i-12345678'],
    dag=ec2_dag
)

t_ssh_execution = SSHOperator(
    task_id='ssh_execution',
    ssh_conn_id=ssh_conn_id,
    command='echo "Hello, World!" && sleep 30',
    dag=ec2_dag
)

t_ec2_stop = EC2StopInstanceOperator(
    task_id='ec2_stop',
    instance_id=['i-12345678'],
    dag=ec2_dag
)

t_ec2_start >> t_ssh_execution >> t_ec2_stop

