from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from projects.forms import ProjectForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

@login_required
def create_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form_input = form.save(commit=False)
            form_input.user = request.user
            form_input.save()
            return redirect('project_index')
    else:
        form = ProjectForm()

    return render(request, 'projects/create_project.html', {
        'form': form
    })


@login_required
def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/project_index.html", context)

# @login_required
# def project_index(request):
#     # project = Project.objects.filter(user=request.user).order_by('-created_at')
#     project = Project.objects.all().order_by('-created_at')
#     context = {"project":project}
#     return render(request, "projects/project_index.html",context)


@login_required
def project_detail(request, pk):
    # project = Project.objects.filter(Project, pk=pk, user=request.user).order_by('-created_at')
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "projects/project_detail.html", context)


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
        content = {"form":form}   
    return render(request, "projects/register_user.html", content)

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect("project_index")
    return render(request, 'projects/delete_task.html', {'project':project })
    