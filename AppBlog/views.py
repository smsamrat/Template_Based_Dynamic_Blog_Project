
import uuid
from django.shortcuts import get_object_or_404, redirect, render,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from . models import Blog,Commnet,Likes
from . forms import CommentForm

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

def blog_details(request,slug):
    # blog = get_object_or_404(slug=given url string) # it function use when '<slug:string>/'
    blog = Blog.objects.get(slug=slug)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_obj = form.save(commit=False)
            comment_obj.user = request.user
            comment_obj.blog = blog
            comment_obj.save()
            return HttpResponseRedirect(reverse('blog_details', kwargs={'slug':slug}))

    return render(request,'app_blog/blog_details.html',context={'blog':blog,'form':form})



