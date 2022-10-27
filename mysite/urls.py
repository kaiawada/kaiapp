from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include

from . import setting_common, setting_dev

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),
    path('accounts/', include('allauth.urls')),
]

#開発サーバーでメディアを配信できるようにする設定
urlpatterns += static(setting_common.MEDIA_URL, document_root = setting_dev.MEDIA_ROOT)
