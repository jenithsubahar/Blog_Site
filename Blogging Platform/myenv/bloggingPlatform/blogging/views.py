from django.shortcuts import render,redirect
from .models import User,Log,BlogPost,Comment
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.

def submit_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        comment_text = request.POST.get('comment')
        post = get_object_or_404(BlogPost, pk=post_id)
        comment = Comment.objects.create(post=post, text=comment_text)
        return JsonResponse({'comment': comment.text})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def reg(request):

    if request.method == 'POST':
        # Get form data from the request
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create and save the user object
        user = User.objects.create(name=name, mobile=mobile, email=email, password=password)
        user.save()
        return redirect('login') 
        # Redirect to a success page or any other page
    return render(request, 'register.html')


def log(request):
    # return render(request, 'login.html')
    if request.method == 'POST':
        # Get form data from the request
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create and save the user object
        log = Log.objects.create(email=email, password=password)
        log.save()
        return redirect('blogPage') 
        # Redirect to a success page or any other page
    return render(request, 'login.html')



def blog(request):
    return render(request, 'blogPage.html')


def create(request):
    # return render(request, 'blogCreate.html')

    if request.method == 'POST':
        # Extract form data from the request
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image') if 'image' in request.FILES else None
        
        # Create a new BlogPost object and save it to the database
        blog_post = BlogPost(title=title, content=content, image=image)
        blog_post.save()

        return redirect('blogView') 
        # Redirect to a success page or any other page
    return render(request, 'blogCreate.html')



def view(request):
    # return render(request, 'blogView.html')
    # def blog_view(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blogView.html', {'blog_posts': blog_posts})

def delete_post(request, post_id):
    # Find the post by its ID or return 404 if not found
    post = get_object_or_404(BlogPost, id=post_id)

    # Delete the post
    post.delete()

    # Return a success response
    redirect("blogView")
    return JsonResponse({'message': 'Post deleted successfully'})


def home(request):
    return redirect('blogView.html') 
