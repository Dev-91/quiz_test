# quiz 폴더에 있는 urls.py와 myapi 폴더에 있는 urls.py는 다른 역할
# quiz 폴더에 있는 urls.py는 quiz app에 대한 url을 관리하고
# myapi 폴더에 있는 urls.py는 전체 프로젝트의 대한 url을 관리함

# 따라서 quiz 폴더의 url을 먼저 설정하고 이것을 myapi의 url에 연결시킴

from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
]