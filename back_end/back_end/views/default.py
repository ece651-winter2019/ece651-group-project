from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from .. import models

# @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
# def my_view(request):
#     # try:
#     #     query = request.dbsession.query(models.MyModel)
#     #     one = query.filter(models.MyModel.name == 'one').first()
#     # except DBAPIError:
#     #     return Response(db_err_msg, content_type='text/plain', status=500)
#     print(request.dbsession.execute('SELECT * FROM doctors').fetchall())
#     return {'one': 'ONE', 'project': type(request.dbsession)}

@view_config(route_name='home', renderer=None)
def my_view(request):
    # try:
    #     query = request.dbsession.query(models.MyModel)
    #     one = query.filter(models.MyModel.name == 'one').first()
    # except DBAPIError:
    #     return Response(db_err_msg, content_type='text/plain', status=500)
    result = request.dbsession.execute('SELECT * FROM doctors').fetchall()
    return Response(str(result))
