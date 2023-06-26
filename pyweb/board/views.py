from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from board.models import Question, Answer
from board.forms import QuestionForm, AnswerForm
from django.utils import timezone

def index(request):
    return render(request, 'board/index.html')
    #return HttpResponse("<h1>웹 메인페이지 입니다.</h1>")

# 질문 목록
def question_list(request):
    # question_list = Question.objects.all()
    question_list = Question.objects.order_by('-create_date') # 내림차순 - 필드앞에 -를 붙이면 내림차순
    # 페이지 처리
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)    # 페이지당 게시글 - 10개 설정
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj} # context = {'question_list': question_list} 에서 수정됨
    return  render(request, 'board/question_list.html', context)

def detial(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'board/detail.html', context)

# 질문 등록
@login_required(login_url='common:login')   # 로그인 페이지 이동
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)   # 겟파라미터 입력된 데이터가 있는 폼
        if form.is_valid(): # 얘가 유효하다면 에러가 없다면(유효성 검사를 통과했다면)
            question = form.save(commit=False)      # 가저장 - 여기로 내려가서 저장합니다.(진짜 저장은 아니고 가짜저장 임시저장입니다. create를 명시를 해줘야)
            question.author = request.user          # 세션 권한(로그인한) 있는 글쓴이
            question.create_date = timezone.now()   # 등록일 생성
            form.save()                             # 실제 저장진짜 저장
            return redirect('board:question_list')  # 질문 목록 페이지 이동
    else:
        form = QuestionForm()   # 폼 객체를 생성(비어있는 폼) - else가 get 입니다.
    context = {'form': form}
    return render(request, 'board/question_form.html', context)  # get 방식

# 답변 등록
@login_required(login_url='common:login')   # 로그인 페이지 이동
def answer_create(request, question_id):
    # 질문이 1개 있어야 답변을 등록할 수 있음
    # 일단 질문을 가져와야겠죠
    # question = Question.objects.get(id=question_id)     # 하나 가져온게 question이다
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":                        # POST를 소문자로 표시하면 에러발생
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)        # content만 저장
            answer.author = request.user            # 세션에 로그인한 사람
            answer.create_date = timezone.now()     # 답변 등록일
            answer.question = question              # 외래키 생성
            form.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm() # 빈 폼을 생성해줘야 합니다.   # forms에서 만들어주러 가겠습니다.
    context = {'question': question, 'form': form}
    return render(request, 'board/detail.html', context)

# 질문 수정
@login_required(login_url='common:login')
def question_modify(request, question_id):
    # 수정을 위해서 질문 1개 가져옴
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":                                # 메서드가 post면
        form = QuestionForm(request.POST, instance=question)    #
        if form.is_valid():             # 폼에 유효성이 제대로 됐다면
            form.save(commit=False)     # 커밋이 안된 상태로 객체를 하나 만들어요
            question.modify_date = timezone.now()   # 수정일
            question.author = request.user          # 작성일
            question.save()
            return redirect('board:detail', question_id=question_id)   # 수정되면 가는 경로 - 받아온 주소로 돌아가죠
    else:
        form = QuestionForm(instance=question) #포스트 바 # 데이터가 이미 있는 폼
    context = {'form': form}
    return render(request, 'board/question_form.html', context)


# 질문 삭제
@login_required(login_url='common:login')
def question_delete(request, question_id):
    # question = Question.objects.get(id=question_id)
    # 모델에서 데이터가 있으면 가져오고 없으면 404 페이지 오류 오류 처리를 함
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('board:question_list')

# 답변 삭제
@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('board:detail', question_id=answer.question.id)