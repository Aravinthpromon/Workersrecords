from django.urls import path
from .views import WorkerList, WorkerDetail

urlpatterns = [
    path('', WorkerList.as_view(), name='worker-list'),
    path('<int:pk>', WorkerDetail.as_view(), name='worker-detail'),
]
