from django.contrib.auth.models import User as AuthUser
def getUserData(username, logined_username):
    if logined_username:
        curr_user = User.objects.filter(username__iexact=logined_username).first()
        user_img = curr_user.avatar
        follow_button = (not Follow.objects.filter(follower=curr_user, followed=user))
    else:
        user_img = None
        follow_button = None

        "img": user.avatar,
        "user_img": user_img,
        "follow_button": follow_button,
            "img": f.follower.avatar,
            "img": f.followed.avatar,
            "author_img": c.project.author.avatar,
        "author_img": project.author.avatar,


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