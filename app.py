#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Echelon Ignite 2013 Thailand
# http://e27.co/ignite/
#
# Service Configuration Management for Rapid Growth Workshop Demo
#
__author__ = 'Takashi Someda <someda@nulab-inc.com>'
__version__ = '0.0.1'

from bottle import run
import todo

run(host='localhost', port=8080, debug=True, reloader=True)