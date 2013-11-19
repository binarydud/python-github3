#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Service, MimeTypeMixin


class Contents(Service, MimeTypeMixin):
    def list(self, user=None, repo=None):
        request = self.make_request('repos.contents.list', user=user, repo=repo)
        return self._get(request)
    def get(self, path, user=None, repo=None):
        request = self.make_request('repos.contents.get', user=user, repo=repo, path=path)
        return self._get(request)

    def create(self, path, data, user=None, repo=None):
        request = self.make_request('repos.contents.create', user=user, repo=repo, path=path, body=data)
        return self._put(request, **self._get_mimetype_as_header())

    def update(self, path, data, user=None, repo=None):
        request = self.make_request('repos.contents.update', user=user, repo=repo, path=path, body=data)
        return self._put(request)
