# Echelon Ignite 2013 Thailand SCM Workshop Sample App

## Prerequistes

* bottle
* sqlite3
* pytest

## Setup

  sqlite3 todo.db < etc/schema.sql

## Run App

  ./app.py

## Run Test

  py.test tests

## Create Bundle

  pip bundle -r packages.txt todo.pybundle
