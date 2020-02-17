from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    """ 文章
    title: 标题
    excerpt： 摘要
    cover： 封面
    content： 内容
    author： 作者
    date_posted： 发表时间
    """
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=500, blank=True)
    cover = models.ImageField(upload_to='media/blog/%Y/%m/%d', blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})


    class Meata:
        ordering = ['-date_posted']