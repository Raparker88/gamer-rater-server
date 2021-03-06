
from django.conf.urls import include
from django.urls import path
from raterapi.views import register_user, login_user, Games, Categories, Reviews
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', Games, 'game')
router.register(r'categories', Categories, 'category')
router.register(r'reviews', Reviews, 'review')

urlpatterns = [ 
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
