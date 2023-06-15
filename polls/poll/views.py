from django.http import HttpResponse
from django.shortcuts import render


def index(request):    # 괄호안에 request 써놔요 # return이 있는 함수 # view가 controller라고했죠
    cart = "콩나물"     # 모델(데이터) - 딕셔너리형으로 보냄
    cartlist = ["계란", "콩나물", "생수", "커피"]
    context = {'cart' : cart, 'cartlist': cartlist}
    return render(request, 'poll/index.html', context)   # 경로 잡음. # {'cart' : cart} # index.html {{ }} - 출력 | {% %} - 명령문
    # return HttpResponse("<h1>안녕~ poll!</h1>") # HttpResponse import 해줬음 # 웹 주소란에 http://127.0.0.1:8000/poll/ 입력하면 브라우저에 나타남

def test(request):
    cart = "콩나물"  # 모델(데이터) - 딕셔너리형으로 보냄
    cartlist = ["계란", "콩나물", "생수", "커피"]
    context = {'cart': cart, 'cartlist': cartlist}
    return render(request, 'poll/test.html', context) # context 9번라인에서

