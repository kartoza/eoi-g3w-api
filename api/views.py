from core.api.base.views import G3WAPIView, Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException

from qps_timeseries.models import QpsTimeseriesProject
from .permissions import (
    GetProjectPermission
)


class QpsTimeseriesGetProjectApiView(G3WAPIView):
    """
    API for get information about PS Timeseries Project
    """

    permission_classes = (
        GetProjectPermission,
    )

    def get(self, request, *args, **kwargs):
        try:
            qps_ts_project = QpsTimeseriesProject.objects.get(project__title=kwargs['project_title'])
        except ObjectDoesNotExist:
            raise APIException('QpsTimeseriesProject object not found in DB')

        results = {
            "id": qps_ts_project.id,
            "title": kwargs['project_title'],
        }

        return Response(results)
