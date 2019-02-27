from django.shortcuts import render
from django.http import HttpResponse

from django.db import connection

def index(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM doctors''')
    data = cursor.fetchall()
    print(data)

    # db_conn = connections['default']
    # try:
    #     c = db_conn.cursor()
    # except OperationalError:
    #     connected = False
    # else:
    #     connected = True
    # print(connected)
    return HttpResponse("Hello, world.")

