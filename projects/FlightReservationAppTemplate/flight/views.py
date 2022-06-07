from .models import Flight, Reservation
from .serializers import FlightSerializer, ReservationSerializer, StuffFlightSerializer
from rest_framework import viewsets
from .permissions import IsStufforReadOnly
from datetime import datetime, date


# class SerializerByUserMixin:
#     def get_serializer_class(self, *args, **kwargs):
#         return self.serializer_map.get(str(self.request.user.is_staff), self.serializer_class)


# GET, POST, UPDATE, DELETE, PATCH
class FlightView(viewsets.ModelViewSet):  # SerializerByUserMixin,
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStufforReadOnly,)
    # serializer_map = {
    #     'True': StuffFlightSerializer,
    #     'False': FlightSerializer
    # }

    def get_serializer_class(self):
        serializer = super().get_serializer_class()   # --> FlightSerializer
        if self.request.user.is_staff:
            return StuffFlightSerializer
        return serializer

    def get_queryset(self):
        now = datetime.now()
        print(now)
        curren_time = now.strftime('%H:%M:%S')
        print(curren_time)
        today = date.today()
        print(today)
        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            queryset = Flight.objects.filter(date_of_departure__gt=today)
            print(queryset)
            if Flight.objects.filter(date_of_departure=today):
                today_qs = Flight.objects.filter(
                    date_of_departure=today).filter(etd__gt=curren_time)
                print(today_qs)
                queryset = queryset.union(today_qs)
            return queryset


class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)
