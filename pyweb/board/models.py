from django.contrib.auth.models import User
from django.db import models

# model만들기 - Question(subject, content, create_date), Answer
class Question(models.Model):   #상속받고
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 글쓴이 # 삭제 안되게도 할 수있어요 - 카테고리 없어도 삭제되면 안되는건 casecade 아니고 sellnull?
    subject = models.CharField(max_length=200)  # 제목
    content = models.TextField()                # 질문 내용
    create_date = models.DateTimeField()        # 동록일

    def __str__(self):
        return self.subject

# 답변 모델(테이블)
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 글쓴이
    content = models.TextField()            # 답변 내용
    create_date = models.DateTimeField()    # 등록일
    question = models.ForeignKey(Question,
                on_delete=models.CASCADE)    # 외래키 # Question에서 참조했다

    def __str__(self):
        return self.content