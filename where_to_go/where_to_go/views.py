from django.http import HttpResponse

def start_page(reqest):
    return HttpResponse('Здесь будет карта')