# Django on Vercel

A Simple Starter Template which helps to Deploy a **Django Project on Vercel** as a **Serverless Function** .

This App is Configured with Postgres as the Choice of Database.

- [x] Configured with Static Files in Production.
- [x] Compatable with Postgres/MySQL DB.

```sh
ls
	build.sh            # Build Script for Vercel
	manage.py  
	poetry.lock  	    # Lock All Dependency
	pyproject.toml      # Package Manager
	pyvenv.cfg  
	README.md  
	requirements.txt    # Python Requirements
	static  			# Add Your Static (Empty on Purpose)
	templates  			# Django Templates
	backend  			# Django Project Root
	vercel.json			# Vercel Configuration
```

## Get & Running on your Local Machine

- Clone the **Repo**
```sh
cd ~/Dev/
mkdir django_vercel
cd django_vercel
git clone https://github.com/Arvind-4/Django-with-Vercel.git .
```
- Create a **Virtual Environment** for **Python**
	- using **Poetry**
	```python
	virtualenv --python=python3.9 .
	source bin/activate
	poetry install
	```
	- using **Virtualenv**
	```python
	virtualenv --python=python3.9 .
	source bin/activate
	pip install -r requirements.txt
	```
	
- Run Locally
```python
cd ~/Dev/django_vercel
python manage.py runserver
```
