from django.shortcuts import render_to_response
from django.template import RequestContext


def static_view(request, **kwargs):
	"""
	Muestra archivos html estaticos. El nombre del
	archivo esta en el diccionario kwargs con la clave
	page
	"""

	return render_to_response(kwargs['page'], {}, 
		context_instance=RequestContext(request))

	
