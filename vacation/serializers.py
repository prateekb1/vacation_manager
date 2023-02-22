from rest_framework import serializers
from vacation.models import Vacation
from django.core.exceptions import ValidationError


class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ('id', 'name', 'start_date', 'end_date')
        
    def validate(self, value):
        start = value.get('start_date')
        end = value.get('end_date')
        if start > end:
            print(start)
            print(end)
            raise ValidationError("Start date cannot be after end date.")
        else:
            return value