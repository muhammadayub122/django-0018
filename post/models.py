from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
    title=models.CharField(max_length=225,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='post/',blank=True,null=True)
    wiews_count=models.PositiveIntegerField(default=0)
    total_comment=models.PositiveIntegerField(default=0)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def str(self):
        return f'{self.title}|{self.user.first_name}'
    

class PostView(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='views')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
 
    created_at=models.DateField(auto_now_add=True)

    def str(self):
        return f'{self.post}'
    def save(self,*args,**kwargs):
        self.post.views_count+=1
        self.post.save()
        super().save(*args,**kwargs)
class PostComment(models.Model):
        post=models.OneToOneField(Post,on_delete=models.CASCADE,related_name='comments')
        user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
        reply_comment=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
        created_at=models.DateField(auto_now_add=True)
        comment=models.TextField()
    