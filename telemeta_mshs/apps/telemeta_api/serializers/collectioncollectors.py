# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import serializers

from .MediaCollection import MediacollectionSerializer
from .authority import AuthoritySerializer

from ..models.collectioncollectors import(
    CollectionCollectors as CollectionCollectorsModel)
from telemeta.models.collection import MediaCollection as MediacollectionModel
from ..models.authority import Authority as AuthorityModel


class CollectionCollectorsSerializer(serializers.ModelSerializer):
    """
    Common serializer for all collection's collector actions
    """
    collection = MediacollectionSerializer(required=True)
    collector = AuthoritySerializer(required=True)

    class Meta:
        model = CollectionCollectorsModel
        fields = '__all__'

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details
               of collectioncollectors
        :return: returns a successfully created ext_collection record
        """

        collection_data = validated_data.pop('collection')
        # Create an oject Mediacollection with the data converted in dict
        collection = MediacollectionModel.objects.create(**collection_data)

        collector_data = validated_data.pop('collector')
        # Create an oject collector (Authority) with the data converted in dict
        collector = AuthorityModel.objects.create(**collector_data)

        # Create an oject CollectionCollectors
        CollectionCollectors = \
            CollectionCollectorsModel.objects.create(
                collection=collection, collector=collector, **validated_data)

        return CollectionCollectors
