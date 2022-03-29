
import uuid
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from . models import Blog,Commnet,Likes

# Create your views here.
class CreateBlogs(CreateView):
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

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'app_blog/index.html'

# def index(request):
#     return render(request,'app_blog/index.html',)
