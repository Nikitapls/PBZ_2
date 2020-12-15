from django.urls import path
from worker.views import list_all_workers, detail

urlpatterns = [
    path('', list_all_workers),
    path('detail/<int:pk>',detail)
]
