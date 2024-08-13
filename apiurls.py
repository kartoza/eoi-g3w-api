# coding=utf-8
from django.urls import path
from .api.views import (
    QpsTimeseriesGetProjectApiView,
    GetUser,
    GetOrCreateGroup,
    GetProjectGroup,
    UpdateProjectTitle
)


urlpatterns = [

    path(
        'api/get-project/<str:project_name>',
        QpsTimeseriesGetProjectApiView.as_view(),
        name='qpstimeseries-get-project'
    ),

    path(
        'api/get-user/<str:username>',
        GetUser.as_view(),
        name='get-user'
    ),

    path(
        'api/get-create-group',
        GetOrCreateGroup.as_view(),
        name='get-create-group'
    ),

    path(
        'api/get-project-group/<str:group_name>',
        GetProjectGroup.as_view(),
        name='get-project-group'
    ),
    path(
        'api/update-project-title/<str:project_group_slug>/<str:project_slug>',
        UpdateProjectTitle.as_view(),
        name='update-project-slug'
    ),

]
