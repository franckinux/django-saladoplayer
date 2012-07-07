Author
======

Franck Barbenoire <fbarbenoire@yahoo.fr>

Software version
================

Version 0.1.1, July 2012.

License
=======

This software is released under GPL v3 license :

http://www.gnu.org/licenses/gpl-3.0.html 

Introduction
============

Django-saladoplayer is a django application for displaying spherical panoramas. It is based on the flash panorama viewer `SaladoPlayer <http://panozona.com/wiki/SaladoPlayer>`_ from Marek Standio.
All the necessary flash files and images are embedded whithin the application as static files.

This application enables you to :

* display panorama tours.
* move from one panorama to another within a panorama tour.
* display popup texts when the mouse cursor is over an information hotspot.

All this is available whithout the hassle to configure the html and xml files required by SaladoPlayer.

Before you can use the application, you must fill a directory tree with panorama images respecting the `DeepZoom <http://en.wikipedia.org/wiki/Deep_Zoom>`_ format .
In the open source world, you can use `Python Deep Zoom Tools <https://github.com/openzoom/deepzoom.py>`_ or the `SaladoConverter <http://panozona.com/wiki/SaladoConverter>`_ for that task. They convert an equirectangular panorama image file into lots of image tiles.
