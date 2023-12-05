from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from .models import JobPost


# Create your views here.
job_title = ["First Job", "Second Job"]

job_description = ["first job description", "second job description"]

# def hello(request):
# return HttpResponse('<h4>hello world</h4>')


class Temp_oObject:
    x = 5


def hello(request):
    list = ["alpha", "beta"]
    is_authenticated = False
    temp = Temp_oObject()
    context = {
        "name": "Ana",
        "age": 20,
        "first_list": list,
        "temp_object": temp,
        "is_authenticated": is_authenticated,
    }
    return render(request, "app/hello.html", context)


def job_list(request):
    # list_jobs = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail = reverse('job_detail', args=(job_id,))
    #     list_jobs+= f"<li><a href = '{detail}'>{j}</a></li>"
    # list_jobs += "</ul>"
    # return HttpResponse(list_jobs)
    jobs =JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, "app/index.html", context)


def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse("job_home"))
       #context = {"job_title": job_title[id], "job_description": job_description[id]}
        job = JobPost.objects.get(id =id)
        context = {"job": job}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Data not found")
