# User's CRUD API

Tech requirements:
- Python version 3.8 or upper.
- SQL database (MySQL, PostgreSQL...)


## To start this script:
- Install requirements
- Create a database 
- Create file ".env" using template "env.template" 
- Change the variables in the environment file to yours SQL settings:
    * DB_HOST - host database link
    * DB_PORT - database post
    * DB_NAME - database name
    * DB_USERNAME - your database username
    * DB_PASSWORD - your database username
    * DB_DRIVER - type of database
- Run migrations
- Run script:
```
python __main__.py 
```

### Requirements installations 
```
pip install -r requirements.txt
```


### Migrations 
To run migration: 
```
aerich init -t app.TORTOISE_ORM
aerich init-db
```