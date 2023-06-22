from django.shortcuts import render, redirect
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post


def index(request):
    return render(request, 'blog/index.html')   # 이걸 만드려면 템플릿 폴더가 필요합니다.

def post_list(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'blog/post_list.html', context)

# 상세 페이지
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}    # post로 다 받을 수 있게 해줘야지 오류가 안나죠
    return render(request, 'blog/detail.html', context)

# 글쓰기 폼 -
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)    # (일반 속성, 파일)
        if form.is_valid(): # 유효성 검사를 통과했다면(유효하다면~)
            post = form.save(commit=False)
            post.pub_date = timezone.now()  # 현재 시간
            post.save()
            return redirect('blog:post_list')   # 블로그 목록으로 경로 설정 ':' 사용
    else:
        form = PostForm()   # 비어있는 폼
    context = {'form': form}
    return render(request, 'blog/post_form.html', context)