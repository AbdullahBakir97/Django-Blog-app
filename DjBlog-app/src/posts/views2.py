from django.views import generic
from .models import Post

'''
by default : 
model_opration
template_name = post_list.html
context_name = post_list or object_list 

'''
class PostList(generic.ListView):
    model = Post


'''
by default :
temlate_name = post_details.html
context_name = post or object
    
'''
class PostDetail(generic.DetailView):
    model = Post