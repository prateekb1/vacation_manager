from django.urls import path
from vacation.views import VacationList, VacationDetail, VacationSearch


urlpatterns = [
    path('vacation/', VacationList.as_view()),
    path('vacation/<int:pk>/', VacationDetail.as_view()),
    path('vacation/search/', VacationSearch.as_view()),
]
