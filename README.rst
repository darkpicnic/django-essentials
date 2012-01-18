Django Essentials
================================================

After building several projects, I finally made a script to do most of the work. This file currently does this:

* creates a skeleton fabfile.py

* creates a .gitignore file with these already added
	
	- venv-projectname
	- .DS_Store
	- *.pyc
	- *.db
	- local_settings.py
	
* creates a project structure:
	
	- project_root
		
		- project
			
			- apps
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
			