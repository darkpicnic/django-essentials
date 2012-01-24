Django Essentials
================================================


Summary
------------------------

After building several projects, I finally made a script to do most of the work. This file currently does this:

1. creates a skeleton fabfile.py (stub code)

2. creates a skeleton requirements.txt (with Django)

3. creates a .gitignore file with these already added
	
	- venv-projectname
	- .DS_Store
	- *.pyc
	- *.db
	- local_settings.py
	
4. creates a project structure:
	
	- project_root
		
		fabfile.py
		
		requirements.txt
		
		.gitignore
		
		- project
			
			- apps
			- logs
			- config
			
				local_settings.py
				
				- dev
					
					- project.wsgi
					- settings.py
				
				- staging
					
					- project.wsgi
					- settings.py

				- prod 
				
					- project.wsgi
					- settings.py
				
			- media
			- assets
			
				- css
					
					- style.css
					
				- img
				- js
				
			- static
			- templates
				
				- base.html

5. Modifies the default settings.py file to include

	* more robust logging, including a rotating debug file
	* adds a safe import for machine specific settings files
	* uncomments the admin app include
	
6. Modifies the project urls.py

	* uncomments admin auto discover
	* adds handling of static content when in debug mode
	

Requirements
------------------------

The settings.py modifications are based on Django 1.3.1, but I doubt it would break with anything above 1.0. However, since this script is meant to be executed on initial project creation, you're not risking a lot trying it. Worst case scenario, you'll have to tweak the main settings file a bit


How do I use?
------------------------

Create a project container folder, usually named something like "projectname_project". Inside that folder, run 'django-admin.py startproject' command with the project name. Run this script from anywhere and point to the "projectname_project" folder. A prompt will appear with "What is the project name?". Enter the name you gave the project. Done.


Wishlist
------------------------

* auto sniff virtualenv, including python version
* pull down HTML5 template, bootstrap css, jquery remotely and save to file for debug environment (bootstrap.min.css has a notoriously slow load time)
* integrate better into Django command structure