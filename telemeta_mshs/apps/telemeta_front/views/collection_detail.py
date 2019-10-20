# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools
from telemeta_front.forms.collection import CollectionForm


class CollectionDetail(FrancoraliteTemplateView):
    template_name = "../templates/collection-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(CollectionDetail, self).get_context_data(**kwargs)
            # Obtain values of the record collection
            context['collection'] = tools.request_api(
                '/api/collection/'+context['id']+'/complete/')
            # Obtain values of related items
            context['items'] = tools.request_api(
                '/api/item/?collection=' + context['id'])
            context['form'] = CollectionForm()
        except Exception as err:
            context['collection'] = {}
            context['items'] = []
            context['error'] = str(err.message) + ":" + str(type(err).__name__)
        return context
