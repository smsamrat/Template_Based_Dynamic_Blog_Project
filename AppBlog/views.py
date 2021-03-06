
from dataclasses import field
import uuid
from django.shortcuts import get_object_or_404, redirect, render,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView,TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Blog,Commnet,Likes
from . forms import CommentForm
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
class CreateBlogs(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'app_blog/create_blog.html'
    fields=('blog_title','blog_content','blog_image')
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user    
        title = obj.blog_title
        obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        obj.save()
        return redirect('index')
class MyBlogView(TemplateView):
    context_object_name = 'blogs'
    model= Blog
    template_name = template_name = 'app_blog/myblog.html'

class EditBlog(LoginRequiredMixin,UpdateView):
    model = Blog
    fields=('blog_title','blog_content','blog_image')
    template_name = template_name = 'app_blog/edit_blog.html'

    def get_success_url(self):
        return reverse_lazy('my_blog')

def BlogList(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 2,orphans = 1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_blog/index.html', { 'blogs': page_obj,'page_number':int(page_number),'paginator':paginator })

@login_required
def blog_details(request,slug):
    # blog = get_object_or_404(slug=given url string) # it function use when '<slug:string>/'
    blog = Blog.objects.get(slug=slug)
    form = CommentForm()
    already_liked = Likes.objects.filter(blog=blog,user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_obj = form.save(commit=False)
            comment_obj.user = request.user
            comment_obj.blog = blog
            comment_obj.save()
            return HttpResponseRedirect(reverse('blog_details', kwargs={'slug':slug}))

    return render(request,'app_blog/blog_details.html',context={'blog':blog,'form':form,'liked':liked})

class MyBlog(LoginRequiredMixin,DetailView):
    pass

class UpdateComment(UpdateView):
    model = Commnet
    template_name = 'app_blog/update_comment.html'
    fields = ('comment_text',)

    def get_success_url(self,**kwargs):
        return reverse_lazy('blog_details', kwargs={'slug':self.object.blog.slug})

@login_required
def blog_liked(request,pk):
    blog = Blog.objects.get(pk=pk)
    already_liked = Likes.objects.filter(blog=blog,user=request.user)
    if not already_liked:
        liked = Likes(blog=blog,user=request.user)
        liked.save()
    return HttpResponseRedirect(reverse('blog_details', kwargs={'slug':blog.slug}))

@login_required
def blog_disliked(request,pk):
    blog = Blog.objects.get(pk=pk)
    already_liked = Likes.objects.filter(blog=blog,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('blog_details', kwargs={'slug':blog.slug}))



def loadmoreindex(request):
    post_obj = Blog.objects.all()[0:5]
    # post_values = Post.objects.values()[0:5]
    # print(post_values)
    total_obj = Blog.objects.count()
    print(total_obj)
    return render(request, 'app_blog/loadmore.html', context={'posts': post_obj, 'total_obj': total_obj})

def load_more(request):    
    offset = request.GET.get('offset')
    offset_int = int(offset)
    limit = 2
    # post_obj = Post.objects.all()[offset_int:offset_int+limit]
    post_obj = list(Blog.objects.values()[offset_int:offset_int+limit])
    data = {
        'posts': post_obj
    }
    return JsonResponse(data=data)