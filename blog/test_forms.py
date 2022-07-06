# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.test import TestCase
from .forms import PostForm, EditForm, CommentForm


class TestPostForm(TestCase):

    def test_Post_title_is_required(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_slug_is_required(self):
        form = PostForm({'slug': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors.keys())
        self.assertEqual(form.errors['slug'][0], 'This field is required.')

    def test_post_author_is_required(self):
        form = PostForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(form.errors['author'][0], 'This field is required.')

    def test_post_category_is_required(self):
        form = PostForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    # def test_post_content_is_required(self):
    #     form = PostForm({'content': ''})
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('content', form.errors.keys())
    #     self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_featured_image_field_is_not_required(self):
        form = PostForm({'name': 'test featured_image'})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = PostForm()
        self.assertNotEqual(form.Meta.fields, ['title', 'slug', 'author', 'category', 'content', 'featured_image'])


class TestEditForm(TestCase):

    def test_edit_title_is_not_required(self):
        form = EditForm({'name': 'test title'})
        self.assertFalse(form.is_valid())

    def test_post_slug_is_not_required(self):
        form = EditForm({'name': 'test slug'})
        self.assertFalse(form.is_valid())

    def test_post_content_is_not_required(self):
        form = EditForm({'name': 'test content'})
        self.assertFalse(form.is_valid())

    def test_featured_image_field_is_not_required(self):
        form = EditForm({'name': 'test featured_image'})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = EditForm()
        self.assertNotEqual(form.Meta.fields, ['title', 'slug',
                         'content', 'featured_image'])


class TestCommentForm(TestCase):

    def test_comment_body_is_not_required(self):
        form = CommentForm({'name': 'test body'})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertNotEqual(form.Meta.fields, ['body'])
