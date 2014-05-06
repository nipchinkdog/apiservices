#! Views
#! basic imports in django views
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.db import transaction

#! django class views
from django.views.generic.base import View

#! third parties
import json
import urllib2
import simplejson

#! python modules
import requests
