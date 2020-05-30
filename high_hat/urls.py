from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import challenge.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', challenge.views.home, name="home"),
    path('challenges/', challenge.views.challenges, name="challenges"),
    path('samples/', challenge.views.samples, name="samples"),
    path('login/', challenge.views.login, name="login"),
    path('signup/', challenge.views.signup, name="signup"),
    path('logout/', challenge.views.logout, name="logout"),
    path('dashboard/', challenge.views.dashboard, name="dashboard"),
]
