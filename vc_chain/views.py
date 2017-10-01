from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
        "user": data_handler.getUserData(username, request.user.username),
        "timeline": data_handler.getTimelineData(username),
        "commit_stat": data_handler.getCommitStatsData(username),
    }
    return render(request, 'dashboard.html', data)


@login_required
def addProjectView(request, username):
    data = {
        "user": data_handler.getUserData(username, request.user.username),
    }
    return render(request, 'add-project.html', data)


@login_required
def codeEditView(request, username, projectname, branchname, filename):
    data = {
        "user": data_handler.getUserData(username, request.user.username),
        "file": data_handler.getFileCodeData(username, projectname, branchname, filename),
    }
    return render(request, 'code-edit.html', data)


def codeView(request, username, projectname, branchname, filename):
    data = {
        "user": data_handler.getUserData(username, request.user.username),
        "file": data_handler.getFileCodeData(username, projectname, branchname, filename),
    }
    return render(request, 'code-view.html', data)


def commitView(request, username, projectname, branchname, commitid):
    data = {
        "user": data_handler.getUserData(username, request.user.username),
        "commit_diff": data_handler.getCommitDiffData(username, projectname, branchname, commitid),
    }
    return render(request, 'commit-view.html', data)


def commitsListView(request, username, projectname, branchname):
    data = {
        "user": data_handler.getUserData(username, request.user.username),
        "commits": data_handler.getCommitListData(username, projectname, branchname),
    }
    return render(request, 'commits.html', data)


@login_required
def editProfileView(request, username):
    data = {
        "user": data_handler.getUserData(username, request.user.username),
    }
    return render(request, 'edit-profile.html', data)


def followersView(request, username):
    data = {
        "type": "Followers",
        "user": data_handler.getUserData(username, request.user.username),
        "people": data_handler.getFollowerData(username),
    }
    return render(request, 'people.html', data)


def followingsView(request, username):
    data = {
        "type": "Following",
        "user": data_handler.getUserData(username, request.user.username),
        "people": data_handler.getFollowingData(username),
    }
    return render(request, 'people.html', data)


def projectExplorerView(request, username, projectname, branchname=None):
    data = {
        "user": data_handler.getUserData(username, request.user.username),
        "project": data_handler.getProjectExplorerData(username, projectname, branchname, request.user.username),
    }
    return render(request, 'project-explore.html', data)


def projectsListView(request, username):
    data = {
        "type": "Projects",
        "user": data_handler.getUserData(username, request.user.username),
        "projects": data_handler.getProjectListData(username),
    }
    return render(request, 'projects.html', data)


def starProjectsListView(request, username):
    data = {
        "type": "Stars",
        "user": data_handler.getUserData(username, request.user.username),
        "projects": data_handler.getStarProjectListData(username),
    }
    return render(request, 'projects.html', data)


def forkProjectsListView(request, username):
    data = {
        "type": "Forks",
        "user": data_handler.getUserData(username, request.user.username),
        "projects": data_handler.getProjectListData(username, just_fork=True),
    }
    return render(request, 'projects.html', data)


@login_required
def addProject(request, username):
    project_name = request.POST["projectnameinput"]
    branch_name = request.POST["branchnameinput"]
    project_descr = request.POST['descriptioninput']
    commit_msg = request.POST['commitmessageinput']
    files = request.FILES.getlist('files[]')

    data_handler.addProject(username, project_name, branch_name, project_descr, commit_msg, files)

    return redirect('/user/' + request.user.username + "/projects")


@login_required
def codeEditFile(request, username, projectname, branchname):
    oldfilename = request.POST['editoroldfilename']
    filename = request.POST['editorfilename']
    code = request.POST['editorcode']
    commit_msg = request.POST['editorcommit']

    data_handler.editFile(username, projectname, branchname, oldfilename, filename, code, commit_msg)

    return redirect('/user/' + request.user.username + "/projects")


@login_required
def editProfile(request, username):
    new_name = request.POST['profileName']
    new_username = request.POST['profileUsername']
    new_email = request.POST['profileEmail']
    new_password = request.POST['profilePassword']
    if 'profileImageFile' in request.POST:
        new_image = request.POST['profileImageFile']
    elif 'profileImageFile' in request.FILES:
        new_image = request.FILES['profileImageFile']
    else:
        new_image = ''

    data_handler.editProfile(username, new_username, new_name, new_email, new_image, new_password)

    return redirect('/')


@login_required
def followUser(request, username, following):
    data_handler.addFollow(username, following)
    return followingsView(request, username)


@login_required
def unfollowUser(request, username, following):
    data_handler.removeFollow(username, following)
    return followingsView(request, username)


@login_required
def starProject(request, username, projectname, starrer):
    data_handler.addStar(username, projectname, starrer)
    return projectExplorerView(request, username, projectname)


@login_required
def unstarProject(request, username, projectname, starrer):
    data_handler.removeStar(username, projectname, starrer)
    return projectExplorerView(request, username, projectname)


@login_required
def forkProject(request, username, projectname, forker):
    data_handler.makeFork(username, projectname, forker)
    return projectsListView(request, username)
