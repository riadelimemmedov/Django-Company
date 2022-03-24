from struct import pack
from django.urls import path
from .views import *

app_name = 'pform'

urlpatterns = [
    path('reports/<str:production_line>/',reportView,name='reportView'),
    path('reports/delete/<pk>/',deleteView,name='deleteView'),
    path('reports/<str:production_line>/<pk>/update/',ReportUpdatView.as_view(),name='reportUpdatView'),
    path('',HomeView.as_view(),name='homeView'),
    path('reports/',SelectView.as_view(),name='selectView'),
    path('reports/summary',main_report_summary,name='mainReportSummary'),
    # path('reports/generate/pdf/',get_generated_problems_in_pdf,name='pdf'),
]