from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import MyView, MyFileView

urlpatterns = [
    path('my-view1/', login_required(MyView.as_view())),
    path('api/myfiles/', MyFileView.as_view(), name='myfiles'),
]
