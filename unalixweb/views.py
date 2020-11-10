from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponsePermanentRedirect,
    HttpResponseServerError,
    JsonResponse
)
from django.shortcuts import render
import unalix

unalix._config.timeout = 2.5

def home(request):
    return render(request, 'index.html')

def api(request):

    method = request.GET.get("method")
    old_url = request.GET.get("url")
    output = request.GET.get("output")

    if not output:
        output = "html"

    if not method:
        method = "unshort"

    if not old_url:
        return HttpResponseBadRequest()

    if not output in ["json", "html", "redirect"]:
        return HttpResponseBadRequest()

    if not method in ["clear", "unshort"]:
        return HttpResponseBadRequest()

    try:
        if method == "unshort":
            new_url = unalix.unshort_url(old_url, parse_documents=True)
        elif method == "clear":
            new_url = unalix.clear_url(old_url)
    except unalix._exceptions.ConnectionError as exception:
            new_url = exception.url
    except Exception as exception:
        context = {
            'exception': str(exception)
        }
        if output == "html":
            return render(request, 'error.html', context)
        if output == "json":
            return JsonResponse(context)
        if output == "redirect":
            return HttpResponseServerError()

    context = {
        "new_url": new_url
    }

    if output == "html":
        return render(request, 'success.html', context)

    if output == "json":
        return JsonResponse(context)

    if output == "redirect":
        return HttpResponsePermanentRedirect(new_url)
