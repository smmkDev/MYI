from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import (render, get_object_or_404, redirect)
from django.views.generic import (View, DetailView, CreateView, ListView)
from django.contrib.auth.models import User
import requests
import datetime

from .models import (Post, Group, Answer)
from user.models import (Alumni, Student)
from .forms import (PostForm, GroupForm, AnswerForm)

# Create your views here.

class AddPostView(View):

    def get(self, request, *args, **kwargs):

        form = PostForm(request.POST or None)
        return render(request, 'groups/post_add.html', {'form':form})
    

    def post(self, request, *args, **kwargs):

        form = PostForm(request.POST or None)
        self.form_valid(form, request)
        form = PostForm()
        return render(request, 'groups/post_add.html', {'form':form})
    

    def form_valid(self, form, request):      
           
        if form.is_valid():
            text = form.cleaned_data['text']
            img = request.FILES.get('image')
            vid = request.FILES.get('video')
            print(request.FILES)
            user = get_object_or_404(Student, user=self.request.user)
            if user:
                post = Post(text=text, post_std=user)
            else:
                user = get_object_or_404(Alumni, user=self.request.user)
                post = Post(text=text, post_alm=user)  
            if img != None:
                post.image.save(img.name, img, save=True)
            if vid != None:  
                post.video.save(vid.name, vid, save=True)
            post.save()
            group = self.get_object()
            group.posts.add(post)
            return redirect(f"/group/detail/{self.kwargs.get('pk')}")
        return False   


    def get_object(self):

        pk = self.kwargs.get('pk')
        group = get_object_or_404(Group, pk=pk)
        return group
    

class PostDetailView(DetailView):

    template_name = 'groups/post_ans.html'
    queryset = Post.objects.all()

    def get_object(self):

        pk = self.kwargs.get('pk')
        response = requests.get(f'http://127.0.0.1:8000/api/post/detail/{pk}')
        return response.json()  


class AddAnswerView(View):

    def get(self, request, *args, **kwargs):

        form = AnswerForm(request.POST or None)
        return render(request, 'groups/ans_add.html', {'form':form})
    

    def post(self, request, *args, **kwargs):
        
        form = AnswerForm(request.POST or None)
        self.form_valid(form, self.request)
        return render(request, 'groups/ans_add.html', {'form':form})


    def form_valid(self, form, request):

        if form.is_valid():

            text = form.cleaned_data['text']
            img = request.FILES.get('image')
            vid = request.FILES.get('video')
            user = self.request.user
            user = get_object_or_404(Student, user=user)
            if  user:
                ans = Answer(student=user, text=text)
            else:
                user = get_object_or_404(Alumni, user=user)
                ans = Answer(student=user, text=text)
            if img != None:
                ans.image.save(img.name, img, save=True)
            if vid != None:
                ans.video.save(vid.name, vid, save=True)
            ans.save()
            obj = self.get_object()
            obj.answers.add(ans)
            obj.save()


    def get_object(self):

        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Post, pk=pk)
        return obj        



class GroupDetailView(DetailView) :

    queryset = Group.objects.all()
    template_name = "groups/group_dt.html"


    def get_object(self):
        
        pk = self.kwargs.get('pk')
        response  = requests.get(f'http://127.0.0.1:8000/api/group/detail/{pk}').json()
        response['pk'] = pk
        response['is_alumni'], response['request_user'] = self.get_userid(self.request)
        response = self.get_group_images(pk, response)
        return response
    
    
    def format_response(self, response):

        alumnis = response['alumnis']
        students = response['students']
        obj = response  
        obj['alumni_image'] = []
        obj['student_image'] = []
        for alumni in alumnis:
           user  = get_object_or_404(User, username=alumni['user']['username'])
           user = get_object_or_404(Alumni, user=user)
           obj['alumni_image'].append(user.profile_image.url)
        for student in students:
            user  = get_object_or_404(User, username=student['user']['username'])
            user = get_object_or_404(Student, user=user)
            obj['student_image'].append(user.profile_image.url) 
        return obj    
    

    def get_userid(self, request):

        user = request.user
        if user.is_authenticated:
            obj =  get_object_or_404(Student, user=user).pk
            if obj:

                return 0, obj
            else:
                
                return 1, get_object_or_404(Alumni, user=user).pk
        else:

            return 0, redirect("/user/login")    
        

    def get_group_images(self, pk, response):    

        obj = get_object_or_404(Group, pk=pk)
        response['banner'] = obj.banner
        response['image'] = obj.image
        return response
    

class GroupCreateView(CreateView):

    queryset = Group.objects.all()
    form_class = GroupForm
    template_name = 'groups/group_cr.html'
    success_url = "/group" 

    def form_valid(self, form):

        print(form.is_valid())
        if form.is_valid():

           name = form.cleaned_data['name']
           field = form.cleaned_data['field'] 
           des = form.cleaned_data['des']
           date = datetime.date.today()
           data = {
               'pk': self.request.user.pk,
               'name': name,
               'field': field,
               'des': des,
               'date': date
           }
           response  = requests.post('http://127.0.0.1:8000/api/group',
                                    data=data)
           print(self.request.FILES)
           self.save_files(self.request) 
        return redirect(self.success_url)


    def save_files(self, request):

        obj = Group.objects.last()
        print(request.FILES)
        banner = request.FILES.get('banner')
        img = request.FILES.get('image')
        if banner != None:
           obj.banner.save(banner.name, banner, save=True) 
        if img != None:   
           obj.image.save(img.name, img, save=True) 
        obj.save() 
 

class GroupListView(ListView):

    queryset = Group.objects.all()
    template_name = "groups/all_groups.html"

    def get_queryset(self):

        response  = requests.get('http://www.myi.syedengineering.com.pk/api/group/list/',  headers={'User-Agent': 'Custom'})
        print(response.status_code)
        return response.json()

     

class JoinGroupView(View):

    
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        user = request.user
        group = get_object_or_404(Group, pk=pk)
        is_alumni, user = self.get_user(user)
        if is_alumni:
           
           group.alumnis.add(user)
        else:

            group.students.add(user)
        return redirect("/group/list")    



    
    def get_user(self, user):

        obj = get_object_or_404(Alumni, user=user)
        if obj:

            return 1, obj
        obj = get_object_or_404(Student, user=user)
        return 0, obj
    



