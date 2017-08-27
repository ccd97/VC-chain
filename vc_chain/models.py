from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Project(models.Model):
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=20)
    author = models.ForeignKey(User)
    forked_from = models.OneToOneField('Project', null=True, blank=True)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name + "/" + self.branch


class Star(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + "-" + str(self.project)


class Fork(models.Model):
    forked_project = models.ForeignKey(Project, related_name="project_after_fork")
    original_project = models.ForeignKey(Project, related_name="original_project")
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.forked_project) + "-" + str(self.original_project)


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name="person_following")
    followed = models.ForeignKey(User, related_name="person_followed")
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.follower) + "-" + str(self.followed)


class Commit(models.Model):
    commit_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    message = models.CharField(max_length=1024)
    time = models.DateTimeField(auto_now=True)
    previous_commit = models.OneToOneField('Commit', null=True, blank=True)

    def __str__(self):
        return str(self.project) + "-" + str(self.commit_id)


class File(models.Model):
    commit = models.ForeignKey(Commit)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    code = models.TextField()

    def __str__(self):
        return str(self.commit) + "-" + self.name
