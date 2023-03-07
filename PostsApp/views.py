from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm



def all_posts(request):
    all_posts = Post.objects.all()

    print("REQUEST.USER",(str(request.user)))

    context = {'all_posts': all_posts, }

    return render(request, 'Posts/all-posts.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    context= {'post': post, 'req': str(request.user)}
    return render(request, 'Posts/post-detail.html', context)

@login_required
def post_form(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print("ESTE ES DATA", data)
            new_post = Post(author = request.user,
                            title = data['title'],
                            subtitle=data['subtitle'],
                            post_description = data['post_description'],
                            post_img = data['post_img'])
            new_post.save()
            return redirect('all-posts')

    context = {'form':form}
    return render(request, 'Posts/post-form.html', context)

@login_required
def delete_post(request, pk):
    post_to_delete = Post.objects.get(id= pk)
    context = {'post_delete': post_to_delete}

    if request.method == 'POST':
        post_to_delete.delete()
        return redirect('all-posts')

    return render(request, 'alert.html', context)

@login_required
def update_post(request, pk):
    post_update = Post.objects.get(id= pk)
    post_form = PostForm(instance=post_update)
    update = True


    context = {'form': post_form, 'update': update}

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post_update)
        form.save()
        
        return redirect('all-posts')


    return render(request, 'Posts/post-form.html', context)

