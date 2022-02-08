from django.urls import path
from .views import blog_post, blogview, search_blog, all_blog, post_detail, createpost


urlpatterns = [
    path('', blogview, name='blogview'),
    path('create-post', createpost, name='create-post'),
       
    path('<id>', post_detail, name = 'post-detail' ),
    
    
    path('', all_blog, name = 'all-blog'),
    path('all-blog/<id>', blog_post, name = 'blog-post'),
    
    path('search-blog' ,search_blog, name='search-blog'),
    
]

