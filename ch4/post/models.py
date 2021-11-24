from django.db import models

# Create your models here.


# class Profile(models.Model):
#     name = models.CharField(max_length=100)
#     gender = models.CharField(choices="male" "female")


class Post(models.Model):
    life = '일상'
    yum = '냠냠'
    etc = '기타'
    
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=[
                                (life, "일상"), (yum, "냠냠"), (etc, "기타")], default=life)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    # Catergory_IN_POST = []

    def __str__(self):
        return self.content
