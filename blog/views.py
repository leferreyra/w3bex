from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Post, Tag


# Vista provisoria del index
def index(request):

	return render_to_response(
		'main.html', {},
		context_instance=RequestContext(request));


def post(request, slug):

	post = get_object_or_404(Post, slug=slug)
	top_posts = Post.objects.all()

	return render_to_response(
		'post.html', {
			"post": post,
			"top_posts":top_posts 
			},
		context_instance=RequestContext(request));


def post_list(request):

	top_posts = Post.objects.all()
	posts = top_posts;

	return render_to_response(
		'post-list.html', {
			"posts": posts,
			"top_posts":top_posts 
			},
		context_instance=RequestContext(request));


def post_by_tag(request, tagname):
    
	top_posts = Post.objects.all()

	tag = get_object_or_404(Tag, tag_name=tagname)
	posts = tag.post_set.all()

	return render_to_response(
		'post-list.html', {
			"posts": posts,
			"top_posts":top_posts 
			},
		context_instance=RequestContext(request));

