    projects = Project.objects.filter(author=user,  is_main_branch=True)
    projects = Project.objects.filter(author=user,  is_main_branch=True)
    return p_list
    projects = Star.objects.filter(user=user,  project__is_main_branch=True)
    return p_list
    stars_to_me = Star.objects.filter(project__author=user, project__is_main_branch=True)
    forks_by_me = Fork.objects.filter(forked_project__author=user, forked_project__is_main_branch=True)
    forks_to_me = Fork.objects.filter(original_project__author=user, original_project__is_main_branch=True)
        project = Project.objects.filter(name__iexact=projectname, is_main_branch=True).first()
        file_set.append([f.previous_file, f])
        i = 0
            if i == 0 or i == 1:
            i = i+1


def addProject(username, project_name, branch_name, project_descr, commit_msg, files):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    project = Project.objects.create(name=project_name, branch=branch_name, author=user, description=project_descr, is_main_branch=True)
    commit = Commit.objects.create(project=project, message=commit_msg)

    for f in files:
        File.objects.create(commit=commit, name=f.name, size=f.size, code=f.read())


def editFile(username, projectname, branchname, oldfilename, filename, code):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    project = Project.objects.filter(name__iexact=projectname, branch__iexact=branchname).first()

    if project is None:
        raise Http404("Project does not exist")

    old_file = File.objects.filter(commit__project=project, name=oldfilename).order_by('-commit__time').first()

    commit = Commit.objects.create(project=project, message=("Edit " + oldfilename))
    File.objects.create(commit=commit, name=filename, size=len(code), code=code, previous_file=old_file)