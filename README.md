# client-management-system
MSD Client management system assignment

Steps for running locally:

1. Go to `client-management-system` and create a virtual environment
   * Windows - `python -m virtualenv c:\path\to\venv`
   * MAC - `python3 -m virtualenv venv`
2. Go to clientms and execute below command to install required softwares as specified in requirements.txt
  `pip  install -r requirements.txt`

3. Go to `client-management-system/venv/bin` and activate virtual environment
   * Windows: `activate`
   * Mac: `source activate`
   
4. Go to `client-management-system/clientms` folder where manage.py file exists and implement database changes:
  * `python manage.py makemigrations`.  - this will create a view of database changes.
  * `python manage.py migrate`. - Makes database changes in the selected database as specified in clientms/settings.py
  
5. start python server:
   `python manage.py runserver`
    
    You should see below logs:
```
Performing system checks...

System check identified no issues (0 silenced).
September 13, 2020 - 16:43:36
Django version 2.2.16, using settings 'clientms.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

6. Open http://127.0.0.1:8000/ to view the application

  
