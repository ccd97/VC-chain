from django.shortcuts import render_to_response
from vc_chain import dummy_data as dummy


def dashboardView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
        "timeline": dummy.getTimelineDummyData(),
        "commit_stat": dummy.getCommitStatsDummyData(),
    }
    return render_to_response('dashboard.html', data)


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


def projectExplorerView(request, username, projectname, branchname=None):
    return render_to_response('project-explore.html')


def projectsListView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
        "projects": dummy.getProjectListDummyData(),
    }
    return render_to_response('projects.html', data)
