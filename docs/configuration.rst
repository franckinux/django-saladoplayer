Configuration
=============

You configure your panorama tour by giving all the necessary informations in the administration interface.

* **Tour**. A tour is a set of panoramas. When creating a tour, you can also create panoramas in the same form. Its fields are as follows :

    * **Title**. This is a string field. This is the title of the tour. It is used as a prefix for the panorama information field.
    * **Title slug**. This is a string field. It is automatically generated from the title but you can change it as you like. It is used in the url for selecting the tour so be careful when you change it.
    * **Dropmenu**. This is a boolean field. It enables to display a drop menu for selecting the panorama you want to move to.
    * **Viewfinder**. This is a boolean field. It enables to  display the viewfinder (coordinates of the central point). This is useful for finding pan and tilt of the hotspots.
    * **Zoomslider**. This is a boolean field. It enables to  display of the zoom slider. By moving the cursor along the slider, you can zoom in or out the panorama.
    * **Scrollmenu**. This is a boolean field. It enables to display a scroll menu for selecting image and move the pano to the image hotspot relative to the image.
    * **Size**. This is a Photologue size. It has to be created in the Photologue interface, you can use the "display" size that Pholotogue invited you to create when you configured it. This is the size the images (from the Photologue galery) will be displayed at. Watermark and effect can be associated to the size.
    * **First panorama**. It specifies what is the first panorama which has to be displayed when the tour starts.
    * **Auto rotation**. This is a boolean field. It enables the rotation of the panorama after a 10 seconds delay.
    * **Full screener**. This is a boolean field. It enables the use of the full screener.
    * **Facebook**. This is a boolean field. It enables metadata to be embedded in the html page. This way you'll have a smart display when the html page is spcecified as a target link in Facebook.
    * **Description**. This is a text field. It is mandatory when Facebook is checked. This description will be displayed in the Facebook interface for describing the tour.
    * **Thumb**. This a Photologue image. A Photologue size named "thumbnail" is supposed to exist. The thumb image is displayed in Facebook interface when the target link is minimized.
    * **Height**. This is an Interger field. This is the height of the tour image when the target link is displayed in the Facebook interface.
    * **Width**. This is an Interger field. This is the width of the tour image when the target link is displayed in the Facebook interface.

* **Panorama**. A panorama is a spherical image stored in a particular directory. A panorama is included in a tour. Its fields are as follows :

    * **Directory**. This is a string field. This is the name of the directory containing the panorama. The url of the root directory of the panorama is obtained by concataining the strings SALADOPLAYER_URL + <directory field value>. SALADOPLAYER_URL is defined in your settings.py file (see installation page).
    * **Title**. This is a string field. Its value is used as a label which is displayed when the mouse cursor is over a panorama hotspot or in the drop menu.
    * **Initial pan**. This is float field. This is an optional information. Initial pan when entering the panorama.
    * **Initial tilt**. This is float field. This is an optional information. Initial tilt when entering the panorama.
    * **Min tilt**. This is float field. This is an optional information. Defines the lowest angle you can look downward.
    * **Max tilt**. This is float field. This is an optional information. Defines the highest angle you can look upward.
    * **Photo gallery**. This a photologue gallery. This will be used for displaying images within the tour. Two modes are currently available for displaying a gallery. As image hotspots, in this case you have to give the pan and tilt of the hotspot in the title field of the photo. The format is "title|pan|tilt", example : "Beautiful painting|63.05|10.61". As scroll menu, the images of the gallery are inserted in the menu.
    * **Direction**. This a decimal field. Difference of the initial direction of the panorama with the north direction.

* **PanoramaHotspot**. This a description of the link between two panoramas within the same tour. It enables to display a panorama hotspot at the specified position (pan and tilt) in the source panorama. When you click on the hotspot, the destination panorama is displayed. Its fields are as follows :

    * **From Panorama**. The source panorama.
    * **To Panorama**. The destination panorama.
    * **Pan**. This is float field. This is the pan parameter of the destination panorama hotspot in the source panorama. You can get pan and tilt by checking Viewfinder in the Tour configuration.
    * **Tilt**. This is float field. This the same as above but for the the tilt parameter.
    * **Show Information**. This is a boolean field. Check it for displaying the information of the destination panorama.

* **Map**. This defines an image that serves as a map for panoramas. Its fields are as follows :

    * **Map image**. This is the Photologue image that serves as the image map.
    * **Tour**. This is the tour the map belongs to.
    * **Pan shift**. This is a DecimalField. It defines the angle the top of the map makes with the north direction.

* **PanoramaMapping**. This is basically a link between a panorama and a map. Its fields are as follows :

    * **Map**. The map part of the link.
    * **Panorama**. The panorama part of the link.
    * **x**. This is an integer field. The horizontal position of the panorama in the map image.
    * **y**. This is an integer field. The vertical position of the panorama in the map image.

* **InformationHotspot**. It enables to display some text when the mouse cursor is over an information hotspot. Its fields are as follows :

    * **Panorama**. The panorama where the information has to be displayed in.
    * **Title**. This is a string field. Its value is used as a label which is displayed when the mouse cursor is over the information hotspot.
    * **Pan**. This is float field. This is the pan parameter of the information hotspot in the panorama.
    * **Tilt**. This is float field. This is the tilt parameter of the information hotspot in the panorama.

* **LinkHotspot**. It enables to open the url in a new browser window or tab. Its fields are as follows :

    * **Panorama**. The panorama where the link has to be displayed in.
    * **Url**. This is a string field. This is the url that will be opened in the Internet browser window or tab.
    * **Title**. This is a string field. Its value is used as a label which is displayed when the mouse cursor is over the link hotspot.
    * **Pan**. This is float field. This is the pan parameter of the link hotspot in the panorama.
    * **Tilt**. This is float field. This is the tilt parameter of the link hotspot in the panorama.

* **GalleryHotspot**. It enables to display a gallery in the panorama. Its fields are as follows :

    * **Panorama**. The panorama where the gallery has to be displayed in.
    * **Pan**. This is float field. This is the pan parameter of the gallery hotspot in the panorama.
    * **Tilt**. This is float field. This is the tilt parameter of the gallery hotspot in the panorama.
    * **Photo gallery**. This a photologue gallery. It contains the photos that have to be displayed in the gallery.

