# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Post, Category, Comment
from .forms import CommentForm, PostForm, EditForm, CategoryForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDetail(View):

    def get(self, request, slug):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(
                request,
                'Success! Your comment has been submitted.')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(
                request,
                'Success! You unliked the post.')
        else:
            post.likes.add(request.user)
            messages.success(
                request,
                'Success! You liked the post.')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPostView(SuccessMessageMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_message = "Post has been created successfully"


class AddCategoryView(SuccessMessageMixin, generic.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'
    success_message = "Category has been added successfully"


def category_view(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats.title(),
                  'category_posts': category_posts})


class EditPostView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    success_message = "Post has been updated successfully"


class DeletePostView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'

    def get_success_url(self):
        messages.success(self.request, "Post has been deleted successfully")
        return reverse_lazy('home')


def delete_post_comment(request, comment_id):
    '''
    Deletes the comment from the post
    '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can delete comments')
        return redirect(reverse('home'))

    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment has been deleted!')

    return redirect(reverse('home'))
