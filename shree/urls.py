from django.urls import path

from . import views

from shree.models import User
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
users = routers.DefaultRouter()
users.register(r'', UserViewSet)



urlpatterns = [
    
    # path('users/', include(users.urls)),
    path('getRoutes/', views.getRoutes),
    path('getUsers/<str:username>/', views.getUser),
    path('getUsers/', views.getUsers),
    path('createUser/', views.createUser),


    path('users/<str:username>/', views.user, name='user'),
    path('users/', views.users),
    path('<str:username>/profile/', views.profile),
    path('signOut/', views.signOut),
    path('signIn/', views.signIn),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about),
    path('home/', views.home, name = 'home'),
    path('employeer1/<str:username>/', views.rate1),
    path('employeer2/<str:username>/', views.rate2),
    path('employeer3/<str:username>/', views.rate3),
    path('employeer4/<str:username>/', views.rate4),
    path('employeer5/<str:username>/', views.rate5),
    path('leaves/', views.leaves, name='leaves'),
    path('hod_verify/<int:request_id>/', views.hod_verify),
    path('ceo_verify/<int:request_id>/', views.ceo_verify),
    path('<str:username>/leave/', views.leave, name='leave'),
    path('hod_rejection/<int:request_id>/', views.hod_rejection),
    path('ceo_rejection/<int:request_id>/', views.ceo_rejection),
]