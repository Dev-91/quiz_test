#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializser

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response('Hello World!')

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuiz = random.sample(list(totalQuizs), id)
    serializer = QuizSerializser(randomQuiz, many=True)
    return Response(serializer.data)
