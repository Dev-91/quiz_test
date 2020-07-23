from rest_framework import serializers
from .models import Quiz

class QuizSerializser(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')
# """Quiz 모델 데이터가 주어지면 title, body, answer를 포함한 JSON데이터로 변환해주는 시리얼 라이저"""