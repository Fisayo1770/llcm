from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Comment
from .forms import CommentForm, PostForm
# Create your views here.
class PostCreatView(CreateView):
    form_class = PostForm
    template_name = 'lovcom/post_create.html'

    def form_valid(self, form):
        action = self.request.POST.get('action')
        if action == 'SAVE':
            return super().form_valid(form)
        elif action == 'PREVIEW':
            preview = Post(
                body=form.cleaned_data['body'],
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                phone=form.cleaned_data['phone'],
            )
            ctx = self.get_context_data(preview=preview)
            return self.render_to_response(context=ctx)
        return HttpResponseBadRequest()

def post_list(request):
    posts = Post.published.all()
    return render(request, 'lovcom/post/list.html', {'posts': posts})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'post'
    pagination_by = 30
    template_name = 'lovcom/post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
        publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'lovcom/post/detail.html', {'post': post, 'comments':comments,
                'new_comment': new_comment, 'comment_form': comment_form})

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                'lovcom/post/list.html',
                {'page': page,
                'posts': posts})
