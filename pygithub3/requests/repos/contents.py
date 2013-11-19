#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.repos import Content

class List(Request):
    uri = '/repos/{user}/{repo}/contents/'
    resource = Content

class Get(Request):

    uri = '/repos/{user}/{repo}/contents/{path}'
    resource = Content

class Create(Request):
    uri = '/repos/{user}/{repo}/contents/{path}'
    resource = Content
    body_schema = {
        'schema': ('path', 'message', 'content', 'branch'),
        'required': ('message', 'content')
    }

class Update(Request):
    uri = '/repos/{user}/{repo}/contents/{path}'
    resource = Content
    body_schema = {
        'schema': ('path', 'message', 'content', 'branch', 'sha'),
        'required': ('message', 'content', 'sha')
    }
