
from rest_framework import generics
from vacation.models import Vacation
from vacation.serializers import VacationSerializer


class VacationList(generics.ListCreateAPIView):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer


class VacationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer


class VacationSearch(generics.ListAPIView):
    serializer_class = VacationSerializer

    def get_queryset(self):
        queryset = Vacation.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset
