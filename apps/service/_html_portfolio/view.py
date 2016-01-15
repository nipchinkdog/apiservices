# -*- coding: utf-8 -*-
#! variables: ROOT_URL etc
from apps.service._imports.Settings_init import *
from apps.service._imports.Views_init import *


class _Html_Portfolio(View):

    _template = '_portfolio_index.html'

    def get(self, request):
        return render_to_response(self._template,
                                  {},
                                  context_instance=RequestContext(request))