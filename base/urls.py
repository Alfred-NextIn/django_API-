from django.urls import path
from . import views
#this import is for simpleJWT token generation
from rest_framework_simplejwt.views import(
    TokenObtainPairView
)
urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocates_list, name ='advocates'),
    # path('advocates/<str:username>/', views.advocate_details)
    path('advocates/<str:username>/', views.AdvocateDetails.as_view()),

    path('companies/', views.company_list, name ='companies'),
    # path('companies/<str:name>/', views.company_details, name = 'company_details')

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]