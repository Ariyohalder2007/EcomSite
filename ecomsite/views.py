from django.http import HttpResponse


def index(request):
    return HttpResponse('You are Home You can go to <a href="/shop"> shop</a> or <a href="/blog"> blog</a> ')