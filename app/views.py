from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost

import os

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description",
]
class TempClass:
    x = 5

def hello(request):
    list = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = False
    context={
            "name":"Django","age": 25, 
            "first_list": list, 
            "temp_object": temp,
            "is_authenticated": is_authenticated
    }
    return render(request, "app/hello.html", context)

def job_list(request):
    jobs = JobPost.objects.all()
    context={
        "jobs": jobs
    }
    return render(request, "app/index.html", context)

def job_detail(request, job_id):
    try:
        if job_id == 0:
            return redirect(reverse('jobs_home'))
        # context={
        #     "job_title": job_title[job_id],
        #     "job_description": job_description[job_id],
        # }
        job = JobPost.objects.get(id=job_id)
        context={
            "job": job
        }
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")
