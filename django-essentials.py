#!/usr/bin/python
import os,sys
import random
import string
from string import Template


REQUIREMENTS_TEMPLATE = Template("""\
Django
""")

URLS_TEMPLATE = Template("""\
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	
	# url(r'^$$', '$project_name.views.home', name='home'),
	# url(r'^$project_name/', include('$project_name.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
    )
""")


FABFILE_TEMPLATE = Template("""\
from fabric.api import *

env.user = 'root'
env.project = '$project_name'

def pack():
	# create a new source distribution as tarball
	local('git archive --format=tar HEAD | gzip > %s.tar.gz' % env.project, capture=False)
	
def dev():
	pass
	
def staging():
	pass

def prod():
	pass

def deploy():
# upload the source tarball to the temporary folder on the server
#	put('%s.tar.gz' % env.project, '/tmp/%s.tar.gz' % env.project)
#
#	# create a place where we can unzip the tarball, then enter
#	# that directory and unzip it
#	run('rm -rf /tmp/%s' % env.project)
#	run('mkdir /tmp/%s' % env.project)
#
#	# delete old project folder
#	run('rm -rf %s/%s' % ( env.target_dir, env.project ))
#
#	# delete old media folder
#	run('rm -rf %s/media' % env.media_dir)
#
#	with cd('/tmp/%s' % env.project):
#		run('tar xzf /tmp/%s.tar.gz' % env.project)
#		run('mv requirements.txt %s' % env.target_dir)
#		run('mv %s %s' % (env.project, env.target_dir))
#
#
#	with cd('%s/%s' % (env.target_dir, env.project)):
#		# move media folder
#		run('mv media %s/media' % env.media_dir)
##		with prefix('source %s/venv-revlonallaccess/bin/activate' % env.target_dir):
##			run('%s/venv-projectname/bin/python manage.py collectstatic --noinput' % env.target_dir)
#
#		# create symlink
#		run('ln -s %s local_settings.py' % env.settings_file)
#
#	# delete packaged tarball
#	local('rm %s.tar.gz' % env.project, capture=False)
#
#	# now that all is set up, delete the folder again
#	run('rm -rf /tmp/%s /tmp/%s.tar.gz' % (env.project, env.project))
#
#	# touch the wsgi file
#	run('touch %s/%s/%s.wsgi' % (env.target_dir, env.project, env.project))

""")

GITIGNORE_TEMPLATE = Template("""\
venv-$project_name
*.pyc
.DS_Store
*.db
local_settings.py
""")

HTML5_TEMPLATE = Template("""\
<!doctype html>
<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="en"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

  <title>{% block site-title %}{% endblock %}{% block page-title %}{% endblock %}</title>
  <meta name="description" content="">
  <meta name="author" content="">

  <meta name="viewport" content="width=device-width,initial-scale=1">

  <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
  <link rel="stylesheet" href="{{STATIC_URL}}css/style.css">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>

	{% block extra_css %}{% endblock %}
	{% block extra_js %}{% endblock %}

</head>

<body>
  <div id="container">
    <header>
		{% block header %}{% endblock %}
    </header>
    <div id="main" role="main">
		{% block content %}{% endblock %}
    </div>
    <footer>
		{% block footer %}{% endblock %}
    </footer>
  </div> <!--! end of #container -->


  <!--[if lt IE 7 ]>
    <script src="//ajax.googleapis.com/ajax/libs/chrome-frame/1.0.3/CFInstall.min.js"></script>
    <script>window.attachEvent('onload',function(){CFInstall.check({mode:'overlay'})})</script>
  <![endif]-->
  
</body>
</html>

""")


WSGI_TEMPLATE = Template("""\
import os, sys, site

PROJECT_ROOT = '$parent_dir'

site.addsitedir("$parent_dir/venv-$project_name/lib/python2.6/site-packages")

sys.path.append(PROJECT_ROOT)
sys.path.append(PROJECT_ROOT + '/$project_name')
os.environ['DJANGO_SETTINGS_MODULE'] = '$project_name.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
""")



MAIN_SETTINGS_TEMPLATE = Template("""\
# Django settings for $project_name project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
#    ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Add apps folder to path
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "apps"))

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$secret_key'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = '$project_name.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Uncomment the next line to enable the admin:
    'django.contrib.admin',

    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)


LOG_FILE_LOCATION = 'logs/application.log'

try:
	from config.local_settings import *
except ImportError:
	pass

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
	    'verbose': {
		    'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
	    },
	    'simple': {
		    'format': '%(levelname)s %(message)s'
	    },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'rotating_file': {
	        'level' : 'DEBUG',
	        'formatter' : 'verbose', # from the django doc example
	        'class' : 'logging.handlers.TimedRotatingFileHandler',
	        'filename' :   LOG_FILE_LOCATION, # full path works
	        'when' : 'midnight',
	        'interval' : 1,
	        'backupCount' : 7,
        }

    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'my_logger' : {
	        'handlers' : ['rotating_file'],
            'level' : 'DEBUG',
        }
    }
}


""")




LOCAL_SETTINGS_TEMPLATE = Template("""\
import os

DEBUG = 0
LOCAL = DEBUG

DOMAIN = ''

PROJECT_ROOT  = '$project_dir'
STATIC_ROOT   = ''
MEDIA_ROOT    = ''

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': '',                      # Or path to database file if using sqlite3.
		'USER': '',                      # Not used with sqlite3.
		'PASSWORD': '',                  # Not used with sqlite3.
		'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	}
}

LOG_FILE_LOCATION = os.path.join(PROJECT_ROOT, 'logs/application.log')

STATICFILES_DIRS = (
	PROJECT_ROOT + '/assets/',
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)


TEMPLATE_DIRS = (
	PROJECT_ROOT + '/templates/',
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)
""")



def make_file(target_filename, content=''):
	if not os.path.exists(target_filename):
		print "Creating file: %s" % target_filename 
		file = open(target_filename, 'w')
		file.write(content)
		file.close()
		


def create_folders(parent, targets):
	parent_path = parent
	if os.path.exists( parent_path ):
		for folder in targets:
			new_folder = os.path.join(parent_path, folder)
			if not os.path.exists(new_folder):
				print "Creating folder %s inside : %s" % (folder, parent) 
				os.makedirs(new_folder)
			else:
				print "Folder '%s' already exists, moving on" % new_folder 


if not (len(sys.argv) > 1):
	exit("You did not specify a target folder")
else:
	user_submitted_path = sys.argv[1]
	if not os.path.exists(user_submitted_path):
		exit("Hmmm... the path you suggested looks wrong...")
	else:
		print "Starting Django Essentials..."
		PROJECT_NAME = raw_input('What is the project name? : ')

		PROJECT_FOLDERS = ['apps', 'templates', 'logs', 'config', 'media', 'assets', 'static']
		ASSET_FOLDERS   = ['css', 'js', 'img']
		CONFIG_FOLDERS  = ['dev', 'staging', 'prod']

		PARENT_DIR  = user_submitted_path
		PROJECT_DIR = os.path.join(PARENT_DIR, PROJECT_NAME)

		if not os.path.exists(PROJECT_DIR):
			print "ERROR: Create project first"
			exit()
		else:
			print "Project has been created, moving on"

			# Create fabfile, .gitignore, etc
			make_file(PARENT_DIR + "/fabfile.py", FABFILE_TEMPLATE.safe_substitute( project_name=PROJECT_NAME ))
			make_file(PARENT_DIR + "/requirements.txt", REQUIREMENTS_TEMPLATE.safe_substitute())
			make_file(PARENT_DIR + "/.gitignore", GITIGNORE_TEMPLATE.safe_substitute( project_name=PROJECT_NAME ))

			# Create base folders
			create_folders(PROJECT_DIR, PROJECT_FOLDERS)
			create_folders(os.path.join(PROJECT_DIR, 'assets'), ASSET_FOLDERS)
			create_folders(os.path.join(PROJECT_DIR, 'config'), CONFIG_FOLDERS)

			# Create settings and wsgi files for each config release
			for release in CONFIG_FOLDERS:
				target_path = os.path.join(os.path.join(PROJECT_DIR, 'config'), release)
				make_file(target_path + '/project.wsgi', WSGI_TEMPLATE.safe_substitute(project_name=PROJECT_NAME, parent_dir=PARENT_DIR))
				make_file(target_path + '/settings.py', LOCAL_SETTINGS_TEMPLATE.safe_substitute(project_dir=PROJECT_DIR))


			# Open settings file and replace with custom template
			local_settings_file = os.path.join(PROJECT_DIR, 'config') + "/local_settings.py"
			make_file(local_settings_file, LOCAL_SETTINGS_TEMPLATE.safe_substitute(project_dir=PROJECT_DIR))

			# Gut settings file, replace with custom
			settings_file = os.path.join(PROJECT_DIR, 'settings.py')
			if os.path.exists( settings_file ):
				with open(settings_file, "w") as open_file:
					random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(50))
					new_settings = MAIN_SETTINGS_TEMPLATE.substitute(secret_key=random_string, project_name=PROJECT_NAME)
					open_file.write(new_settings)
			else:
				print "Could not find default settings file"

			
			# Gut urls.py file, replace with template
			urls_file = os.path.join(PROJECT_DIR, 'urls.py')
			if os.path.exists(urls_file):
				with open(urls_file, "w") as open_file:
					open_file.write( URLS_TEMPLATE.substitute(project_name=PROJECT_NAME) )
			else:
				print "Did not change primary urls file; could not be found"
			


			# Create base.html file in templates dir
			base_target_path = os.path.join(PROJECT_DIR, 'templates') + '/base.html'
			make_file(base_target_path, HTML5_TEMPLATE.safe_substitute())

			# Create style.css
			style_css_path = os.path.join(PROJECT_DIR, 'assets/css') + '/style.css'
			make_file(style_css_path, '/*  Skeleton style.css for %s  */' % PROJECT_NAME)
		