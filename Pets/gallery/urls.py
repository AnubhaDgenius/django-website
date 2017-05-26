from django.conf.urls import url, include
from django.contrib import admin
from gallery import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter() 
router.register(r'notices', views.NoticeViewSet)
router.register(r'Owner', views.OwnerViewSet)
router.register(r'users', views.UserViewSet)



urlpatterns = [
    url(r'^about/', views.about),
    url(r'^contact/', views.contact),
    url(r'^Owner/edit/(?P<pk>\d+)$', views.OwnerUpdate.as_view(), name='Owner_edit'), 
    url(r'^DogBreedInfo/', views.DogBreedInfo),
    url(r'^DogBreedInfo2/', views.DogBreedInfo2),
    url(r'^DogBreedInfo3/', views.DogBreedInfo3),
    url(r'^$', views.NoticeList.as_view(), name='notice_list'),
    url(r'^(?P<pk>\d+)$', views.NoticeDetails.as_view(), name='notice_detail'),    

    url(r'^new_ques$', views.QuesCreate.as_view(), name='ques_new'),          
    
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),        
]