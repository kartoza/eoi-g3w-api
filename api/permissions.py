from rest_framework.permissions import BasePermission
from qps_timeseries.models import QpsTimeseriesProject

import logging

logger = logging.getLogger('g3w_api')

class GetProjectPermission(BasePermission):
    """ Check permission for plot data """

    def has_permission(self, request, view):

        try:

            qpsts = QpsTimeseriesProject.objects.get(project__title=view.kwargs['project_title'])

            return request.user.has_perm('qdjango.view_project', qpsts.project)

        except Exception as e:
            logger.debug(f'[QPS_TIMESERIES] - PlotDataPermission: {e}')
            return False