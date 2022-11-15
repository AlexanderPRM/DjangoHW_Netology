from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.views import Response
from .models import Sensor
from .serializers import SensorDetailSerializer, MeasurementSerializer
from rest_framework import status


class SensorsView(ListCreateAPIView):
    def get(self, request):
        queryset = Sensor.objects.all()
        sensors = SensorDetailSerializer(queryset, many=True)
        return Response(sensors.data)

    def post(self, request):
        serializer = SensorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_201_CREATED})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST})


class RetvieweSensorView(RetrieveUpdateAPIView):
    def get(self, request, pk):
        sensor_get = Sensor.objects.get(id=pk)
        sensor_serializer = SensorDetailSerializer(sensor_get, many=False)
        return Response(sensor_serializer.data)

    def patch(self, request, pk):
        sensor_get = Sensor.objects.get(id=pk)
        sensor_serializer = SensorDetailSerializer(
                                                sensor_get,
                                                data=request.data,
                                                partial=True)
        if sensor_serializer.is_valid():
            sensor_serializer.save()
            return Response({'status': status.HTTP_201_CREATED})


class CreateMeasurement(CreateAPIView):
    def post(self, request):
        measurement_create = MeasurementSerializer(data=request.data)
        if measurement_create.is_valid():
            measurement_create.save()
            return Response({'status': status.HTTP_201_CREATED})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST})
