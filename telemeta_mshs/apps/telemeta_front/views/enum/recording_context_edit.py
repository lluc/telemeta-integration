# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from rest_framework import status
import requests
from requests.exceptions import RequestException
from settings import FRONT_HOST_URL
from telemeta_front.forms.recording_context import RecordingContextForm
from django.shortcuts import render


class RecordingContextEdit(FormView):
    template_name = "../templates/enum/recording_context-add.html"
    form_class = RecordingContextForm
    success_url = '/recording_context/'

    def get_context_data(self, **kwargs):
        context = super(RecordingContextEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/recording_context/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['recording_context'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        recording_context = requests.get(
            FRONT_HOST_URL + '/api/recording_context/' + str(id))
        form = RecordingContextForm(initial=recording_context.json())

        return render(request,
                      '../templates/enum/recording_context-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = RecordingContextForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/recording_context/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/recording_context/edit' + str(id)
                                                + '/')
                return HttpResponseRedirect('/recording_context/')

            except RequestException:
                return HttpResponseRedirect('/recording_context/edit')

        return HttpResponseRedirect('/recording_context/edit')
