from django.contrib import admin
from django.urls import path
from api.views import SendMail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendmail/', SendMail.as_view(),name='send_mail'),

]
