from pyramid.config import Configurator
import os

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # if os.environ.get('DATABASE_URL', ''):
    #     print('HELLO!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    #     settings['sqlalchemy.url'] = os.environ['DATABASE_URL', 'mysql://bd3121794ba1e4:6d936518@us-cdbr-iron-east-03.cleardb.net/heroku_e0771598287fecc?reconnect=true']
    # settings['sqlalchemy.url'] = 'sqlite:////home/calkulas/Documents/ECE651/ece651-group-project/back_end/back_end.sqlite'
    settings['sqlalchemy.url'] = 'mysql+mysqldb://bd3121794ba1e4:6d936518@us-cdbr-iron-east-03.cleardb.net/heroku_e0771598287fecc'

    with Configurator(settings=settings) as config:
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()

    return config.make_wsgi_app()
