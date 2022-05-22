#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive 
from the 
contents of the web_static folder of your AirBnB Clone repo, 
using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """create a pack versions"""
    local("mkdir -p versions")
    nombre = datetime.now().strftime("%Y%m%d%H%M%S")
    archivo = "versions/web_static_{}.tgz".format(nombre)
    local("tar -cvzf {} web_static".format(archivo))
    if archivo:
        return(archivo)
    else:
        return (None)
