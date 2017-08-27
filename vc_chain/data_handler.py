from vc_chain.models import User, Project, Star, Follow, Fork
from django.http import Http404


def getUserData(username):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    projects = Project.objects.filter(author=user)
    stars = Star.objects.filter(user=user)
    follower_count = Follow.objects.filter(followed=user).count()

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
        "img": "images/users/ccd-avatar.jpg",
        "projects": len(p_set),
        "stars": len(s_set),
        "forks": len(f_set),
        "followers": follower_count,
    }


def getProjectListData(username, just_fork=False):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    projects = Project.objects.filter(author=user)

    p_list = list()
    for p in projects:
        if just_fork and p.forked_from is None:
            continue
        star_count = Star.objects.filter(project=p).count()
        fork_count = Fork.objects.filter(original_project=p).count()
        p_list.append({
            "author": user.username,
            "name": p.name,
            "description": p.description,
            "last_update": "Apr 30",
            "stars": star_count,
            "forks": fork_count,
        })

    return list({p['name']: p for p in p_list}.values())


def getStarProjectListData(username):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    projects = Star.objects.filter(user=user)

    p_list = list()
    for s_p in projects:
        p = s_p.project
        star_count = Star.objects.filter(project=p).count()
        fork_count = Fork.objects.filter(original_project=p).count()
        p_list.append({
            "author": p.author.username,
            "name": p.name,
            "description": p.description,
            "last_update": "Apr 30",
            "stars": star_count,
            "forks": fork_count,
        })

    return list({p['name']: p for p in p_list}.values())
