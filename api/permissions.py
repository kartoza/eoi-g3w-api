from rest_framework.permissions import BasePermission
from qps_timeseries.models import QpsTimeseriesProject

import logging

logger = logging.getLogger('g3w_api')


class BaseSuperuserPermission(BasePermission):
    """ Check permission for getting or creating Group """

    def has_permission(self, request, view):
        return request.user.is_superuser


class GetProjectPermission(BasePermission):
    """ Check permission for getting QPS Time Series Project """

    def has_permission(self, request, view):

        try:
            if request.user.is_superuser:
                return True
            qpsts = QpsTimeseriesProject.objects.get(project__name=view.kwargs['project_name'])

            return request.user.has_perm('qdjango.view_project', qpsts.project)

        except Exception as e:
            logger.debug(f'[QPS_TIMESERIES] - Get Project: {e}')
            return False


class GetUserPermission(BasePermission):
    """ Check permission for getting User data """

    def has_permission(self, request, view):
        try:
            if request.user.is_superuser:
                return True
            else:
                return request.user.username == view.kwargs['username']

        except Exception as e:
            logger.debug(f'Get User: {e}')
            return False


class GetCreateGroupPermission(BasePermission):
    """ Check permission for getting or creating Group """

    def has_permission(self, request, view):
        try:
            return request.user.is_superuser

        except Exception as e:
            logger.debug(f'Get User: {e}')
            return False



class UpdateProjectPermission(BaseSuperuserPermission):
    """ Check permission for updating Project """
    pass
