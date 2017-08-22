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
from vc_chain import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/(?P<username>\w{0,50})/dashboard$', views.dashboardView),
    url(r'^user/(?P<username>\w{0,50})/projects/add$', views.addProjectView),
    url(r'^user/(?P<username>\w{0,50})/projects/(?P<projectname>\w{0,50})/(?P<branchname>\w{0,50})/edit/(?P<filename>[-\w.]+)/$', views.codeEditView),
    url(r'^user/(?P<username>\w{0,50})/projects/(?P<projectname>\w{0,50})/(?P<branchname>\w{0,50})/view/(?P<filename>[-\w.]+)/$', views.codeView),
    url(r'^user/(?P<username>\w{0,50})/projects/(?P<projectname>\w{0,50})/(?P<branchname>\w{0,50})/commits/(?P<commitid>\w{0,50})/$', views.commitView),
    url(r'^user/(?P<username>\w{0,50})/projects/(?P<projectname>\w{0,50})/(?P<branchname>\w{0,50})/commits/$', views.commitsListView),
    url(r'^user/(?P<username>\w{0,50})/edit/$', views.editProfileView),
    url(r'^user/(?P<username>\w{0,50})/people/$', views.peopleView), # TODO: stars, forks, followers
    url(r'^user/(?P<username>\w{0,50})/projects/(?P<projectname>\w{0,50})/(?P<branchname>\w{0,50})/explore/$', views.projectExplorerView),
    url(r'^user/(?P<username>\w{0,50})/projects/$', views.projectsListView),
]
