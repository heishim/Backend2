from django.urls import path
from . views import FichierView, FichierViewSet, donnee, sortie, delete
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('fichiers', FichierViewSet)
#urlpatterns = router.urls

urlpatterns = [
    path('donnee/', donnee),
    path('sortie/', sortie),
    path('clean/', delete),
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
]

urlpatterns += router.urls

