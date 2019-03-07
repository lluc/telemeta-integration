# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.item_transcoding_flag import (
    ItemTranscodingFlag as ItemTranscodingFlagModel)
from ..serializers.item_transcoding_flag import ItemTranscodingFlagSerializer


class ItemTranscodingFlagViewSet(viewsets.ModelViewSet):
    """
    ItemTranscodingFlag management
    """

    queryset = ItemTranscodingFlagModel.objects.all()
    serializer_class = ItemTranscodingFlagSerializer
