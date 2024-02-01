#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime  # Import the datetime module to work with dates and times
from fabric.api import local  # Import the local function from the fabric.api module
from os.path import isdir  # Import the isdir function from the os.path module


def do_pack():
    """generates a tgz archive"""
    try:
        # Get the current date and time in the format YYYYMMDDHHMMSS
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        # Check if the "versions" directory exists, if not, create it
        if isdir("versions") is False:
            local("mkdir versions")
        # Define the file name for the archive using the current date and time
        file_name = "versions/web_static_{}.tgz".format(date)
        # Create the .tgz archive by compressing the contents of the "web_static" folder
        local("tar -cvzf {} web_static".format(file_name))
        # Return the file name of the created archive
        return file_name
    except:
        # If an exception occurs during the process, return None
        return None

