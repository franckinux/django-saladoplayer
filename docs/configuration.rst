Configuration
=============

You configure your panorama tour by giving all the necessary informations in the administration interface.

* **Tours**. A tour is a set of panoramas. When creating a tour, you can also create panoramas in the same form. Its fields are as follows :

    * **Title**. This is a string field. This is the title of the tour. It is used as a prefix for the panorama information field.
    * **Title slug**. This is a string field. It is automatically generated from the title but you can change it as you like. It is used in the url for selecting the tour so be careful when you change it.
    * **Dropmenu**. This is a boolean field. It enables to display a drop menu for selecting the panorama you want to move to.
    * **Viewfinder**. This is a boolean field. It enables to  display the viewfinder (coordinates of the central point). This is useful for finding pan and tilt of the hotspots.
    * **Zoomslider**. This is a boolean field. It enables to  display of the zoom slider. By moving the cursor along the slider, you can zoom in or out the panorama.
    * **Scrollmenu**. This is a boolean field. It enables to display a scroll menu for selecting image and move the pano to the hotspot relative to the image.
    * **Size**. This is a Photologue size. It has to be created in the Photologue interface, you can use the "display" size that Pholotogue invited you to create when you configured it. This is the size the images (from the Photologue galery) will be displayed at. Watermark and effect can be associated to the size.
    * **First panorama**. It specifies what is the first panorama which has to be displayed when the tour starts.
    * **Auto rotation**. This is a boolean field. It enables the rotation of the panorama after a 10 seconds delay.
    * **Facebook**. This is a boolean field. It enables metadata to be embedded in the html page. This way you'll have a smart display when the html page is spcecified as a target link in Facebook.
    * **Description**. This is a text field. It is mandatory when Facebook is checked. This description will be displayed in the Facebook interface for describing the tour.
    * **Thumb**. This a Photologue image. A Photologue size named "thumbnail" is supposed to exist. The thumb image is displayed in Facebook interface when the target link is minimized.
    * **Height**. This is an Interger field. This is the height of the tour image when the target link is displayed in the Facebook interface.
    * **Width**. This is an Interger field. This is the width of the tour image when the target link is displayed in the Facebook interface.

* **Panoramas**. A panorama is a spheric image stored in a particular directory. A panorama is included in a tour. Its fields are as follows :

    * **Directory**. This is a string field. The name of the directory containing the panorama. The url of the root directory of the panorama is obtained by concataining the strings SALADOPLAYER_URL + <directory field value>.
    * **Information**. This is a string field. Its value is used as a label which is displayed when the mouse cursor is over a panorama hotspot or in the drop menu.
    * **Initial pan**. This is an optional information. Initial pan when entering the panorama.
    * **Initial tilt**. This is an optional information. Initial tilt when entering the panorama.
    * **Min tilt**. This is an optional information. Defines the lowest angle you can look downward.
    * **Max tilt**. This is an optional information. Defines the highest angle you can look upward.
    * **Gallery**. This a photologue gallery. This will be used for displaying images within the tour. Two modes are currently available for displaying a gallery. As hotspots, in this case you have to give the pan and tilt of the hotspot in the title field of the photo. The format is "title|pan|tilt", example : "Beautiful painting|63.05|10.61". As scroll menu, the images of the gallery are inserted in the menu.

* **Chainings**. A chaining record describes the link between two panoramas. It enables to display a hotspot panorama at the specified position. When you click on the hotspot, the destination panorama is displayed. Its fields are as follows :

    * **From Panorama**. The source panorama.
    * **To Panorama**. The destination panorama.
    * **Pan**. the pan parameter of the hotspot position of the destination panorama in the source panorama. You can get this value by setting SALADOPLAYER_VIEWER to True in your settings.py.
    * **Tilt**. the same as above but for the the tilt parameter.
    * **Show Information**. This is a boolean field. Whether to display or not the information of the destination panorama.

* **Hotspot Informations**. It enables to display some text when the mouse cursor is over an information hotspot. Its fields are as follows :

    * **Panorama**. The panorama where the information has to be displayed in.
    * **Pan**. the pan parameter of the hotspot position in the panorama.
    * **Tilt**. the tilt parameter of the hotspot position in the panorama.
    * **Information**. This is a string field. Its value is used as a label which is displayed when the mouse cursor is over the information hotspot.
