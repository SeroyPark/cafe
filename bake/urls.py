from django.urls import path
import bake
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path("bake/pan/", bake.views.pan, name='pan'),
    path("bake/ja/", bake.views.ja, name='ja'),
    path("bake/yong/", bake.views.yong, name='yong'),
    path("bake/jawrite/", bake.views.jawrite, name='jawrite'),
]