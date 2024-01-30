from django.shortcuts import render
from django.http import HttpResponse

job_title = [
    "First Job",
    "Second Job"
]

job_description = [
    "First job description",
    "Second job description",
]

# Create your views here.
def hello(request):
    return HttpResponse("<h3>Hello World<h3>")

def job_detail(request, id):
    return_html = f"<h1>{job_title[int(id)]}</h1> <h3>{job_description[int(id)]}</h3>"
    return HttpResponse(return_html)