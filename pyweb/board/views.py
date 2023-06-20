from django.http import HttpResponse
from django.shortcuts import render, redirect
from board.models import Question
from board.forms import QuestionForm, AnswerForm
from django.utils import timezone

def index(request):
    return render(request, 'board/index.html')
    #return HttpResponse("<h1>웹 메인페이지 입니다.</h1>")

def question_list(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return  render(request, 'board/question_list.html', context)

def detial(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'board/detail.html', context)

# 질문 등록
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)   # 겟파라미터 입력된 데이터가 있는 폼
        if form.is_valid(): # 얘가 유효하다면 에러가 없다면(유효성 검사를 통과했다면)
            question = form.save(commit=False)      # 가저장 - 여기로 내려가서 저장합니다.(진짜 저장은 아니고 가짜저장 임시저장입니다. create를 명시를 해줘야)
            question.create_date = timezone.now()   # 등록일 생성
            form.save()                             # 실제 저장진짜 저장
            return redirect('board:question_list')  # 질문 목록 페이지 이동
    else:
        form = QuestionForm()   # 폼 객체를 생성(비어있는 폼) - else가 get 입니다.
    context = {'form': form}
    return render(request, 'board/question_form.html', context)  # get 방식

# 답변 등록
def answer_create(request, question_id):
    # 질문이 1개 있어야 답변을 등록할 수 있음
    # 일단 질문을 가져와야겠죠
    question = Question.objects.get(id=question_id)    # 하나 가져온게 question이다
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)        # content만 저장
            answer.create_date = timezone.now()     # 답변 등록일
            answer.question = question              # 외래키 생성
            form.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm() # 빈 폼을 생성해줘야 합니다.   # forms에서 만들어주러 가겠습니다.
    context = {'question': question, 'form': form}
    return  render(request, 'board/detail.html', context)