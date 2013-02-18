from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Post


# Vista provisoria del index
def index(request):

	return render_to_response(
		'main.html', {},
		context_instance=RequestContext(request));


def post(request, slug):

	post = get_object_or_404(Post, slug=slug)

	return render_to_response(
		'post.html', {"post": post},
		context_instance=RequestContext(request));