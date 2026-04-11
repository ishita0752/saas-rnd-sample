from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
import pathlib

def home_page_view(request,*args,**kwargs):
    qs=PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=request.path)
    my_title="My page"
    my_conteext={
        "page_title":my_title,
        "page_visit_count":page_qs.count(),
        "total_visit_count":qs.count(),
    }
    path=request.path
    html_template="home.html"
    PageVisit.objects.create(path=request.path)
    return render(request,html_template,my_conteext)