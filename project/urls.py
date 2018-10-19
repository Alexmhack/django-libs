from django.contrib import admin
from django.urls import path, include

from .views import dashboard_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
]

# django-jet urls
urlpatterns += [
    path('jet/', include('jet.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', namespace='jet-dashboard')),
]

# django-allauth urls
urlpatterns += [
    path('accounts/', include('allauth.urls')),
]

# django-hijack urls
urlpatterns += [
    path('hijack/', include('hijack.urls', namespace='hijack')),
]
