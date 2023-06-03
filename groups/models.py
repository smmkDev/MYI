from django.db import models
from django.urls import reverse
from user.models import (Alumni, Student)
from django.contrib.auth.models import User

# Create your models here.

class Stats(models.Model):

    upvotes = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)


class Answer(models.Model):

    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE,
                             related_name="ans_std")
    alumni = models.ForeignKey(Alumni, null=True, on_delete=models.CASCADE,
                             related_name="ans_alm")
    text = models.CharField(max_length=300)
    image = models.ImageField(upload_to="answers/images", null=True)
    video = models.FileField(upload_to="answers/videos", null=True)


class Post(models.Model):

    post_std = models.ForeignKey(Student, null=True, on_delete=models.CASCADE,
                             related_name="post_std")
    post_alm = models.ForeignKey(Alumni, null=True, on_delete=models.CASCADE,
                             related_name="post_alm")
    text = models.TextField(max_length=200)
    image = models.ImageField(upload_to='posts/images', null=True)
    video = models.FileField(upload_to='posts/videos', null=True)
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    answers = models.ManyToManyField(Answer)


    # def get_ans_url(self):

    #     return reverse("add_ans", kwargs={'pk':self.pk})
    

    def update_stats(self):

        self.upvote += 1
        self.save()


class Group(models.Model):

    admin = models.ForeignKey(User, null=True, on_delete=models.CASCADE, 
                              related_name="group_admin")
    banner = models.ImageField(upload_to="group_images/banners", null=True)
    image = models.ImageField(upload_to="group_images/main_images", null=True)
    name = models.CharField(max_length=50, default="Your Group")
    field = models.CharField(max_length=50, default="Electrical")
    des = models.CharField(max_length=150, default="None")
    posts = models.ManyToManyField(Post)
    date = models.DateField(null=True)
    alumnis = models.ManyToManyField(Alumni)
    students = models.ManyToManyField(Student)

    # def get_post_url(self):

    #     return reverse("add_post", kwargs={'pk':self.pk})

        
    
    

