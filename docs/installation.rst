Installing the application
==========================

The SaladoPlayer application does not require any other application to be installed.

* insert the saladoplayer application in the INSTALLED_APPS tuple in your project settings.py::

    INSTALLED_APPS = (
    ...
    'photologue',
    'saladoplayer',
    'south',
    'tagging',
    ...
    )

* insert the saladoplayer.contextprocessor.settings in the TEMPLATE_CONTEXT_PROCESSORS tuple in your project settings.py::

    TEMPLATE_CONTEXT_PROCESSORS += (
    ...
    'saladoplayer.context_processor.settings',
    'django.core.context_processors.request',
    ...
    )

* modify the following symbols in settings.py:

    * SALADOPLAYER_DEBUG. This is a boolean value. When it is True, it displays the SaladoPlayer trace window.
    * SALADOPLAYER_FLASH_SECURE.This is a boolean value. It controls whether to use "alway" or "sameDomain" for the AllowScriptAccess parameter (see `Control access to scripts \| Host web page <http://helpx.adobe.com/flash/kb/control-access-scripts-host-web.html>`_ page from Adobe for some more explanations about this). When the value is True, "sameDomain" is used.
    * SALADOPLAYER_STATIC_URL. This is a string value. Its value is the panorama url root.
    * SALADOPLAYER_SHOW_BRANDING. This is a boolean value. When it is True, the text "Powered by SaladoPlayer" is displayed otherwise, it is not.

* create the applications database by running the following commands in your project root directory::

    $ python manage.py syncdb
    $ python manage.py migrate
    $ python manage.py plinit
    $ python manage.py spinit

plinit configures the Photologue application database. Create the "thumbnail" and "display" sizes, they will be used by Saladoplayer.

spinit configures the SaladoPlayer application database. It checks that you have created the above sizes in Photologue. It also creates a Photologue gallery named "saladoplayer" and inserts 3 hotspot images. You can change the images to redefine the hotspot images. There is currently 3 images named "see", "goto" and "info". You have to use the same names.

* there are still some simple tasks to accomplish for making this work. I will not detail here since you can find them in the general documentation of Django :

    * collect the static files
    * setup the media and static stuff in the settings.py configuration file

* sample init session :
::


  $ python manage.py syncdb
  Syncing...
  Creating tables ...
  Creating table auth_permission
  Creating table auth_group_permissions
  Creating table auth_group
  Creating table auth_user_user_permissions
  Creating table auth_user_groups
  Creating table auth_user
  Creating table django_content_type
  Creating table django_session
  Creating table django_site
  Creating table django_admin_log
  Creating table tagging_tag
  Creating table tagging_taggeditem
  Creating table south_migrationhistory
  Creating table audiotracks_track

  You just installed Django's auth system, which means you don't have any superusers defined.
  Would you like to create one now? (yes/no): yes
  Username (leave blank to use 'franck'):
  E-mail address: fbarbenoire@yahoo.fr
  Password:
  Password (again):
  Superuser created successfully.
  Installing custom SQL ...
  Installing indexes ...
  Installed 0 object(s) from 0 fixture(s)

  Synced:
  > django.contrib.auth
  > django.contrib.contenttypes
  > django.contrib.sessions
  > django.contrib.sites
  > django.contrib.messages
  > django.contrib.staticfiles
  > django.contrib.admin
  > django_extensions
  > tagging
  > south
  > audiotracks

  Not synced (use migrations):
  - photologue
  - captcha
  - saladoplayer
  (use ./manage.py migrate to migrate these)
  $ python manage.py migrate
  Running migrations for photologue:
  - Migrating forwards to 0003_auto__chg_field_photosize_name.
  > photologue:0001_initial
  > photologue:0002_auto__chg_field_gallery_title__chg_field_galleryupload_title__chg_fiel
  > photologue:0003_auto__chg_field_photosize_name
  - Loading initial data for photologue.
  Installed 0 object(s) from 0 fixture(s)
  Running migrations for captcha:
  - Migrating forwards to 0001_initial.
  > captcha:0001_initial
  - Loading initial data for captcha.
  Installed 0 object(s) from 0 fixture(s)
  Running migrations for saladoplayer:
  - Migrating forwards to 0001_initial.
  > saladoplayer:0001_initial
  - Loading initial data for saladoplayer.
  Installed 0 object(s) from 0 fixture(s)
  $ python manage.py plinit

  Photologue requires a specific photo size to display thumbnail previews in the Django admin application.
  Would you like to generate this size now? (yes, no):yes

  We will now define the "admin_thumbnail" photo size:

  Width (in pixels):200
  Height (in pixels):150
  Crop to fit? (yes, no):no
  Pre-cache? (yes, no):yes
  Increment count? (yes, no):no

  A "admin_thumbnail" photo size has been created.

  Would you like to apply a sample enhancement effect to your admin thumbnails? (yes, no):no

  Photologue comes with a set of templates for setting up a complete photo gallery. These templates require you to define both a "thumbnail" and "display" size.
  Would you like to define them now? (yes, no):yes

  We will now define the "thumbnail" photo size:

  Width (in pixels):200
  Height (in pixels):150
  Crop to fit? (yes, no):no
  Pre-cache? (yes, no):yes
  Increment count? (yes, no):no

  A "thumbnail" photo size has been created.


  We will now define the "display" photo size:

  Width (in pixels):800
  Height (in pixels):600
  Crop to fit? (yes, no):no
  Pre-cache? (yes, no):yes
  Increment count? (yes, no):no

  A "display" photo size has been created.

  Would you like to apply a sample reflection effect to your display images? (yes, no):no
  $ python manage.py spinit
  saladoplayer gallery successfuly added

