Configuration
=============

You configure your panorama tour by giving all the necessary informations in the administration interface.

* **Tours**. A tour is a set of panoramas. When creating a tour, you can also create panoramas in the same form. Its fields are as follows :

    * **Title**. This is a string field. This is the title of the tour. It is used as a prefix for the panorama information field.

* **Panoramas**. A panorama is a spheric image stored in a particular directory. A panorama is included in a tour. Its fields are as follows :

    * **Directory**. This is a string field. The name of the directory containing the panorama. The url of the root directory of the panorama is obtained by concataining the strings SALADOPLAYER_URL + <directory field value>.
    * **Information**. This is a string field. Its value is used as a label which is displayed when the mouse cursor is over a panorama hotspot.

* **Chainings**. A chaining record describes the link between two panoramas. It enables to display a hotspot panorama at the specified position. When you click on the hotspot, the destination panorama is displayed. Its fields are as follows :

    * **From Panorama**. The source panorama.
    * **To Panorama**. The destination panorama.
    * **Pan**. the pan parameter of the hotspot position of the destination panorama in the source panorama. You can get this value by setting SALADOPLAYER_VIEWER to True in your settings.py.
    * **Tilt**. the same as above but for the the tilt parameter.
    * **Show Information**. This is a boolean field. Whether to display or not the information of the destination panorama.

* **Initial Panoramas**. It specifies what is the first panorama which has to be displayed when the tour starts. Its fields are as follows :

    * **Tour**. The panorama tour.
    * **Panorama**. The first panorama in the tour.

* **Hotspot Informations**. It enables to display some text when the mouse cursor is over an information hotspot. Its fields are as follows :

    * **Panorama**. The panorama where the information has to be displayed in.
    * **Pan**. the pan parameter of the hotspot position in the panorama.
    * **Tilt**. the tilt parameter of the hotspot position in the panorama.
    * **Information**. This is a string field. Its value is used as a label which is displayed when the mouse cursor is over the information hotspot.
