from django.urls import path
from .views import SiteList, SiteDetails, SummarySum, SummaryAverage


urlpatterns = [
    path('', SiteList.as_view()),
    #path('sites/', SiteList.as_view()),
    path('sites/<int:site>/', SiteDetails.as_view()),
    path('summary/', SummarySum.as_view()),
    path('summary-average/', SummaryAverage.as_view())
]