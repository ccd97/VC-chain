from django.shortcuts import render_to_response
from vc_chain import dummy_data as dummy


def indexView(request):
    return render_to_response('index.html')


def dashboardView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
        "timeline": dummy.getTimelineDummyData(),
        "commit_stat": dummy.getCommitStatsDummyData(),
    }
    return render_to_response('dashboard.html', data)


def addProjectView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
    }
    return render_to_response('add-project.html', data)


def codeEditView(request, username, projectname, branchname, filename):
    data = {
        "user": dummy.getUserDummyData(),
        "file": dummy.getFileCodeDummyData(),
    }
    return render_to_response('code-edit.html', data)


def codeView(request, username, projectname, branchname, filename):
    data = {
        "user": dummy.getUserDummyData(),
        "file": dummy.getFileCodeDummyData(),
    }
    return render_to_response('code-view.html', data)


def commitView(request, username, projectname, branchname, commitid):
    data = {
        "user": dummy.getUserDummyData(),
        "commit_diff": dummy.getCommitDiffDummyData(),
    }
    return render_to_response('commit-view.html', data)


def commitsListView(request, username, projectname, branchname):
    data = {
        "user": dummy.getUserDummyData(),
        "commits": dummy.getCommitListDummyData(),
    }
    return render_to_response('commits.html', data)


def editProfileView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
    }
    return render_to_response('edit-profile.html', data)


def peopleView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
        "people": dummy.getPeopleDummyData(),
    }
    return render_to_response('people.html', data)


def projectExplorerView(request, username, projectname, branchname=None):
    data = {
        "user": dummy.getUserDummyData(),
        "project": dummy.getProjectExplorerDummyData(),
    }
    return render_to_response('project-explore.html', data)


def projectsListView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
        "projects": dummy.getProjectListDummyData(),
    }
    return render_to_response('projects.html', data)
