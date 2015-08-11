from django.http import HttpResponseRedirect
from django.contrib import messages

from profanity import profanityScore

class ProfanityFilterMiddleware(object):
    def process_request(self, request):
        rpd = request.body.lower()
        if profanityScore(rpd) >= 10:
            messages.error(request, 'Please remove any obscenities in your message and re-submit. Thank you!')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])