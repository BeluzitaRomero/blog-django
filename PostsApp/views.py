from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm



# ---------------------------------------------------------------------------- #
#                                     POSTS                                    #
# ---------------------------------------------------------------------------- #

def all_posts(request):
    all_posts = Post.objects.all().order_by('-id')

    context = {'all_posts': all_posts, }

    return render(request, 'Posts/all-posts.html', context)

def post_detail(request, pk):
    #En esta view me traigo un post por id y ademas el form de comentarios
    #para poder ver el post y comentar dentro de la misma template
    post = Post.objects.get(id=pk)

    comment_form = CommentForm()

    #Si se hace POST del comentario:
    if request.method == 'POST':
        comment_form= CommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data

            new_comment = Comment(post_id = post, 
                                  comment = data['comment'],
                                  username=request.user)
            new_comment.save()

            #Queria redireccionar dentro del mismo detalle para ver el 
            #comentario en el momento
            return redirect(f'/post-detail/{post.id}')

    #Sino, creo un contexto del listado de comentarios y una evaluacion
    #para saber si existen o no comentarios, para poder usarlo en el template
    #como condicion para mostrar o no el listado

    all_comments = Comment.objects.filter(post_id=post.id)
    len_comments = len(all_comments) > 0

    comment_context = {'all': all_comments, 'len_comments': len_comments}

    #la clave 'req' la utilizo para poder comparar al usuario autenticado con
    #el usuario autor del post y de esa manera, mostrar o no botones de delete/update
    context= {'post': post, 'req': str(request.user), 
              'comments':comment_context, 
              'comment_form':comment_form}
    
    return render(request, 'Posts/post-detail.html', context)



@login_required
def post_form(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
           
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
    context = {'delete': post_to_delete}

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
        
        return redirect(f'/post-detail/{post_update.id}')


    return render(request, 'Posts/post-form.html', context)


# ---------------------------------------------------------------------------- #
#                                   COMMENTS                                   #
# ---------------------------------------------------------------------------- #

@login_required
def delete_comment(request, pk):
    comment_to_delete = Comment.objects.get(id= pk)
    context = {'delete': comment_to_delete}
    print('COMMENT_POST_ID',comment_to_delete.post_id)

    if request.method == 'POST':
        comment_to_delete.delete()
        return redirect(f'/post-detail/{comment_to_delete.post_id.id}')

    return render(request, 'alert.html', context)

# ---------------------------------------------------------------------------- #
#                                   ABOUT ME                                   #
# ---------------------------------------------------------------------------- #

def about_me(request):
    return render(request, 'about-me.html')