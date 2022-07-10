
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound

from webapp.forms import Task_form
from webapp.models import Task, STATUS_CHOICES
from django.urls import reverse



def index(request):
    task = Task.objects.order_by("-created_at")
    context = {"tasks": task}
    return render(request, "index.html", context)

# def index(request):
#     guest = Guestbook.objects.order_by("-created_at").filter(status="active")
#     context = {"guest": guest}
#     return render(request, "index.html", context)


def index_view(request, **kwargs):
    pk = kwargs.get("pk")
    taskss = get_object_or_404(Task, pk=pk)
    return render(request, "task_view.html", {"taskss": taskss})


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html", {'statuses': STATUS_CHOICES})
    else:
        task = request.POST.get("task")
        status = request.POST.get("status")
        created_at = request.POST.get("created_at")
        description = request.POST.get("description")
        new_task = Task.objects.create(task=task, status=status, description=description, created_at=created_at)

        context = {"task": new_task}
        return redirect("index_view", pk=new_task.pk)




def updates(request, pk):
    record = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        task1 = Task_form(initial={
            "task": record.task,
            "description": record.description,
            "status": record.status})
        return render(request, "update.html", {"form": task1})
    else:
        form = Task_form(data=request.POST)
        if form.is_valid():
            record.task = form.cleaned_data.get("task")
            record.description = form.cleaned_data.get("description")
            record.status = form.cleaned_data.get("status")
            record.save()
            return redirect("index")
        return render(request, "update.html", {"form": form})

