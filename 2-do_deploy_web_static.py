#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

# Set up connection to the servers
env.hosts = ['142.44.167.228', '144.217.246.195']

# Function to deploy the archive to the web servers
def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    # Check if the specified archive path exists
    if exists(archive_path) is False:
        return False
    try:
        # Extract file name and remove extension
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        # Target path for storing and extracting the archive
        path = "/data/web_static/releases/"
        # Copy the local archive to the server
        put(archive_path, '/tmp/')
        # Create a new directory for the archive
        run('mkdir -p {}{}/'.format(path, no_ext))
        # Extract the sent archive
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        # Remove the temporary archive
        run('rm /tmp/{}'.format(file_n))
        # Move files from the internal archive directory to the external directory
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        # Remove the internal archive directory
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')
        # Create a new symbolic link pointing to the new version
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

