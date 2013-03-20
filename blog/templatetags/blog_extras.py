from django import template
from w3bex import settings
import markdown

register = template.Library()

@register.filter()
def markdown_img(value, images):
	"""
	Convierte markdown a html, agregando las referencias a las
	imagenes en el markdown utilizando los modelos de imagenes.
	"""

	md = markdown.Markdown()

	for image in images:

	    image_url = image.image.url

	    # Agregar la referencia a la imagen en markdown
	    md.references[image.name] = (image_url, '')

	return md.convert(value)
