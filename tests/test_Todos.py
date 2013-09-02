#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Echelon Ignite 2013 Thailand
# http://e27.co/ignite/
#
# Service Configuration Management for Rapid Growth Workshop Demo
#

import todo
import sqlite3

def test_findAll(tmpdir):
    db = create_db(tmpdir)
    todos = todo.Todos(db)
    assert len(todos.findAll()) == 0

def create_db(tmpdir):
    dbfile = tmpdir.join('todo.db').realpath()
    db = sqlite3.connect(str(dbfile))
    db.execute('CREATE TABLE todos (summary text, done bool);')
    return db    