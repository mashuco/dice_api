from rest_framework import routers
from .views import TrpgSessionSet ,SessionUserSet,DiceRollSet,DiceLogSet
from django.conf import settings
from django.urls import path, include
from django.conf.urls import url
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'session', TrpgSessionSet)
router.register(r'user', SessionUserSet)
router.register(r'uEntry', SessionUserSet)
router.register(r'uDiceLog', DiceLogSet)
router.register(r'uDiceRoll', DiceRollSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns