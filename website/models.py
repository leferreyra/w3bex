from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Tag(models.Model):
	"""
	Clasifican el contenido de los Posts. Un Post puede tener muchos tags
	y un tag puede identificar muchos posts
	"""

	tag_name = models.CharField(max_length=50)

	def __unicode__(self):

		return self.tag_name


class Post(models.Model):
	"""
	Representa cada articulo escrito en el blog
	"""

	title = models.CharField(max_length=150)
	author = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag)
	source = models.CharField(max_length=300, blank=True)
	slug = models.CharField(max_length=150, blank=True)
	body = models.TextField()
	published = models.BooleanField();

	def pretty_date(self):

		return self.date.strftime("%d/%m/%Y a las %H:%M")

	def save(self, *args, **kwargs):

		# if the objects is just created doesn't have
		# id so we create the slug from the title
		if not self.id:
			self.slug = slugify(self.title)

		super(Post, self).save(args, kwargs)


	def __unicode__(self):

		return self.title