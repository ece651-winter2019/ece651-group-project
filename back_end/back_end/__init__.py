from pyramid.config import Configurator
import os

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    if os.environ.get('DATABASE_URL', ''):
        settings['sqlalchemy.url'] = os.environ['DATABASE_URL', '']

    with Configurator(settings=settings) as config:
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()

    return config.make_wsgi_app()
