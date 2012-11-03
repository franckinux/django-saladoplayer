Author
======

Franck Barbenoire <fbarbenoire@yahoo.fr>

Software version
================

Version 0.2.2, November 3rd, 2012.

License
=======

This software is released under GPL v3 license :

http://www.gnu.org/licenses/gpl-3.0.html 

Introduction
============

Django-saladoplayer is a django application for displaying spherical panoramas. It is based on the flash panorama viewer `SaladoPlayer <http://panozona.com/wiki/SaladoPlayer>`_ from Marek Standio.
All the necessary flash files and images are embedded whithin the application as static files.

This application enables you to :

* display panorama tours ;
* move from one panorama to another within a panorama tour ;
* display popup texts when the mouse cursor is over an information or panorama hotspot.

All this is available whithout the hassle to configure the html and xml files required by SaladoPlayer. As a consequence, the update of SaladoPlayer application or modules is made easy : no need to update html or xml config files. This is particulary interesting when you have a great number of panorama tours : updates and new features can be applied in one operation. Just update the django-saladoplayer application containing the new modules and the new corresponding templates, that's all!

Before you can use the application, you must fill a directory tree with panorama images respecting the `DeepZoom <http://en.wikipedia.org/wiki/Deep_Zoom>`_ format. This tree must be availaible to your browser before using it.
In the open source world, you can use `Python Deep Zoom Tools <https://github.com/openzoom/deepzoom.py>`_ or the `SaladoConverter <http://panozona.com/wiki/SaladoConverter>`_ to perform that task. These tools convert an equirectangular panorama image file into lots of image tiles.
