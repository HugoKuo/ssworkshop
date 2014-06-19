import time
import sys
import uuid
import os
import socket
import pyrax  # from `sudo pip install -U pyrax`
import connection

from argparse import ArgumentParser



def run(args=None):
    parsed_args = parse_args(args=args)
    args = vars(parsed_args)
    fn = args.pop('func')
    #args['config'] = ssnode.get_config(args['config'])
    print args
    return fn(**args)


def parse_args(args=None):
    parser = ArgumentParser(
        description='Manaege the workshop environment')
    subparsers = parser.add_subparsers(help='commands for ssworkshop')

    parser.add_argument('-c', '--config', type=str, default='',
                      help='Override the default config file location.')

    list_image_p = subparsers.add_parser(
        'images', help="List saved images")
    list_image_p.set_defaults(func=list_image)

    start_node_p = subparsers.add_parser(
        'start_nodes', help="To start nodes")
    start_node_p.set_defaults(func=start_ssnode)

    start_controller_p = subparsers.add_parser(
        'start_controller', help="To start controller")
    start_controller_p.set_defaults(func=start_controller)

    auto_build_p = subparsers.add_parser(
        'auto_build', help="Build the workshop environment automatically")
    auto_build_p.set_defaults(func=build_workshop)



    return parser.parse_args(args=args)




def list_image(config):
    cs = connection.authentication("cloudservers")
    images = cs.images.list()
    print images
    return


def start_nodes():
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
