import logging

from rest_framework import response, views, permissions, status

logger = logging.getLogger("api_views")


class HomeView(views.APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):

        logger.info("再测试一下TESTADD")

        return response.Response(status=status.HTTP_200_OK)
