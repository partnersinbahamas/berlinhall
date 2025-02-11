from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from .templatetags.blog_tags import get_latest_post, get_latest_category_post, posts_by_category, get_all_tags, get_post_by_slug, get_all_posts, get_latest_tag_post
from .models import Post
from django.db.models import F

# Create your views here.

class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        context['background_title'] = "Berlin – A City of Freedom and Contrasts 🇩🇪✨"
        context['background_content'] = "Berlin is a unique blend of history, art, and modern urban life. Medieval churches stand next to graffiti-covered walls, and strict architecture contrasts with the city’s vibrant alternative culture. The city’s turbulent past is ever-present: the Berlin Wall, once a symbol of division, is now an open-air canvas for street artists. Today, Berlin is a hub for startups, nightlife, and limitless self-expression. From the Brandenburg Gate to riverside clubs along the Spree, there’s something for everyone in this dynamic city. 🏙️🎨🎶 Warst du schon mal in Berlin? 😊"
        context['tab_title'] = 'Home'
        context['attached_post'] = get_latest_post()
        return context

class PostCategories(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_latest_category_post(category_slug=self.kwargs['slug'])
        context['tags'] = get_all_tags()

        return context
    
    def get_queryset(self):
        return posts_by_category(category_slug=self.kwargs['slug']).select_related('category')

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/single_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        context['posts'] = get_all_posts()
        context['tags'] = post.tags.all()

        return context

    def get_object(self, queryset=None):
        post = super().get_object(queryset)

        Post.objects.filter(pk=post.pk).update(views = F('views') + 1)
        post.refresh_from_db(fields=['views'])

        return post

class PostTags(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_latest_tag_post(self.kwargs['slug'])
        context['tags'] = get_all_tags()

        return context

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug']).prefetch_related('tags')