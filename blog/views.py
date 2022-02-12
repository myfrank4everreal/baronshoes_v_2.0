
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Blog, Post, Comment, Author
from django.db.models import Q
from django.db.models import Count
from account.models import SignUp
from .forms import CommentForm, PostForm
from django.contrib.auth.models import User



from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def search_blog(request):
    
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(Q(headline__icontains=query)|Q(bodytext__icontains=query)).distinct()
    
        context = {
            'queryset':queryset,
        }
        return render(request, 'blog/search_result.html', context)
    else:
        pass
# here i want to get the author for the post 
def get_author(user):
    author = Author.objects.filter(user=user)
    if author.exists:
        for i in author:
            if len(i) >= 1 :
                return author[0]
        
    else:
        return None
        
    
        
    
def get_category():
    # queryset = Post.objects.all()
    category = Post.objects.values('category__name').annotate(Count('category__name')) 
    
    return category
    
def blogview(request):
    title = 'blogview'
    category_count = get_category()
    featuredpost = Post.objects.filter(featured=True)
    
    print(category_count)
    title = 'Featured Blogs'
    bloglist = Blog.objects.all()
    recentpost = Post.objects.order_by('-pub_date')[:8]
    
    
   
    # for the newsletter subscription 
    context={
        'title':title,
        'bloglist':bloglist, 
        'featuredpost':featuredpost,
        'recentpost':recentpost,
        
        }
    return render(request, 'blog/blogview.html', context)


# def get_user():
#     user = User.objects.filter(user=user)

    

def post_detail(request, id=id):
    featuredpost = Post.objects.filter(featured=True)
    category_count = get_category()
    
    post = get_object_or_404(Post, id=id)
    
 
    comment_count = post.comment_set.count()
    
    # for the post comment form 
    commentform = CommentForm()
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            commentform.instance.user = request.user
            commentform.instance.post = post
            commentform.save()
    print(category_count)        
    context = {
        'comment_count':comment_count,
        'post':post,
        'commentform':commentform,
        'category_count':category_count,
        'featuredpost':featuredpost,
               }
    return render(request, 'blog/post_detail.html', context)

def blog_post(request, id):
    featuredpost = Post.objects.filter(featured=True)
    category_count = get_category()
    
    
    blog_post_queryset = get_object_or_404(Blog, id = id)
    context = {'queryset' : blog_post_queryset,
               'category_count':category_count,
               'featuredpost':featuredpost,
               }
    return render(request, 'blog/blogpost.html', context)

def all_blog(request):
    title = 'all-blog'
    category_count = get_category()
    
     # for the pagination of blog home
    postlist = Post.objects.all()
    featuredpost = Post.objects.filter(featured=True)
    
    paginator = Paginator(postlist, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) 
           
    context = {
        'category_count':category_count,
        'featuredpost':featuredpost,
        
        'title':title,
        'queryset':paginated_queryset,
        'page_request_var':page_request_var
            }
    
    return render(request, 'blog/blogview.html', context)



def createpost(request):
    author = get_author(request.user)
    title="Create Post"
    
    form = PostForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post-detail', kwargs={'id':form.instance.id}))
    
    context = {
                'form':form, 
                'author':author,
                'title':title,
               }
        
    return render(request, 'blog/updatepost.html', context)


    

def updatepost(request, id):
    title= 'updatepost'
    
    author = get_author(request.user)
    post = get_object_or_404(Post, id=id)  
    
    form = PostForm(request.POST or None, request.FILES  or None, instance = post )
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        
        form.instance.author = author
        if form.is_valid():
            if form.instance.thumbnail == None:
                thumbnail = post.thumbnail
                form.instance.thumbnail = thumbnail
            else:
                print(post.thumbnail)
            form.save()

            return HttpResponseRedirect(reverse('post-detail', kwargs={'id':form.instance.id}))
    context = {'form':form,
               'title':title,
               'author':author,}
    return render(request, 'blog/updatepost.html', context)