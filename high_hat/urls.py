from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import challenge.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', challenge.views.home, name="home"),
    path('challenges/', challenge.views.challenges, name="challenges"),
    path('samples/', challenge.views.samples, name="samples"),
    path('samples/sample/<int:sample_id>', challenge.views.sample, name="sample"),
    path('login/', challenge.views.login, name="login"),
    path('signup/', challenge.views.signup, name="signup"),
    path('logout/', challenge.views.logout, name="logout"),
    path('dashboard/', challenge.views.dashboard, name="dashboard"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)