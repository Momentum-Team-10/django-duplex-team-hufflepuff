# Welcome to Code_Snips!

Code_Snips is the one-stop-shop for all your convenient coding needs. With an account on Code_Snips, users can browse our library of conveniently formatted code blocks, copy and use those blocks immediately in their coding projects, or save for later in a collection of favorites. Users can also participate and contribute to the Code_Snips community by adding their own blocks of code for others to use, edit and update code they've created, and comment on other users' code_snips as well as their own.

## To Use Code_Snips
- ```git clone <repo-url>```
- Navigate to your cloned directory.
- ```pipenv install```
- ```pipenv shell```
- Navigate to the ```hufflepuff``` folder inside of the project directory. There you will find ```manage.py```, a file required to run the local server.
- ```python manage.py runserver``` will get your app up and running! Follow the http://127.0.0.1:8000/ link in your terminal, and you are good to go!

User accounts can be created from the site, however, to create an admin account, you need to run ```python manage.py createsuperuser``` from your terminal. With this account you will have access to the admin site in Code_Snips and be able to manage all user accounts and instances of created code_snips and their associated attributes.
