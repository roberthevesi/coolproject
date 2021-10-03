# coolproject

# Steps:
1. create virtual environment using `python -m venv .venv`
2. activate virtual environment:
    1. windows: `.venv\Scripts\activate.bat`
    2. linux/mac: `source .venv/bin/activate`
3. after activation, make sure there's `(.venv)` at the beginning
4. install requirements with `pip install -r requirements.txt`
5. create a django project: `django-admin startproject <project_name>`
6. create a django app: `django-admin startapp <app_name>`
7. to run project: `python src/manage.py runserver`