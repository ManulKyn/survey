from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('survey.urls')),
]