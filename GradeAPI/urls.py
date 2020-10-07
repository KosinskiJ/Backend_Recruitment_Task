from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register('add-mark', views.AddMarkView)
router.register('candidates-list', views.CandidateListView)


urlpatterns = [

    path('api/', include(router.urls))

]