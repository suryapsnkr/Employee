from django.urls import path

from shree import views

from shree.models import Employee
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'Employeename', 'email', 'is_staff']

# ViewSets define the view behavior.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Routers provide an easy way of automatically determining the URL conf.
Employees = routers.DefaultRouter()
Employees.register(r'', EmployeeViewSet)



urlpatterns = [
    
    # path('Employees/', include(Employees.urls)),
    # path('getRoutes/', views.getRoutes),
    # path('getEmployees/<str:eid>/', views.getEmployee),
    # path('getEmployees/', views.getEmployees),
    # path('createEmployee/', views.createEmployee),


    path('employees/<int:eid>/', views.employee, name='employee'),
    path('employees/', views.employees, name= 'employees'),
    path('signOut/', views.signOut),
    path('signIn/', views.signIn),
    path('signUp/', views.signUp),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about),
    path('home/', views.home, name = 'home'),
    path('tempr1/<str:eid>/', views.rate1),
    path('tempr2/<str:eid>/', views.rate2),
    path('tempr3/<str:eid>/', views.rate3),
    path('tempr4/<str:eid>/', views.rate4),
    path('tempr5/<str:eid>/', views.rate5),
    path('leaves/', views.leaves, name='leaves'),
    path('hod_verify/<int:rid>/', views.hod_verify),
    path('ceo_verify/<int:rid>/', views.ceo_verify),
    path('<str:eid>/leave/', views.leave, name='leave'),
    path('hod_rejection/<int:rid>/', views.hod_rejection),
    path('ceo_rejection/<int:rid>/', views.ceo_rejection),
]