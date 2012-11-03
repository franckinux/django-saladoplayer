Installing the application
==========================

The SaladoPlayer application does not require any other application to be installed.

* insert the saladoplayer application in the INSTALLED_APPS tuple in your project settings.py::

    INSTALLED_APPS = (
    ...
    saladoplayer,
    ...
    )

* insert the saladoplayer.contextprocessor.settings in the TEMPLATE_CONTEXT_PROCESSORS tuple in your project settings.py::

    TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    saladoplayer.context_processor.settings,
    ...
    )

* modify the following symbols in settings.py:

    * SALADOPLAYER_DEBUG. This is a boolean value. When it is True, it displays the SaladoPlayer trace window.
    * SALADOPLAYER_FLASH_SECURE.This is a boolean value. It controls whether to use "alway" or "sameDomain" for the AllowScriptAccess parameter (see `Control access to scripts \| Host web page <http://helpx.adobe.com/flash/kb/control-access-scripts-host-web.html>`_ page from Adobe for some more explanations about this). When the value is True, "sameDomain" is used.
    * SALADOPLAYER_STATIC_URL. This is a string value. Its value is the panorama url root.
    * SALADOPLAYER_SHOW_BRANDING. This is a boolean value. When it is True, the text "Powered by SaladoPlayer" is displayed otherwise, it is not.

* create the saladoplayer database by running the following command in your project root directory::

    $ python manage.py syncdb

