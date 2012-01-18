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