from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField







# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=255,verbose_name="标题")
    category=models.ForeignKey("Category",on_delete=models.CASCADE,)
    # content=models.TextField(max_length=10000)
    content = RichTextUploadingField(null=True, blank=True)
    author=models.ForeignKey("UserProfile",verbose_name="作者",on_delete=models.CASCADE,)
    posttime=models.DateTimeField(auto_now=True,verbose_name="时间")
    hidden=models.BooleanField(default=False)
    head_img=models.ImageField(upload_to="uploads",null=True,blank=True)
    prioritty=models.IntegerField(default=1000,verbose_name="优先级")

    def __str__(self):
        return "{},{}".format(self.title,self.author)

class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,)
    author=models.ForeignKey("UserProfile",on_delete=models.CASCADE,)
    # parent_comment=models.ForeignKey("self",related_name="parent",blank=True,null=True)
    comment=models.TextField(max_length=2000)
    posttime = models.DateTimeField(auto_now=True, verbose_name="时间")
    def __str__(self):
        return  "user{},comment:{}".format(self.author,self.comment)

class Category(models.Model):
    name=models.CharField(max_length=80,unique=True)
    admin=models.ManyToManyField("UserProfile")
    def __str__(self):
        return  "{}".format(self.name)
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,)
    name=models.CharField(max_length=32)
    groups=models.ManyToManyField("UserGroup")
    def __str__(self):
        return  "{}".format(self.name)
class UserGroup(models.Model):
    name=models.CharField(max_length=64,unique=True)
    def __str__(self):
        return "{}".format(self.name)