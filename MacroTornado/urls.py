from abc import ABC

from tornado.web import url
from tornado.web import StaticFileHandler

from apps.users import urls as user_urls
from apps.community import urls as community_urls
from apps.ueditor import urls as ueditor_urls
from apps.question import urls as question_urls
from MacroTornado.settings import settings


class MyFileHandler(StaticFileHandler, ABC):
    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.redirect('http://example.com') # Fetching a default resource


urlPattern = [
    (url("/media/(.*)", StaticFileHandler, {'path': settings["MEDIA_ROOT"]}))
]


urlPattern += user_urls.urlpattern
urlPattern += community_urls.urlpattern
urlPattern += ueditor_urls.urlpattern
urlPattern += question_urls.urlpattern
