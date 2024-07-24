# coding=utf-8
from django.urls import path
from .api.views import (
    QpsTimeseriesGetProjectApiView
)


urlpatterns = [

    path(
        'api/get-project/<str:project_title>',
        QpsTimeseriesGetProjectApiView.as_view(),
        name='qpstimeseries-get-project'
    ),

]
