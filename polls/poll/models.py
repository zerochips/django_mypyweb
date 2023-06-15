from django.db import models

# 질문 테이블(모델)
class Question(models.Model):   # ()괄호안에 있으면 상속 받았다는 겁니다.
    # 필드
    question_text = models.CharField(max_length=200) # 200자까지
    pub_date = models.DateTimeField()                # 생성자니까 괄호가 있어야 합니다.

    def __str__(self):  #객체 정보를 문자열로 반환
        return self.question_text
    
# 전체 검색하는 명령어 : Question.objects.all()
# 하나 검색하는 명령어 : Question.objects.get(id=2)
# 수정하는 명령어(변수에 할당하는 방법) :

# 항목 테이블(엔티티)
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  #투표수
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
