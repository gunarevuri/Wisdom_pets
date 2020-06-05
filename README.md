# Wisdom_pets
### Django
- This project based on Django framework and uses sqlite3 for database.

- To run this application just clone the project. Then required data for database models are present inside adoptions folder.
To run project make sure you have installed Django framework. 

- Check you have installed python or not. To check version can use below command


``` 
python --version

```


- I had used python 3.8 in this project

- I have provided all the required modules to run in requirements.txt file. If you want to install all prerequisites at once can use below command

```
pip3 install -r requirements.txt

```

### Migrations

- After installing required packages or modules, Crete models to our project. We can done this by making migrations and migrate command.

```

python3 manage.py makemigrations

```

Then run 

```
python3 manage.py showmigrations

```

This will show all migrations that you have made to database. These migrations were stored in migrations folder inside your adoptions app.Then follow below command to make migration successfull

```
python3 manage.py migrate

```
- Django had powerful feature which displays our project data in admin endpoint, to access that endpoint we must be a super user. Do you want to become a super user then follow below command.

```
python3 manage.py createsuperuser

```
- Then it will ask for username and password.

 
