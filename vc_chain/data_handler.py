from vc_chain.models import User, Project, Star, Follow, Fork, Commit, File
from django.http import Http404
from django.contrib.auth.models import User as AuthUser
import datetime
import difflib


def getUserData(username, logined_username):
    user = User.objects.filter(username__iexact=username).first()

    if logined_username:
        curr_user = User.objects.filter(username__iexact=logined_username).first()
        user_img = curr_user.avatar
        follow_button = (not Follow.objects.filter(follower=curr_user, followed=user))
    else:
        user_img = None
        follow_button = None

    if user is None:
        raise Http404("User does not exist")

    projects = Project.objects.filter(author=user,  is_main_branch=True)
    stars = Star.objects.filter(user=user)
    following_count = Follow.objects.filter(follower=user).count()

    p_set = set()
    f_set = set()
    for p in projects:
        if p.forked_from is not None:
            f_set.add(p.forked_from)
        p_set.add(p.name)

    s_set = set()
    for s in stars:
        s_set.add(s.project.name)

    return {
        "name": user.name,
        "username": user.username,
        "email": user.email,
        "img": user.avatar,
        "user_img": user_img,
        "projects": len(p_set),
        "stars": len(s_set),
        "forks": len(f_set),
        "following": following_count,
        "follow_button": follow_button,
    }


def getProjectListData(username, just_fork=False):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    projects = Project.objects.filter(author=user,  is_main_branch=True)

    p_list = list()
    for p in projects:
        if just_fork and p.forked_from is None:
            continue
        star_count = Star.objects.filter(project=p).count()
        fork_count = Fork.objects.filter(original_project=p).count()
        f_user = "" if p.forked_from is None else p.forked_from.author.username
        f_project = "" if p.forked_from is None else p.forked_from.name
        p_list.append({
            "forked_user": f_user,
            "forked_project": f_project,
            "author": user.username,
            "name": p.name,
            "description": p.description,
            "last_update": "Apr 30",
            "stars": star_count,
            "forks": fork_count,
        })

    return p_list


def getStarProjectListData(username):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    projects = Star.objects.filter(user=user,  project__is_main_branch=True)

    p_list = list()
    for s_p in projects:
        p = s_p.project
        star_count = Star.objects.filter(project=p).count()
        fork_count = Fork.objects.filter(original_project=p).count()
        f_user = "" if p.forked_from is None else p.forked_from.author.username
        f_project = "" if p.forked_from is None else p.forked_from.name
        p_list.append({
            "forked_user": f_user,
            "forked_project": f_project,
            "author": p.author.username,
            "name": p.name,
            "description": p.description,
            "last_update": "Apr 30",
            "stars": star_count,
            "forks": fork_count,
        })

    return p_list


def getFollowerData(username):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    followers = Follow.objects.filter(followed=user)

    f_list = list()
    for f in followers:
        f_list.append({
            "name": f.follower.name,
            "username": f.follower.username,
            "email": f.follower.email,
            "img": f.follower.avatar,
        })

    return f_list


def getFollowingData(username):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    following = Follow.objects.filter(follower=user)

    f_list = list()
    for f in following:
        f_list.append({
            "name": f.followed.name,
            "username": f.followed.username,
            "email": f.followed.email,
            "img": f.followed.avatar,
        })

    return f_list


def getTimelineData(username):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    timeline_data = []

    stars_by_me = Star.objects.filter(user=user)
    for s in stars_by_me:
        timeline_data.append({
            "type": "star",
            "time": s.time,
            "puser": s.user.username,
            "suser": s.project.author.username,
            "sproject": s.project.name,
        })
    stars_to_me = Star.objects.filter(project__author=user, project__is_main_branch=True)
    for s in stars_to_me:
        timeline_data.append({
            "type": "star",
            "time": s.time,
            "puser": s.user.username,
            "suser": s.project.author.username,
            "sproject": s.project.name,
        })
    forks_by_me = Fork.objects.filter(forked_project__author=user, forked_project__is_main_branch=True)
    for f in forks_by_me:
        timeline_data.append({
            "type": "fork",
            "time": f.time,
            "puser": f.forked_project.author.username,
            "suser": f.original_project.author.username,
            "pproject": f.forked_project.name,
            "sproject": f.original_project.name,
        })

    forks_to_me = Fork.objects.filter(original_project__author=user, original_project__is_main_branch=True)
    for f in forks_to_me:
        timeline_data.append({
            "type": "fork",
            "time": f.time,
            "puser": f.forked_project.author.username,
            "suser": f.original_project.author.username,
            "pproject": f.forked_project.name,
            "sproject": f.original_project.name,
        })
    follow_me = Follow.objects.filter(followed=user)
    for f in follow_me:
        timeline_data.append({
            "type": "follow",
            "time": f.time,
            "puser": f.follower.username,
            "suser": f.followed.username,
        })
    follow_to = Follow.objects.filter(follower=user)
    for f in follow_to:
        timeline_data.append({
            "type": "follow",
            "time": f.time,
            "puser": f.follower.username,
            "suser": f.followed.username,
        })
    commits = Commit.objects.filter(project__author=user)
    for c in commits:
        timeline_data.append({
            "type": "commit",
            "time": c.time,
            "puser": c.project.author.username,
            "pproject": c.project.name,
            "branch": c.project.branch,
        })

    timeline_data = sorted(timeline_data, key=lambda k: k['time'], reverse=True)

    return timeline_data


def getCommitStatsData(username):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    commits_count = {}
    commit_data = []

    commits = Commit.objects.filter(project__author=user)
    for c in commits:
        date = c.time.date()
        if date in commits_count:
            commits_count[date] += 1
        else:
            commits_count[date] = 1

    if not commits_count:
        curr_date = datetime.datetime.now().date()
        for i in range(10):
            commit_data.append({"y": str(curr_date), "a": "0"})
            curr_date -= datetime.timedelta(days=1)
        return commit_data

    date = min(commits_count.keys()) - datetime.timedelta(days=5)
    end_date = max(commits_count.keys())

    while date <= end_date:
        if date in commits_count:
            commit_data.append({"y": str(date), "a": str(commits_count[date])})
        else:
            commit_data.append({"y": str(date), "a": "0"})
        date += datetime.timedelta(days=1)

    return commit_data


def getProjectExplorerData(username, projectname, branchname=None, logined_username=None):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    if branchname is None:
        project = Project.objects.filter(author=user, name__iexact=projectname, is_main_branch=True).first()
    else:
        project = Project.objects.filter(author=user, name__iexact=projectname, branch__iexact=branchname).first()

    if project is None:
        raise Http404("Project does not exist")

    if logined_username:
        curr_user = User.objects.filter(username__iexact=logined_username).first()
        not_starred = (not Star.objects.filter(user=curr_user, project=project))
        not_forked = (not Fork.objects.filter(original_project=project, forked_project__author=curr_user))
    else:
        not_starred = None
        not_forked = None

    files = File.objects.filter(commit__project=project).order_by('commit__time')
    current_files = {}
    file_data = []

    for f in files:
        if f.size == "0":
            current_files.pop(f.name)
        else:
            if f.previous_file is not None and f.previous_file.name != f.name:
                current_files.pop(f.previous_file.name)
            current_files[f.name] = {
                "author": f.commit.project.author,
                "last_commit": f.commit.message,
                "last_commit_time": f.commit.time,
            }

    for key, value in current_files.items():
        file_data.append({
            "name": key,
            "author": value['author'],
            "last_commit": value['last_commit'],
            "last_commit_date": value['last_commit_time'].date(),
        })

    latest_commit = max(list(current_files.values()), key=lambda x: x['last_commit_time'])

    commits_count = Commit.objects.filter(project=project).count()
    star_count = Star.objects.filter(project=project).count()
    fork_count = Fork.objects.filter(original_project=project).count()

    branches = []
    all_branches_project = Project.objects.filter(author=user, name__iexact=projectname)
    for p in all_branches_project:
        branches.append(p.branch)

    return {
        "name": project.name,
        "branch": project.branch,
        "description": project.description,
        "latest_commit_msg": latest_commit['last_commit'],
        "latest_commit_author": latest_commit['author'].username,
        "latest_commit_author_img": latest_commit['author'].avatar,
        "stars": star_count,
        "forks": fork_count,
        "commits": commits_count,
        "branches": branches,
        "files": file_data,
        "starred": not not_starred,
        "forked": not not_forked,
    }


def getCommitListData(username, projectname, branchname):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    project = Project.objects.filter(author=user, name__iexact=projectname, branch__iexact=branchname).first()

    if project is None:
        raise Http404("Project does not exist")

    commits = Commit.objects.filter(project=project)
    commits_data = {}

    for c in commits:
        date = c.time.date()
        c_data = {
            "author": c.project.author.username,
            "author_img": c.project.author.avatar,
            "message": c.message,
            "id": c.commit_id,
            "time": c.time
        }
        if date in commits_data:
            commits_data[date].append(c_data)
        else:
            commits_data[date] = [c_data]

    commits_by_date_data = []
    for key in sorted(commits_data, reverse=True):
        cmts = []
        for c in sorted(commits_data[key], key=lambda x: x['time'], reverse=True):
            cmts.append({
                "author": c['author'],
                "author_img": c['author_img'],
                "message": c['message'],
                "id": c['id'],
            })
        commits_by_date_data.append({
            "date": key,
            "commits": cmts,
        })

    return {
        "project": project.name,
        "branch": project.branch,
        "commits_by_date": commits_by_date_data,
    }


def getPrismFileType(filename):
    ext = filename.split('.')[-1].lower()
    name = filename.split('.')[0].lower()

    if name == "makefile":
        return "language-makefile"
    elif ext == "h" or ext == "c":
        return "language-c"
    elif ext == "hpp" or ext == "cpp":
        return "language-cpp"
    elif ext == "py":
        return "language-python"
    elif ext == "java":
        return "language-java"
    elif ext == "js":
        return "language-javascript"
    elif ext == "html":
        return "language-html"
    elif ext == "css":
        return "language-css"
    elif ext == "md":
        return "language-markdown"
    else:
        return "language-"+ext


def getAceFileType(filename):
    ext = filename.split('.')[-1].lower()
    name = filename.split('.')[0].lower()

    if name == "makefile":
        return "makefile"
    elif ext == "h" or ext == "c" or ext == "hpp" or ext == "cpp":
        return "c_cpp"
    elif ext == "py":
        return "python"
    elif ext == "java":
        return "java"
    elif ext == "js":
        return "javascript"
    elif ext == "html":
        return "html"
    elif ext == "css":
        return "css"
    elif ext == "md":
        return "markdown"
    else:
        return ext


def getFileCodeData(username, projectname, branchname, filename):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    project = Project.objects.filter(author=user, name__iexact=projectname, branch__iexact=branchname).first()

    if project is None:
        raise Http404("Project does not exist")

    req_file = File.objects.filter(commit__project=project, name=filename).order_by('-commit__time').first()

    if req_file is None or req_file.size == "0":
        raise Http404("File does not exist")

    return {
        "name": req_file.name,
        "project": project.name,
        "branch": project.branch,
        "size": req_file.size,
        "code": req_file.code,
        "prism_type": getPrismFileType(req_file.name),
        "ace_type": getAceFileType(req_file.name),
    }


def getCommitDiffData(username, projectname, branchname, commitid):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    project = Project.objects.filter(author=user, name__iexact=projectname, branch__iexact=branchname).first()

    if project is None:
        raise Http404("Project does not exist")

    commit = Commit.objects.filter(project=project, commit_id=commitid).first()

    if commit is None:
        raise Http404("Commit does not exist")

    diff_str = ""

    files = File.objects.filter(commit=commit)

    file_set = []
    for f in files:
        file_set.append([f.previous_file, f])

    for f_p in file_set:
        old_code = "" if f_p[0] is None else f_p[0].code.splitlines()
        new_code = "" if f_p[1].size == "0" else f_p[1].code.splitlines()
        old_file = "/dev/null" if f_p[0] is None else f_p[0].name
        new_file = "/dev/null" if f_p[1].size == "0" else f_p[1].name
        if f_p[0] is None:
            diff_str += "new file mode 100644" + '\n'
        if f_p[1].size == "0":
            diff_str += "deleted file mode 100644" + '\n'
        i = 0
        for line in difflib.unified_diff(old_code, new_code, fromfile=old_file, tofile=new_file):
            if i == 0 or i == 1:
                diff_str += line
            else:
                diff_str += line + '\n'
            i = i+1

    return {
        "project": project.name,
        "branch": project.branch,
        "author": project.author.username,
        "author_img": project.author.avatar,
        "message": commit.message,
        "commit_id": commit.commit_id,
        "date": commit.time,
        "diff": diff_str,
    }


def addProject(username, project_name, branch_name, project_descr, commit_msg, files):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    project = Project.objects.create(name=project_name, branch=branch_name, author=user, description=project_descr, is_main_branch=True)
    commit = Commit.objects.create(project=project, message=commit_msg)

    for f in files:
        File.objects.create(commit=commit, name=f.name, size=f.size, code=f.read())


def editFile(username, projectname, branchname, oldfilename, filename, code, commit_message):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    project = Project.objects.filter(author=user, name__iexact=projectname, branch__iexact=branchname).first()

    if project is None:
        raise Http404("Project does not exist")

    old_file = File.objects.filter(commit__project=project, name=oldfilename).order_by('-commit__time').first()

    commit = Commit.objects.create(project=project, message=commit_message)
    File.objects.create(commit=commit, name=filename, size=len(code), code=code, previous_file=old_file)


def deleteFile(username, projectname, branchname, filename, commit_msg):
    editFile(username, projectname, branchname, filename, filename, '', commit_msg)


def editProfile(old_username, username, name, email, avatar, password):
    user = User.objects.filter(username__iexact=old_username).first()
    authuser = AuthUser.objects.filter(username__iexact=old_username).first()

    if user is None or authuser is None:
        raise Http404("User does not exist")

    if username:
        user.username = username
    if name:
        user.name = name
    if email:
        user.email = email
    if avatar:
        user.avatar = avatar

    if password:
        authuser.set_password(password)
    if username:
        authuser.username = username

    user.save()
    authuser.save()


def addFollow(follower, following):
    follower_user = User.objects.filter(username__iexact=follower).first()
    following_user = User.objects.filter(username__iexact=following).first()

    if follower_user is None or following_user is None:
        raise Http404("User does not exist")

    Follow.objects.create(follower=follower_user, followed=following_user)


def removeFollow(follower, following):
    follower_user = User.objects.filter(username__iexact=follower).first()
    following_user = User.objects.filter(username__iexact=following).first()

    if follower_user is None or following_user is None:
        raise Http404("User does not exist")

    Follow.objects.filter(follower=follower_user, followed=following_user).delete()


def addStar(starred_user, starred_project, starrer):
    user = User.objects.filter(username__iexact=starred_user).first()
    starrer_user = User.objects.filter(username__iexact=starrer).first()

    if user is None or starred_user is None:
        raise Http404("User does not exist")

    project = Project.objects.filter(author=starrer_user, name__iexact=starred_project, is_main_branch=True).first()

    if project is None:
        raise Http404("Project does not exist")

    Star.objects.create(user=starrer_user, project=project)


def removeStar(starred_user, starred_project, starrer):
    user = User.objects.filter(username__iexact=starred_user).first()
    starrer_user = User.objects.filter(username__iexact=starrer).first()

    if user is None or starred_user is None:
        raise Http404("User does not exist")

    project = Project.objects.filter(author=starrer_user, name__iexact=starred_project, is_main_branch=True).first()

    if project is None:
        raise Http404("Project does not exist")

    Star.objects.filter(user=starrer_user, project=project).delete()


def makeFork(original_user, original_project, forker):
    user = User.objects.filter(username__iexact=original_user).first()
    forking_user = User.objects.filter(username__iexact=forker).first()

    if user is None or forking_user is None:
        raise Http404("User does not exist")

    projects = Project.objects.filter(author=user, name__iexact=original_project)

    if projects is None:
        raise Http404("Project does not exist")

    for p in projects:
        project = Project.objects.create(name=p.name, branch=p.branch, author=forking_user, description=p.description, is_main_branch=p.is_main_branch, forked_from=p)
        commits = Commit.objects.filter(project=p)
        for c in commits:
            commit = Commit.objects.create(project=project, message=c.message, time=c.time)
            files = File.objects.filter(commit=c)
            for f in files:
                if f.previous_file is not None:
                    pf = File.objects.filter(commit__project=project, name=f.previous_file.name, size=f.previous_file.size, code=f.previous_file.code).first()
                else:
                    pf = None
                File.objects.create(commit=commit, name=f.name, size=f.size, code=f.code, previous_file=pf)

    main_branch_original = Project.objects.filter(author=user, name__iexact=original_project, is_main_branch=True).first()
    main_branch_forked = Project.objects.filter(author=forking_user, name__iexact=original_project, is_main_branch=True).first()
    Fork.objects.create(forked_project=main_branch_forked, original_project=main_branch_original)
