from tornado import web
from peewee_async import Manager

from tornado.ioloop import IOLoop
from MxForm.urls import urlpattern
from MxForm.settings import settings, database

if __name__ == "__main__":

    import wtforms_json
    wtforms_json.init()

    app = web.Application(urlpattern, debug=True, **settings)
    app.listen(8888)

    objects = Manager(database)
    # No need for sync anymore!
    database.set_allow_sync(False)
    app.objects = objects
    io_loop = IOLoop.current()
    io_loop.start()