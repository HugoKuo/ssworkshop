import time
import sys
import uuid
import os
import socket
import pyrax  # from `sudo pip install -U pyrax`

from ConfigParser import ConfigParser


CONF_FILE = "/etc/ssworkshop.conf"

def get_conf(conf_file, section="RACKSPACE"):
    # You can specify which section to return, default to "RACKSAPCE"
    c = ConfigParser()
    if not c.read(conf_file):
        print "Unable to read config file %s" % conf_file
        sys.exit(1)

    confs = dict(c.items(section))
    #confs presents as a dictionary
    return confs

def authentication(type="cloudservers"):

    # Retrieve the credential of rackspace from conf file
    # {'rax_user': '', 'region': '"DFW"', 'rax_api_key': ''}
    confs = get_conf(CONF_FILE, section="RACKSPACE")
    username = confs["rax_user"]
    api_key = confs["rax_api_key"]
    region = confs["region"]

    pyrax.set_setting("identity_type", "rackspace")
    pyrax.set_credentials(username, api_key, region=region)

    #return an instance
    return pyrax.type
