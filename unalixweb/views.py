from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponsePermanentRedirect,
    HttpResponseServerError,
    JsonResponse
)
from django.shortcuts import render
from unalix import clear_url, unshort_url

def home(request):
    return render(request, 'index.html')

def api(request):

    method = request.GET.get("method")
    old_url = request.GET.get("url")
    output = request.GET.get("output")

    if not old_url:
        return HttpResponseBadRequest()

    if not output:
        output = "html"
    elif not output in ["json", "html", "redirect"]:
        return HttpResponseBadRequest()

    if not method:
        method = "unshort"
    elif not method in ["clear", "unshort"]:
        return HttpResponseBadRequest()

    try:
        if method == "unshort":
            new_url = unshort_url(old_url, parse_documents=True)
        elif method == "clear":
            new_url = clear_url(old_url)
    except Exception as exception:
        context = {'exception': str(exception)}
        if output == "html":
            return render(request, 'error.html', context)
        elif output == "json":
            return JsonResponse(context)
        elif output == "redirect":
            return HttpResponseServerError()
    else:
        context = {"new_url": new_url}
        if output == "html":
            return render(request, 'success.html', context)
        elif output == "json":
            return JsonResponse(context)
        elif output == "redirect":
            return HttpResponsePermanentRedirect(new_url)
