from django.contrib import admin

from board.models import Question, Answer

# 관리자 페이지에 질문 모델 등록
admin.site.register(Question)   # 질문 모델 등록
admin.site.register(Answer)     # 답변 모델 등록
