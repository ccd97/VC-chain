from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from vc_chain import dummy_data as dummy


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
        "user": dummy.getUserDummyData(),
        "timeline": dummy.getTimelineDummyData(),
        "commit_stat": dummy.getCommitStatsDummyData(),
    }
    return render(request, 'dashboard.html', data)


@login_required
def addProjectView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
    }
    return render(request, 'add-project.html', data)


@login_required
def codeEditView(request, username, projectname, branchname, filename):
    data = {
        "user": dummy.getUserDummyData(),
        "file": dummy.getFileCodeDummyData(),
    }
    return render(request, 'code-edit.html', data)


def codeView(request, username, projectname, branchname, filename):
    data = {
        "user": dummy.getUserDummyData(),
        "file": dummy.getFileCodeDummyData(),
    }
    return render(request, 'code-view.html', data)


def commitView(request, username, projectname, branchname, commitid):
    data = {
        "user": dummy.getUserDummyData(),
        "commit_diff": dummy.getCommitDiffDummyData(),
    }
    return render(request, 'commit-view.html', data)


def commitsListView(request, username, projectname, branchname):
    data = {
        "user": dummy.getUserDummyData(),
        "commits": dummy.getCommitListDummyData(),
    }
    return render(request, 'commits.html', data)


@login_required
def editProfileView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
    }
    return render(request, 'edit-profile.html', data)


def peopleView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
        "people": dummy.getPeopleDummyData(),
    }
    return render(request, 'people.html', data)


def projectExplorerView(request, username, projectname, branchname=None):
    data = {
        "user": dummy.getUserDummyData(),
        "project": dummy.getProjectExplorerDummyData(),
    }
    return render(request, 'project-explore.html', data)


def projectsListView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
        "projects": dummy.getProjectListDummyData(),
    }
    return render(request, 'projects.html', data)
