Using the templates
===================

You can use the following templates tags for including them in your own templates :

* before using the templates, insert this in your html page::

    {% load saladoplayer %}

* **saladoplayerscript**. This template tag must inserted in the header part of the html page. Its arguments are as follows :

    * **tour_slug**. This is a string argument. This is the tour slug of the tour to be displayed.
    * **height**. This is an integer argument. This is the height of the SaladoPlayer window.
    * **width**. This is an integer argument. This is the width of the SaladoPlayer window::
    * **hotspot**. This is a string argument. Its value may be "hs" or "nohs" depending on whether you want the hotspots to be displayed or not.

        {% saladoplayerscript tour_slug height width hotspot %}

* **saladoplayerdiv** : There is no argument. This template tag must inserted in the body part of the html page where you want the tour to appear. It inserts a div html tag which id is "SaladoPlayer"::

    {% saladoplayerdiv %}
