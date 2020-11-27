from tornado import web
from peewee_async import Manager

from tornado.ioloop import IOLoop
from MacroTornado.urls import urlPattern
from MacroTornado.settings import settings, database

if __name__ == "__main__":
    import wtforms_json
    wtforms_json.init()
    app = web.Application(urlPattern, debug=True, **settings)
    app.listen(8888)

    objects = Manager(database)
    database.set_allow_sync(False)
    app.objects = objects
    io_loop = IOLoop.current()
    io_loop.start()