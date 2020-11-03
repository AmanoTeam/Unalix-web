from django.http import (
	HttpResponse,
	HttpResponseBadRequest,
	JsonResponse
)
from django.shortcuts import render

from unalix import clear_url, unshort_url

def api(request):
	
	method = request.GET.get("method")
	old_url = request.GET.get("url")
	output = request.GET.get("output")
	
	if not old_url:
		return HttpResponseBadRequest()
	
	if not output:
		output = "json"
	elif not output in ["clear", "unshort"]:
		return HttpResponseBadRequest()
	
	if not method:
		method = "json"
	elif not method in ["clear", "unshort"]:
		return HttpResponseBadRequest()
	
	try:
		if method == "unshort":
			new_url = unshort_url(old_url)
		elif method == "clear":
			new_url = clear_url(old_url)
	except Exception as exception:
		context = {'exception': exception}
		if output == "html":
			return render(request, 'error.html', context)
		elif output == "json":
			return JsonResponse(context)
	else:
		context = {'old_url': old_url, "new_url": new_url}
		if output == "html":
			return render(request, 'success.html', context)
		elif output == "json":
			return JsonResponse(context)
	
	