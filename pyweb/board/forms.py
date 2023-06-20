from django import forms
from board.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:     # 중첩 클래스라고 그랬죠
        model = Question
        fields = ['subject', 'content']
        labels = {      # labels에서 아래처럼 표시하니 한글로 수정이 가능했음
            'subject': '제목',
            'content': '내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:     # 중첩 클래스라고 그랬죠
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변 내용'
        }