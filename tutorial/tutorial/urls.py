from django.urls import path, include

urlpatterns = [
  path('', include('snippets.urls')),
  path('auth/', include('rest_framework.urls')),
]
