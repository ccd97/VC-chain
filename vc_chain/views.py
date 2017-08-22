from django.shortcuts import render_to_response


def dashboardView(request, username):
    return render_to_response('dashboard.html')


def addProjectView(request, username):
    return render_to_response('add-project.html')


def codeEditView(request, username, projectname, branchname, filename):
    return render_to_response('code-edit.html')


def codeView(request, username, projectname, branchname, filename):
    return render_to_response('code-view.html')


def commitView(request, username, projectname, branchname, commitid):
    return render_to_response('commit-view.html')


def commitsListView(request, username, projectname, branchname):
    return render_to_response('commits.html')


def editProfileView(request, username):
    return render_to_response('edit-profile.html')


def peopleView(request, username):
    return render_to_response('people.html')


def projectExplorerView(request, username, projectname, branchname):
    return render_to_response('project-explore.html')


def projectsListView(request, username):
    return render_to_response('projects.html')
