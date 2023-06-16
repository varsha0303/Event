# EVENT Management

### 1.  `How to setup project`

#### a. Expected Python Version - 3.8.10
#### b. Below are 2 ways to create Virtual Environment

- Using "venv"

    -  python<version> -m venv <virtual-environment-name>
        e.g : python3 -m venv venv

- Using "virtualenv"

    - virtualenv <virtual-environment-name>
        e.g : virtualenv venv

#### c. Pip install for development

- pip install -r requirements.txt


#### d. Database Setup

- Database - Postgres <br>
    - [Postgress Installation Guide](https://ubuntu.com/server/docs/databases-postgresql)

- How to create database in postgres -

    - create database <database-name>;

- Add <database-name> in the settings file -

- To reset the password of database user if forgotten:

    - ALTER USER <database-user-name> WITH PASSWORD 'new_password';


### 3. `Coding Practices`

a. Use Pylint

b. Use pep8

c. If using Visual Studio as an editor then add extensions mentioned below :

- Pylint

- Error Lense

d. Expected Pylint rating should be 10.


### 4. `Code coverage`

a. [Code Coverage doumentation](https://coverage.readthedocs.io/en/7.2.7/)

b. API Testing :

- Use Django rest frameworks "APITestCase" for test cases.
