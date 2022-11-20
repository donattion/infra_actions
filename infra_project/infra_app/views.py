from django.http import HttpResponse
from http import HTTPStatus


def index(request):
    return HttpResponse('У меня получилось!'), HTTPStatus.OK


def second_page(request):
    return HttpResponse('А это вторая страница!'), HTTPStatus.OK
