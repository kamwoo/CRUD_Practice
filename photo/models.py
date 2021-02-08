from django.db import models
from django.urls import reverse

# Create your models here.
from django.contrib.auth.models import User
# 장고의 기본 유저 모델

# 외래키(ForeignKey) : 어떤 테이블에서 주키가 다른 테이블에서 기록될때 외래키라고 한다.
                        # User 테이블에서 해당 유저를 찾을 수 있는 주키
# 주키(PrimaryKey) : User 테이블에 1 admin ~ ~ ~ ~

class Photo(models.Model): # models.Model에 장고의 orm기능이 다 들어가있다. 그래서 필드만 명시해도 기능이 된다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    # User 모델에 주키를 저장할 것이다. # 유저가 탈퇴하거나하면 사진같은 것들을 같이 없앤다.
    # query를 작성하지 않아도 유저 넘버에 해당하는 정보를 찾아올 수 있다.
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    # upload_to는 어디에 저장할 지  # default는 사진이 없을 때 어떻게 할 것이냐, 기본 설정값
    text = models.TextField()
    # 기본값이 없어도 들어간다.
    created = models.DateTimeField(auto_now_add=True)
    # auto_now_add는 데이터베이스의 row가 한번 새로 등록될 때 현재 시간을 자동으로 설정하겠다.
    updated = models.DateTimeField(auto_now=True)
    # auto_now는 등록되거나 수정될 때마다 새로 시간을 자동으로 설정하겠다.

    class Meta: # 옵션
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")
        # 작성자의 id

    def get_absolute_url(self): # 기능을 수행한 다음 전환될 화면
        return reverse('photo:photo_detail', args=[self.id])
