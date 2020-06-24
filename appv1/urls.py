from rest_framework import routers
from .views import TrpgSessionSet ,SessionUserSet,DiceRollSet,DiceLogSet
from django.conf import settings
from django.urls import path, include
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'session', TrpgSessionSet)
router.register(r'user', SessionUserSet)
router.register(r'uEntry', SessionUserSet)
router.register(r'uDiceLog', DiceLogSet)
router.register(r'uDiceRoll', DiceRollSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns