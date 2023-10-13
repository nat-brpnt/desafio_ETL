
# 🐱 Cat Rescue ETL

**[English]** This project is a simple **ETL** (*Extract, Transform, Load*) pipeline written in Python. It is designed to extract data from a .CSV file containing information about rescued cats, transform the data, and load it into a MongoDB database. The transformation involves updating adoption information for specific cats.

This pipeline is a solution to the [Explorando IA Generativa em um Pipeline de ETL com Python](https://web.dio.me/project/explorando-ia-generativa-em-um-pipeline-de-etl-com-python/learning/691df7f1-e1ad-4fc7-b643-0d800ea3fee2?back=/track/santander-bootcamp-2023-ciencia-de-dados-com-python&tab=undefined&moduleId=undefined) challenge proposed during the **Data Science** path of the [Santander Bootcamp](https://www.dio.me/users/nataliabrpnt)

## Table of Contents
1. [Getting started](https://github.com/nat-brpnt/desafio_ETL/edit/main/readME.md#getting-started)
2. [Prerequirements](https://github.com/nat-brpnt/desafio_ETL/edit/main/readME.md#prerequisites)
3. [Installation](https://github.com/nat-brpnt/desafio_ETL/edit/main/readME.md#installation)
4. [Usage](https://github.com/nat-brpnt/desafio_ETL/edit/main/readME.md#usage)
   

### Getting Started
These instructions will help you set up and run the project on your local machine.

### Prerequisites
**Python**: Ensure that you have Python installed on your machine. If not, you can download and install it from [python.org](https://www.python.org/).


### Installation
1. Clone the repository to your local machine:

    `git clone https://github.com/nat-brpnt/desafio_ETL`


2. Create a virtual environment (optional but recommended):

    `python -m venv venv`
    `source venv/bin/activate  # On Windows: venv\Scripts\activate`

3. Install the required Python packages:

    `pip install -r requirements.txt`


### Usage
1. Set up your MongoDB URI:

- Create a **'.env'** file in the project directory.

- Add the following line to the **'.env'** file with your MongoDB connection string:

    `MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>`

Replace **`<username>`**, **`<password>`**, and **`<dbname>`** with your MongoDB credentials and database name.

2. Replace the `csv_file_path` variable with the correct path to you .CSV file

3. Run the ETL pipeline:

    `python etl.py`
   
The script will perform the following tasks:

- Extract data from the CSV file.
- Transform the data by updating adoption information for specific cats and convert the data into a JSON file.
- Load the data into a MongoDB database.
  
4. After running the script, you can check your MongoDB database to verify that the data has been successfully loaded.

---

# 🐱 Cat Rescue ETL

**[Português]** Este projeto é uma pipeline **ETL** (*Extract, Transform, Load*) simples escrita em Python. Ela foi criado para extrair dados de um arquivo .CSV contendo informações sobre gatos resgatados, transformar os dados e carregá-los em um banco de dados MongoDB. A transformação envolve a atualização de informações de adoção para gatos específicos.

Essa pipeline é a solução para o desafio [Explorando IA Generativa em um Pipeline de ETL com Python](https://web.dio.me/project/explorando-ia-generativa-em-um-pipeline-de-etl-com-python/learning/691df7f1-e1ad-4fc7-b643-0d800ea3fee2?back=/track/santander-bootcamp-2023-ciencia-de-dados-com-python&tab=undefined&moduleId=undefined) proposto durante o caminho de **Data Science** do [Santander Bootcamp](https://www.dio.me/users/nataliabrpnt).

## Tabela de Conteúdos
1. [Primeiros Passos](https://github.com/nat-brpnt/desafio_ETL/edit/main/readME.md#primeiros-passos)
2. [Pré-requisitos](https://github.com/nat-brpnt/desafio_ETL/edit/main/readME.md#pr%C3%A9-requisito)
3. [Instalação](https://github.com/nat-brpnt/desafio_ETL/edit/main/readME.md#instala%C3%A7%C3%A3o)
4. [Uso](https://github.com/nat-brpnt/desafio_ETL/edit/main/readME.md#uso)
   

### Primeiros Passos
Estas instruções vão ajudar a configurar e executar o projeto localmente.

### Pré-requisito
**Python**: Certifique-se de ter o Python instalado em seu computador. Se não tiver, você pode fazer o download e instalá-lo em [python.org](https://www.python.org/).


### Instalação
1. Clone o repositório em seu computador

    `git clone https://github.com/nat-brpnt/desafio_ETL`


2. Substitua a variável `csv_file_path` com o caminho correto para seu arquivo .CSV

3. Crie um ambiente virtual (opcional, mas recomendado):

    `python -m venv venv`
    `source venv/bin/activate  # On Windows: venv\Scripts\activate`

4. Instale os pacotes Python necessários:

    `pip install -r requirements.txt`


### Uso
1. Configure sua URI do MongoDB:

- Crie um arquivo **'.env'** na pasta do projeto
  
- Adicione a seguinte linha ao arquivoe **'.env'** com sua *string( de conexão do MongoDB::

    `MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>`
  
Substitua **`<username>`**, **`<password>`**, e **`<dbname>`** por suas credenciais do MongDB e o nome do seu database.

2. Execute a pipeline ETL:

    `python etl.py`

O script realizará as seguintes tarefas:

- Extrair dados do arquivo CSV.
- Transformar os dados atualizando informações de adoção para gatos específicos e convertê-los par um arquivo JSON.
- Carregar os dados em um banco de dados MongoDB.

 3. Após a execução do script, você pode verificar seu banco de dados MongoDB para confirmar que os dados foram carregados com sucesso.

---

> “Don’t adventures ever have an end? I suppose not. Someone else always has to carry on the story.”

— Bilbo Baggins

---
<div align="center">made with ❤️ by <a href="https://github.com/nat-brpnt">nat</a>.</div>