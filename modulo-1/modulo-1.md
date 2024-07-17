# **Módulo 1: Introdução ao Apache Airflow**

## **Definição e Importância**

Apache Airflow é uma plataforma de automação de workflows que permite a definição, monitoramento e gerenciamento de processos complexos. Ela é amplamente utilizada em empresas para automatizar tarefas, como coletar dados, processar informações e executar tarefas críticas.

A importância do Airflow está em sua capacidade de:

* Automatizar workflows, reduzindo a necessidade de intervenção humana
* Garantir a consistência e a reproducibilidade dos processos
* Oferecer insights sobre o desempenho dos workflows e detectar problemas


## **Componentes do Apache Airflow**

Apache Airflow é uma plataforma de automação de workflows que consiste em vários componentes trabalhando juntos para executar e gerenciar DAGs (Directed Acyclic Graphs). A seguir estão os principais componentes do Airflow:

1. **Web Server** (`airflow webserver`): O Web Server é o componente responsável por apresentar a interface gráfica do Airflow, permitindo que usuários acessem e gerenciem suas DAGs. Ele também fornece uma API RESTful para que os workflows possam ser controlados programaticamente. 

2. **Scheduler** (`airflow scheduler`): O Scheduler é o componente responsável por executar as DAGs no Airflow. Ele verifica periodicamente as DAGs para ver se elas estão prontas para serem executadas e, em seguida, inicia a execução delas. O Scheduler também gerencia a fila de tarefas (job queue) e controla o número de trabalhadores (workers) disponíveis.

3. **Worker** (`airflow worker`): O Worker é o componente responsável por executar as tarefas (tasks) individuais dentro de uma DAG. Ele comunica com o Scheduler para obter as próximas tarefas a serem executadas e, em seguida, as executa.

4. **Celery** (`airflow celery`): Celery é um framework de trabalhadores (worker queue) que permite que os workflows sejam executados de forma assíncron e escalonável. O Airflow utiliza o Celery para gerenciar a fila de tarefas (job queue) e controlar o número de trabalhadores disponíveis.

5. **Flower** (`airflow flower`): Flower é uma interface gráfica que permite que usuários monitorem e gerenciem os trabalhadores do Airflow. Ele fornece informações sobre as tarefas em andamento, como estado, tempo de execução e erros, o que ajuda a monitorar e depurar os workflows.

### **Explicação das relações entre os componentes**

* O Web Server apresenta a interface gráfica do Airflow e permite que usuários acessem e gerenciem suas DAGs.
* O Scheduler é responsável por executar as DAGs no Airflow e gerenciar a fila de tarefas (job queue).
* O Worker é o componente responsável por executar as tarefas individuais dentro de uma DAG. Ele comunica com o Scheduler para obter as próximas tarefas a serem executadas.
* Celery é um framework de trabalhadores que permite que os workflows sejam executados de forma assíncron e escalonável.
* Flower é uma interface gráfica que permite que usuários monitorem e gerenciem os trabalhadores do Airflow.

## #**Executors do Apache Airflow**

Os Executors são os responsáveis por executar as tarefas (tasks) individuais dentro de uma DAG no Airflow. Existem vários tipos de Executors no Airflow, cada um com suas características e vantagens. A seguir estão os principais Executors do Airflow:

1. **LocalExecutor** (`airflow.local_executor`): O LocalExecutor é o executor padrão do Airflow. Ele executa as tarefas locaismente no mesmo servidor onde o Web Server está rodando.

2. **CeleryExecutor** (`airflow.celery_executor`): O CeleryExecutor utiliza o framework de trabalhadores (worker queue) Celery para executar as tarefas em um pool de servidores remotos. Isso permite que os workflows sejam escalonados e executados em vários servidores, aumentando a capacidade de processamento e reduzindo a carga no servidor principal.

3. **SequentialExecutor** (`airflow.sequential_executor`): O SequentialExecutor é um executor sequencial que executa as tarefas uma após a outra, sem paralelizar nenhuma delas. Isso pode ser útil quando as tarefas têm dependências ou interações específicas.

4. **DaskExecutor** (`airflow.dask_executor`): O DaskExecutor é um executor que utiliza o framework de computação distribuída Dask para executar as tarefas em paralelo. Isso permite que os workflows sejam executados rapidamente e escalonadamente, aproveitando recursos de vários servidores.

5. **KubernetesExecutor** (`airflow.kubernetes_executor`): O KubernetesExecutor é um executor que utiliza o container orchestrator Kubernetes para executar as tarefas em containers Docker. Isso permite que os workflows sejam executados em um ambiente controlado e escalonável, com recursos de vários servidores.

6. **MesosExecutor** (`airflow.mesos_executor`): O MesosExecutor é um executor que utiliza o framework de orquestração de clusters Mesos para executar as tarefas em nodes remotos. Isso permite que os workflows sejam escalonados e executados em vários servidores, aumentando a capacidade de processamento e reduzindo a carga no servidor principal.

***Explicação das características dos Executors***

* O LocalExecutor é o mais simples e executa as tarefas localmente no mesmo servidor.
* O CeleryExecutor permite que os workflows sejam escalonados e executados em vários servidores remotos, utilizando o framework de trabalhadores (worker queue) Celery.
* O SequentialExecutor é um executor sequencial que executa as tarefas uma após a outra, sem paralelizar nenhuma delas.
* O DaskExecutor é um executor que utiliza o framework de computação distribuída Dask para executar as tarefas em paralelo.
* O KubernetesExecutor e o MesosExecutor são executores que utilizam orquestradores de containers Docker e clusters, respectivamente, para executar as tarefas em nodes remotos.


## **Instalação e Configuração Básica**

Para instalar o Airflow, você precisará:

1. Instalar o Python 3.x
2. Instalar o pip (gerenciador de pacotes do Python)
3. Executar o comando `pip install apache-airflow`

Para configurar o Airflow, você precisará:

1. Configurar o banco de dados ( SQLite ou PostgreSQL)
2. Definir as credenciais de usuário e senha
3. Configurar a porta do WebServer

### **Dicas para Instalação e Configuração**

* Verifique se você tem permissões de administrador para instalar e configurar o Airflow.
* Leia atentamente as instruções oficiais do Airflow para garantir uma configuração correta.
* Certifique-se de que a sua máquina tenha recursos suficientes (memória RAM, CPU) para executar o
Airflow.

## **Principais conceitos**

Airflow é uma ferramenta de automação de workflows e processos que fornece um ambiente robusto para
gerenciar e executar tarefas em diferentes plataformas. Aqui estão os principais conceitos do
Airflow:

### 1. **Operators (Operadores)**

Os Operadores são a base da funcionalidade do Airflow. Eles são responsáveis por executar as tarefas
específicas no workflow, como enviar emails, realizar upload de arquivos para um bucket S3 ou
executar scripts Python.

Exemplos de Operadores:

* BashOperator: Executa comandos Bash em um servidor.
* PythonOperator: Executa scripts Python.
* EmailOperator: Envia emails.

### 2. **Hooks (Ferramentas)**

As Ferramentas são uma extensão dos Operadores que fornece funcionalidades adicionais para interagir
com diferentes plataformas e serviços, como AWS, GCP, Azure, etc.

Exemplos de Ferramentas:

* AWSHook: Fornece acesso a recursos AWS, como EC2, S3, SQS, etc.
* GCPHook: Fornece acesso a recursos GCP, como Cloud Storage, Cloud SQL, etc.
* EmailHook: Envia emails utilizando serviços como Sendgrid ou Mailgun.

### 3. **Sensors (Sensores)**

Os Sensores são utilizados para monitorar o estado de uma tarefa e aguardar que ela seja concluída
antes de continuar com o workflow.

Exemplos de Sensores:

* FileSensor: Verifica se um arquivo foi criado ou modificado.
* SSH Sensor: Verifica o estado de uma máquina remota utilizando SSH.
* HTTPSensor: Verifica se um recurso HTTP está disponível.

### 4. **Connections (Conexões)**

As Conexões são configurações que permitem ao Airflow se conectar a diferentes plataformas e
serviços, como AWS, GCP, Azure, etc.

Exemplos de Conexões:

* AWS Connection: Configuração para se conectar à conta AWS.
* GCP Connection: Configuração para se conectar à conta GCP.
* Email Connection: Configuração para se conectar a um serviço de email como Sendgrid ou Mailgun.

### 5. **Variables (Variáveis)**
No Apache Airflow, uma **Variável** é um par chave-valor que pode ser utilizado para armazenar e recuperar valores ao longo de diferentes tarefas, DAGs e até mesmo todo o workflow. As variáveis são uma característica poderosa que permite dissociar a configuração do seu fluxo de trabalho da sua lógica.
Ao usar variáveis de forma eficaz, você pode tornar seus fluxos de trabalho no Airflow mais flexíveis, reutilizáveis e fáceis de manter!

**Tipos de Variáveis**

O Airflow fornece três tipos de variáveis:

1. **Variáveis de Ambiente**: Essas são variáveis definidas no nível de ambiente, o que significa que podem ser acessadas por qualquer tarefa dentro desse ambiente.
2. **Variáveis de DAG**: Essas são variáveis específicas para um DAG e apenas podem ser acessadas por tarefas dentro desse DAG.
3. **Variáveis de Tarefa**: Essas são variáveis específicas para uma única tarefa e apenas podem ser acessadas pelaquela tarefa.

**Usando Variáveis no Airflow**

Você pode usar variáveis em várias maneiras:

1. **Passando variáveis como argumentos**: Você pode passar variáveis como argumentos para operadores, como `bash_operator` ou `python_operator`.
2. **Acessando variáveis dentro de tarefas**: Você pode acessar variáveis dentro de uma tarefa usando a sintaxe `{{ var.value }}`.
3. **Usando variáveis em modelos**: Você pode usar variáveis em arquivos de modelo (por exemplo, templates Jinja) para gerar conteúdo dinâmico.

### 6. **XComs (Cross-Task Communication)**

Os XComs são uma forma de comunicação entre tarefas no Airflow, permitindo que as tarefas
compartilhem dados e resultados entre si.

Exemplos de XComs:

* Passar um valor de uma tarefa para outra.
* Compartilhar um arquivo gerado por uma tarefa com outra tarefa.
* Notificar a outro workflow sobre o resultado de uma tarefa.
