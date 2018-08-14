
from django.urls import path,include
from django.contrib.auth import views as auth_views
from myapp import views
app_name='myapp'
urlpatterns = [
    path('login/',views.Login.as_view(),name='login'),
    path('signup/', views.signup.as_view(), name='signup'),
    path('logout/',views.Logout,name='logout'),
    path('searchbuses/',views.SearchBuses.as_view(), name='searchbuses'),
    path('buses/', views.DisplayBuses.as_view(), name='display'),
    path('buses/<int:id>/',views.BusSeats.as_view(),name='busseats'),
    path('buses/<int:id>/seats/', views.TicketDetails.as_view(), name='seats'),
    path('mybookings/',views.ViewBookings.as_view(),name='history'),
    path('sendticket/<int:ticketid>',views.SendMail.as_view(),name='sendmail'),
    path('cancelticket/<int:ticketid>',views.CancelTicket.as_view(),name='cancelTicket'),
    path('myticket/<int:ticketid>',views.ViewTicket.as_view(),name='ticket'),
]
