from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

import AccountApp.urls
import AdminApp.urls
import StaffApp.urls
import UserApp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(AccountApp.urls)),
    path('admin_app/', include(AdminApp.urls)),
    path('staff_app/', include(StaffApp.urls)),
    path('user_app/', include(UserApp.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

