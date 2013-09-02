#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, template, static_file, view, post, request, install

from bottle_sqlite import SQLitePlugin

import json

install(SQLitePlugin(dbfile='todo.db'))

@route('/todo')
@view('todo')
def todo():
	return dict()

@route('/todo/list')
def list(db):
	c = db.execute('SELECT summary, done FROM todos')
	todos = []
	for row in c.fetchall() :
		todos.append({'summary':row[0],'done':row[1]})
	return {'todos' : todos }

@post('/todo/save')
def save(db):
	todos = json.loads(request.forms.get('todos','[]'))
	db.execute('DELETE FROM todos')
	for todo in todos :
		db.execute('INSERT INTO todos (summary, done) VALUES (?, ?)', (todo['summary'], todo['done']))
	return {'msg':'ok'}

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static')