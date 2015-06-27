from django.conf import settings

from os import listdir
from os.path import isfile, join
import os

mypath = os.path.join(settings.BASE_DIR, 'cities')

files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
