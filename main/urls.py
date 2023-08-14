from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('mail-checker-form', submit_mail, name="mail_submit"),
    path('profile-pic/<str:timestamp>', serve_developer_profile_pic, name="serve_developer_profile_pic"),
]