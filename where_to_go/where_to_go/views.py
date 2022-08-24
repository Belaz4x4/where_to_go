from django.http import HttpResponse
from django.template import loader
def start_page(reqest):
    template = loader.get_template('index.html')
    context = {}
    rendered_page = template.render(context, reqest)
    return HttpResponse(rendered_page)