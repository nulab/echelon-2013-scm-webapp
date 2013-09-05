#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Echelon Ignite 2013 Thailand
# http://e27.co/ignite/
#
# Service Configuration Management for Rapid Growth Workshop Demo
#
__author__ = 'Takashi Someda <someda@nulab-inc.com>'

import bottle
from bottle import run
import todo

import sys
import os
from optparse import OptionParser


def main(argv):

    parser = OptionParser('usage: %prog [options] <space_id>')
    parser.add_option("-p", "--port", metavar="PORT", action="store", type="int", dest="port", default=5000, help="listen port")
    parser.add_option("-d", "--debug", metavar="DEBUG", action="store_true", dest="debug", default=False, help="debug flag")
    parser.add_option("-r", "--reloadable", metavar="RELOADABLE", action="store_true", dest="reloadable", default=False, help="reloadable flag")

    (options, args) = parser.parse_args(argv)

    app_root = os.path.dirname(os.path.abspath(__file__))
    view_path = os.path.join(app_root, 'views')
    bottle.TEMPLATE_PATH.append(view_path)
    todo.app_root = app_root
    todo.install_db()

    run(host='localhost', port=options.port, debug=options.debug, reloader=options.reloadable)

main(sys.argv)
