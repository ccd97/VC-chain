from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from vc_chain import dummy_data as dummy
from vc_chain import data_handler
from vc_chain import models


def indexView(request):
    return render(request, 'index.html')


def indexRedirect(request):
    if request.user.is_authenticated():
        return dashboardRedirect(request)
    else:
        return render(request, 'index.html')


def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    auth_user = authenticate(request, username=username, password=password)
    if auth_user is not None:
        login(request, auth_user)
        return dashboardRedirect(request)
    else:
        return indexRedirect(request)


def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    fname = request.POST['first_name']
    email = request.POST['email']
    User.objects.create_user(username=username, email=email, password=password, first_name=fname).save()
    auth_user = authenticate(request, username=username, password=password)
    if auth_user is not None:
        models.User(username=username, name=fname, email=email).save()
        login(request, auth_user)
        return dashboardRedirect(request)
    else:
        return indexRedirect(request)


def signout(request):
    logout(request)
    return redirect("/")


@login_required
def dashboardRedirect(request):
    return redirect('/user/' + request.user.username + "/dashboard")


def dashboardView(request, username):
    data = {
        "user": data_handler.getUserData(username),
        "timeline": dummy.getTimelineDummyData(),
        "commit_stat": dummy.getCommitStatsDummyData(),
    }
    return render(request, 'dashboard.html', data)


@login_required
def addProjectView(request, username):
    data = {
        "user": data_handler.getUserData(username),
    }
    return render(request, 'add-project.html', data)


@login_required
def codeEditView(request, username, projectname, branchname, filename):
    data = {
        "user": data_handler.getUserData(username),
        "file": dummy.getFileCodeDummyData(),
    }
    return render(request, 'code-edit.html', data)


def codeView(request, username, projectname, branchname, filename):
    data = {
        "user": data_handler.getUserData(username),
        "file": dummy.getFileCodeDummyData(),
    }
    return render(request, 'code-view.html', data)


def commitView(request, username, projectname, branchname, commitid):
    data = {
        "user": data_handler.getUserData(username),
        "commit_diff": dummy.getCommitDiffDummyData(),
    }
    return render(request, 'commit-view.html', data)


def commitsListView(request, username, projectname, branchname):
    data = {
        "user": data_handler.getUserData(username),
        "commits": dummy.getCommitListDummyData(),
    }
    return render(request, 'commits.html', data)


@login_required
def editProfileView(request, username):
    data = {
        "user": data_handler.getUserData(username),
    }
    return render(request, 'edit-profile.html', data)


def peopleView(request, username):
    data = {
        "user": data_handler.getUserData(username),
        "people": dummy.getPeopleDummyData(),
    }
    return render(request, 'people.html', data)


def projectExplorerView(request, username, projectname, branchname=None):
    data = {
        "user": data_handler.getUserData(username),
        "project": dummy.getProjectExplorerDummyData(),
    }
    return render(request, 'project-explore.html', data)


def projectsListView(request, username):
    data = {
        "type": "Projects",
        "user": data_handler.getUserData(username),
        "projects": data_handler.getProjectListData(username),
    }
    return render(request, 'projects.html', data)


def starProjectsListView(request, username):
    data = {
        "type": "Stars",
        "user": data_handler.getUserData(username),
        "projects": data_handler.getStarProjectListData(username),
    }
    return render(request, 'projects.html', data)


def forkProjectsListView(request, username):
    data = {
        "type": "Forks",
        "user": data_handler.getUserData(username),
        "projects": data_handler.getProjectListData(username, just_fork=True),
    }
    return render(request, 'projects.html', data)
