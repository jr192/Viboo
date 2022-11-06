from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from api.serializers.buildings import BuildingsSerializer


class BuildingsViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = BuildingsSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({"response": "Record saved!"})
