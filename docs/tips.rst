Tips
====

Here are some tips and common mistakes.

When working with a remote host :

* Don't forget to collect static files. Then upload these files in a directory so that they can be served by a dedicated server. Read the official documentation about static files ;

* If you have installed the packages as eggs directories, don't forget to add ``django.template.loaders.eggs.Loader`` to your ``TEMPLATE_LOADERS`` tuple in your settings ;
