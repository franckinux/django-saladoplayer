#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.admin
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

import os
from photologue.models import PHOTOLOGUE_DIR

def get_image_path(instance, filename):
    if filename.count('saladoplayer') == 0 or not os.path.isabs(filename):
        #the old way
        return os.path.join(PHOTOLOGUE_DIR, 'photos', filename)
    else:
        #get rid of useless componants of the full path
        return os.path.join(PHOTOLOGUE_DIR, 'photos/saladoplayer', os.path.basename(filename))
