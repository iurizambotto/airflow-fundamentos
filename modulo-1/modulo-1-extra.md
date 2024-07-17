
# **Módulo Extra: Subindo o Airflow com Docker e Docker-Compose, incluindo o PostgreSQL**

## **Introdução**

Em muitos casos, é mais fácil e seguro subir o Airflow em uma ambiente containerizada usando Docker e Docker-Compose. Isso permite que você gerencie as dependências e a configuração do Airflow de forma isolada e reprodutível.

## **Subindo o Airflow com Docker e PostgreSQL**

1. **Crie um arquivo `docker-compose.yml`**: para não precisarmos criar, utilize o arquivo `modulo-1/extras/docker-compose.yaml`, ou seja, no seu terminal vá para a pasta `modulo-1/extras/`.
2. **Suba o Airflow**: Execute o comando `docker-compose up -d` para subir o Airflow e o PostgreSQL em containers isolados.
3. **Acesse o Airflow**: Acesse o Airflow na porta 8080 (ou a porta configurada no arquivo `docker-compose.yml`) e inicie sessão com as credenciais de usuário e senha configuradas.

## **Explicação das variáveis**

* `AIRFLOW_DB_HOST`: Endereço do banco de dados, que é o container `postgres`.
* `AIRFLOW_DB_USER` e `AIRFLOW_DB_PASSWORD`: Usuário e senha para o banco de dados.
* `AIRFLOW_DB_PORT`: Porta do banco de dados.

## **Dicas para Subir o Airflow com Docker e Docker-Compose**

* Certifique-se de que você tenha instalado o Docker e o Docker-Compose em sua máquina.
* Leia atentamente as instruções oficiais do Airflow para garantir uma configuração correta.
* Se você estiver usando um container, certifique-se de que a porta 8080 esteja disponível e não está
sendo usada por outro processo.

Essas são algumas informações importantes sobre como subir o Airflow com Docker e Docker-Compose, incluindo o PostgreSQL. Isso permite que você tenha mais controle sobre a configuração do Airflow e faça deploy da ferramenta de forma isolada e reprodutível.