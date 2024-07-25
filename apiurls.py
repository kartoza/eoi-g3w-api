# coding=utf-8
from django.urls import path
from .api.views import (
    QpsTimeseriesGetProjectApiView,
    GetUser,
    GetOrCreateGroup
)


urlpatterns = [

    path(
        'api/get-project/<str:project_title>',
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

]
