from django.shortcuts import render
import json
from .models import *
from haystack.query import SearchQuerySet
from django.http import HttpResponse
 
def autocomplete(request):
	sqs=SearchQuerySet().autocomplete(content_auto=search_query)[:5]
	suggestions=[result.title for result in sqs]
	the_data=json.dumps({
		'results':suggestions
		})
        return HttpResponse(the_data)
