1. First time activating venv
venv\scripts\activate

pip install --upgrade virtualenv
virtualenv venv --python=python3.12

Below steps are working:
Set python path like C:\Program Files\Python310\Scripts\ in Environment Variable
Open PowerShell in Admin mode , and execute the below command:
Set-ExecutionPolicy Unrestricted -Force
Close PowerShell and repoen in Admin mode
Execute the below command:
venv\scripts\activate

2. py -m pip install Django (installing django)

3. 
py manage.py migrate
py manage.py runserver

4. 
A Django model is a table in your database.




