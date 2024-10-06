from django.contrib import admin
from django.urls import path
#from .views import AsteroidFeedView
from .views import PlanetDataView
from .views import CometDataView
from .views import MoonDataView
from .views import AsteroidDataView
from .views import Hazards

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('earth/<int:days_since_epoch>/', AsteroidFeedView.as_view(), name='asteroid-feed'),  # Updated URL pattern
    path('planets/', PlanetDataView.as_view(), name='planets'),
    path('comets/', CometDataView.as_view(), name='comets'),
    path('moons/', MoonDataView.as_view(), name='moons'),
    path('asteroids/', AsteroidDataView.as_view(), name='asteroids'),
    path('hazards/', Hazards.as_view(), name='hazards'),
]
