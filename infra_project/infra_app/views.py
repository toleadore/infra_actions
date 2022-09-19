from django.http import HttpResponse


def index(request):
    """Главная"""
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
