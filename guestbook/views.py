from django import http
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import models
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.html import escape
from forms import EntryForm
from utils import render_to


@render_to('guestbook/thankyou.html')
def post_entry(request, next=None):
    """
    Post a entry.

    HTTP POST is required. If ``POST['submit'] == "preview"`` or if there are
    errors a preview template, ``guestbook/preview.html``, will be rendered.
    """

    # Require POST
    if request.method != 'POST':
        return http.HttpResponseNotAllowed(["POST"])

    # Fill out some initial data fields from an authenticated user, if present
    data = request.POST.copy()
    if request.user.is_authenticated():
        if not data.get('name', ''):
            data["name"] = request.user.get_full_name()
        #if not data.get('email', ''):
        #    data["email"] = request.user.email

    # Do we want to preview the entry?
    preview = data.get("submit", "").lower() == "preview" or \
              data.get("preview", None) is not None

    # Construct the entry form
    form = EntryForm(data=data)

    # Check security information
    if form.security_errors():
        return HttpResponseBadRequest(
            "The entry form failed security verification: %s" % \
                escape(str(form.security_errors())))

    # If there are errors or if we requested a preview show the entry
    if form.errors or preview:
        return render_to_response("guestbook/preview.html", {"form" : form, },
            RequestContext(request, {})
        )

    # Otherwise create the entry
    entry = form.get_entry_object()
    entry.ip = request.META.get("REMOTE_ADDR", None)
    if request.user.is_authenticated():
        entry.user = request.user

    # Save the entry and signal that it was saved
    entry.save()

    return {'form': form}
