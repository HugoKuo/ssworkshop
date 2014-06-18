import time
import sys
import uuid
import os
import socket
import pyrax  # from `sudo pip install -U pyrax`


from argparse import ArgumentParser



def run(args=None):
    parsed_args = parse_args(args=args)
    #args = vars(parsed_args)
    print args
    return "123"


def parse_args(args=None):
    parser = ArgumentParser(
        description='Manaege the workshop environment')
    subparsers = parser.add_subparsers(help='commands for ssworkshop')

    parser.add_argument('-c', '--config', type=str, default='',
                      help='Override the default config file location.')

    list_image_p = subparsers.add_parser(
        'list_image', help="list saved images")

    list_image_p.set_defaults(func=list_image)

    return parser.parse_args(args=args)




def list_image():
    pass


def start_ssnode():
    pass

def start_controller():
    pass


def start_swiftnode():
    pass


def build_workshop():
    pass




#Class Connection():





#def list_images():


#def list


#List images


#List instance

#
