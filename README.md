# FixturesDjango
Project Tutorial, How to create fixtures, loading data in Django framework
Still developing (not done yet)

# Basics

## What I've done to understand and mastering fixtures

1. Created a new project called fixtures_project.

2. Created a new app called accounts.
  
    1. Created model Account (User django model as fk)
    2. Makemigrations (on terminal)
    3. Migrate

    ## ROOT FOLDER

    ```mermaid
    graph TB
        subgraph fixture_project
        settings.py
        end
        subgraph modules
        accounts --> settings.py
        end
    ```

3. Created a super user on terminal.

4. Configured accounts to appear on Admin page 127.0.0.1:8000/admin.

5. Created plus 3 users

    1. Created usuario (user_fk)

6. Created group named Customers.

7. dumped data using:
    '''
    python manage.py dumpdata --indent 4 > ./db.json
    '''
