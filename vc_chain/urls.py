"""vc_chain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from vc_chain import views, settings
from django.conf.urls.static import static

app_name = 'vc_chain'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.indexRedirect),
    url(r'^index/$', views.indexView, name="index"),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^signout/$', views.signout, name="signout"),
    url(r'^dashboard/$', views.dashboardRedirect),
    url(r'^user/(?P<username>[\w_]{3,50})/dashboard$', views.dashboardView, name="dashboard"),
    url(r'^user/(?P<username>[\w_]{3,50})/projects/add$', views.addProjectView, name="add-project"),
    url(r'^user/(?P<username>[\w_]{3,50})/projects/(?P<projectname>[-\w_]{3,50})/(?P<branchname>[-\w_]{3,50})/edit/(?P<filename>[-\w_.]{3,50})/$', views.codeEditView, name="code-edit"),
    url(r'^user/(?P<username>[\w_]{3,50})/projects/(?P<projectname>[-\w_]{3,50})/(?P<branchname>[-\w_]{3,50})/view/(?P<filename>[-\w_.]{3,50})/$', views.codeView, name="code"),
    url(r'^user/(?P<username>[\w_]{3,50})/projects/(?P<projectname>[-\w_]{3,50})/(?P<branchname>[-\w_]{3,50})/commits/(?P<commitid>\w{1,50})/$', views.commitView, name="commit-diff"),
    url(r'^user/(?P<username>[\w_]{3,50})/projects/(?P<projectname>[-\w_]{3,50})/(?P<branchname>[-\w_]{3,50})/commits/$', views.commitsListView, name="commits-view"),
    url(r'^user/(?P<username>[\w_]{3,50})/edit/$', views.editProfileView, name="edit-profile"),
    url(r'^user/(?P<username>[\w_]{3,50})/projects/(?P<projectname>[-\w_]{3,50})/(?P<branchname>\w{3,50}|_.)/explore/$', views.projectExplorerView, name="project-explorer"),
    url(r'^user/(?P<username>[\w_]{3,50})/projects/(?P<projectname>[-\w_]{3,50})/explore/$', views.projectExplorerView, name="project-explorer"),

    url(r'^user/(?P<username>[\w_]{3,50})/projects/$', views.projectsListView, name='projects-list'),
    url(r'^user/(?P<username>[\w_]{3,50})/stars/$', views.starProjectsListView, name='stars-list'),
    url(r'^user/(?P<username>[\w_]{3,50})/forks/$', views.forkProjectsListView, name='forks-list'),

    url(r'^user/(?P<username>[\w_]{3,50})/followers/$', views.followersView, name="followers-list"),
    url(r'^user/(?P<username>[\w_]{3,50})/following/$', views.followingsView, name="following-list"),

    url(r'^user/(?P<username>[\w_]{3,50})/profile-edit/$', views.editProfile, name="edit-profile-request"),
    url(r'^user/(?P<username>[\w_]{3,50})/add-project/$', views.addProject, name="add-project-request"),
    url(r'^user/(?P<username>[\w_]{3,50})/projects/(?P<projectname>[-\w_]{3,50})/(?P<branchname>[-\w_]{3,50})/edit-file-request$', views.codeEditFile, name="code-edit-request"),
    url(r'^user/(?P<username>[\w_]{3,50})/follow/(?P<following>[\w_]{3,50})$', views.followUser, name="follow"),
    url(r'^user/(?P<username>[\w_]{3,50})/unfollow/(?P<following>[\w_]{3,50})$', views.unfollowUser, name="unfollow"),
    url(r'^user/(?P<username>[\w_]{3,50})/projects/(?P<projectname>[-\w_]{3,50})/star/(?P<starrer>[\w_]{3,50})$', views.starProject, name="project-star"),
    url(r'^user/(?P<username>[\w_]{3,50})/projects/(?P<projectname>[-\w_]{3,50})/unstar/(?P<starrer>[\w_]{3,50})$', views.unstarProject, name="project-unstar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
