from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)    # 제목
    content = models.TextField()                # 내용
    pub_date = models.DateTimeField()           # 발행일
    modify_date = models.DateTimeField(null=True, blank=True) # 입력 폼이 버어도 됨
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                    null=True, blank=True)    # null 허용, 파일을 첨부하지 않을수 있음
    

    def __str__(self):  # 안넣으면 한글이 안될수도있다고함
        return self.title

