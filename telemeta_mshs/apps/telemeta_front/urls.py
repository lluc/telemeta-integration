# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.conf.urls import url, include

from .views import (
    home as home_integration,
    institution, institution_add, institution_delete, institution_detail,
    institution_edit,
    personne, personne_add, personne_detail, personne_edit, personne_delete,
    location, location_add, location_detail, location_edit, location_delete,
    location_gis, location_gis_add, location_gis_detail, location_gis_edit,
    location_gis_delete,
    fond, fond_add, fond_detail, fond_edit, fond_delete,
    mission, mission_add, mission_detail, mission_edit, mission_delete,
    collection, collection_add, collection_detail, collection_edit,
    collection_delete,
    item, item_add, item_detail, item_edit,
    item_delete,
)

from .views.enum import (
    instrument, instrument_edit, instrument_delete, instrument_detail,
    instrument_add,
    domain_song, domain_song_edit, domain_song_delete, domain_song_detail,
    domain_song_add,
    domain_music, domain_music_edit, domain_music_delete, domain_music_detail,
    domain_music_add,
    domain_tale, domain_tale_edit, domain_tale_delete, domain_tale_detail,
    domain_tale_add,
    domain_vocal, domain_vocal_edit, domain_vocal_delete, domain_vocal_detail,
    domain_vocal_add,
    dance, dance_edit, dance_delete, dance_detail,
    dance_add,
    musical_organization, musical_organization_edit,
    musical_organization_delete, musical_organization_detail,
    musical_organization_add,
    hornbostelsachs, hornbostelsachs_edit, hornbostelsachs_delete,
    hornbostelsachs_detail, hornbostelsachs_add,
    musical_group, musical_group_edit,
    musical_group_delete, musical_group_detail,
    musical_group_add,
)


urlpatterns = [
    url(r'^$', home_integration.HomePageView.as_view(), name="home"),
    url(r'^select2/', include('django_select2.urls')),

    # Institutions
    url(r'^institution/$', institution.InstitutionView.as_view(),
        name="institution"),
    url(r'^institution/(?P<id>[0-9]+)/$',
        institution_detail.InstitutionDetail.as_view(),
        name='institution-detail'),
    url(r'^institution/add/$',
        institution_add.InstitutionAdd.as_view(),
        name='institution-add'),
    url(r'^institution/edit/(?P<id>[0-9]+)$',
        institution_edit.InstitutionEdit.as_view(),
        name='institution-edit'),
    url(r'^institution/delete/(?P<id>[0-9]+)$',
        institution_delete.InstitutionDelete.as_view(),
        name='institution-delete'),

    # Authority  (Personnes)
    url(r'^authority/$', personne.PersonneView.as_view(),
        name="personne"),
    url(r'^authority/add/$',
        personne_add.PersonneAdd.as_view(),
        name='personne-add'),
    url(r'^authority/(?P<id>[0-9]+)/$',
        personne_detail.PersonneDetail.as_view(),
        name='personne-detail'),
    url(r'^authority/edit/(?P<id>[0-9]+)$',
        personne_edit.PersonneEdit.as_view(),
        name='personne-edit'),
    url(r'^authority/delete/(?P<id>[0-9]+)$',
        personne_delete.PersonneDelete.as_view(),
        name='personne-delete'),

    # Location ( Lieux)
    url(r'^location/$', location.LocationView.as_view(),
        name="location"),
    url(r'^location/add/$',
        location_add.LocationAdd.as_view(),
        name='location-add'),
    url(r'^location/(?P<id>[0-9]+)/$',
        location_detail.LocationDetail.as_view(),
        name='location-detail'),
    url(r'^location/edit/(?P<id>[0-9]+)$',
        location_edit.LocationEdit.as_view(),
        name='location-edit'),
    url(r'^location/delete/(?P<id>[0-9]+)$',
        location_delete.LocationDelete.as_view(),
        name='location-delete'),

    # Location GIS ( Lieux)
    url(r'^location_gis/$', location_gis.LocationView.as_view(),
        name="location_gis"),
    url(r'^location_gis/add/$',
        location_gis_add.LocationAdd.as_view(),
        name='location_gis-add'),
    url(r'^location_gis/(?P<id>[0-9]+)/$',
        location_gis_detail.LocationDetail.as_view(),
        name='location_gis-detail'),
    url(r'^location_gis/edit/(?P<id>[0-9]+)$',
        location_gis_edit.LocationEdit.as_view(),
        name='location_gis-edit'),
    url(r'^location_gis/delete/(?P<id>[0-9]+)$',
        location_gis_delete.LocationDelete.as_view(),
        name='location_gis-delete'),

    # Fonds
    url(r'^fond/$', fond.FondView.as_view(),
        name="fond"),
    url(r'^fond/add/$',
        fond_add.FondAdd.as_view(),
        name='fond-add'),
    url(r'^fond/(?P<id>[0-9]+)/$',
        fond_detail.FondDetail.as_view(),
        name='fond-detail'),
    url(r'^fond/edit/(?P<id>[0-9]+)$',
        fond_edit.FondEdit.as_view(),
        name='fond-edit'),
    url(r'^fond/delete/(?P<id>[0-9]+)$',
        fond_delete.FondDelete.as_view(),
        name='fond-delete'),

    # Mission
    url(r'^mission/$', mission.MissionView.as_view(),
        name="mission"),
    url(r'^institution/(?P<id_institution>[0-9]+)/fond/(?P<id_fond>[0-9]+)/mission/add/$',  # noqa
        mission_add.MissionAdd.as_view(),
        name='mission-add'),
    url(r'^mission/(?P<id>[0-9]+)/$',
        mission_detail.MissionDetail.as_view(),
        name='mission-detail'),
    url(r'^mission/edit/(?P<id>[0-9]+)$',
        mission_edit.MissionEdit.as_view(),
        name='mission-edit'),
    url(r'^mission/delete/(?P<id>[0-9]+)$',
        mission_delete.MissionDelete.as_view(),
        name='mission-delete'),

    # Collection/Enquetes
    url(r'^collection/$', collection.CollectionView.as_view(),
        name="collection"),
    url(r'^institution/(?P<id_institution>[0-9]+)/fond/(?P<id_fond>[0-9]+)/mission/(?P<id_mission>[0-9]+)/collection/add/$',  # noqa
        collection_add.CollectionAdd.as_view(),
        name='collection-add'),
    url(r'^collection/(?P<id>[0-9]+)/$',
        collection_detail.CollectionDetail.as_view(),
        name='collection-detail'),
    url(r'^collection/edit/(?P<id>[0-9]+)$',
        collection_edit.CollectionEdit.as_view(),
        name='collection-edit'),
    url(r'^collection/delete/(?P<id>[0-9]+)$',
        collection_delete.CollectionDelete.as_view(),
        name='collection-delete'),

    # Items
    url(r'^item/$', item.ItemView.as_view(),
        name="item"),
    url(r'^institution/(?P<id_institution>[0-9]+)/fond/(?P<id_fond>[0-9]+)/mission/(?P<id_mission>[0-9]+)/collection/(?P<id_collection>[0-9]+)/item/add/$',  # noqa
        item_add.ItemAdd.as_view(),
        name='item-add'),
    url(r'^item/(?P<id>[0-9]+)/$',
        item_detail.ItemDetail.as_view(),
        name='item-detail'),
    url(r'^item/edit/(?P<id>[0-9]+)$',
        item_edit.ItemEdit.as_view(),
        name='item-edit'),
    url(r'^item/delete/(?P<id>[0-9]+)$',
        item_delete.ItemDelete.as_view(),
        name='item-delete'),

    # Instruments
    url(r'^instrument/$', instrument.InstrumentView.as_view(),
        name="instrument"),
    url(r'^instrument/add/$',
     instrument_add.InstrumentAdd.as_view(),
     name='instrument-add'),
    url(r'^instrument/(?P<id>[0-9]+)/$',
     instrument_detail.InstrumentDetail.as_view(),
     name='instrument-detail'),
    url(r'^instrument/edit/(?P<id>[0-9]+)$',
         instrument_edit.InstrumentEdit.as_view(),
         name='instrument-edit'),
    url(r'^instrument/delete/(?P<id>[0-9]+)$',
        instrument_delete.InstrumentDelete.as_view(),
        name='instrument-delete'),

    # Domain Song
    url(r'^domain_song/$', domain_song.DomainSongView.as_view(),
        name="domain_song"),
    url(r'^domain_song/add/$',
     domain_song_add.DomainSongAdd.as_view(),
     name='domain_song-add'),
    url(r'^domain_song/(?P<id>[0-9]+)/$',
     domain_song_detail.DomainSongDetail.as_view(),
     name='domain_song-detail'),
    url(r'^domain_song/edit/(?P<id>[0-9]+)$',
         domain_song_edit.DomainSongEdit.as_view(),
         name='domain_song-edit'),
    url(r'^domain_song/delete/(?P<id>[0-9]+)$',
        domain_song_delete.DomainSongDelete.as_view(),
        name='domain_song-delete'),

    # Domain Music
    url(r'^domain_music/$', domain_music.DomainMusicView.as_view(),
        name="domain_music"),
    url(r'^domain_music/add/$',
     domain_music_add.DomainMusicAdd.as_view(),
     name='domain_music-add'),
    url(r'^domain_music/(?P<id>[0-9]+)/$',
     domain_music_detail.DomainMusicDetail.as_view(),
     name='domain_music-detail'),
    url(r'^domain_music/edit/(?P<id>[0-9]+)$',
         domain_music_edit.DomainMusicEdit.as_view(),
         name='domain_music-edit'),
    url(r'^domain_music/delete/(?P<id>[0-9]+)$',
        domain_music_delete.DomainMusicDelete.as_view(),
        name='domain_music-delete'),

    # Domain Tale
    url(r'^domain_tale/$', domain_tale.DomainTaleView.as_view(),
        name="domain_tale"),
    url(r'^domain_tale/add/$',
     domain_tale_add.DomainTaleAdd.as_view(),
     name='domain_tale-add'),
    url(r'^domain_tale/(?P<id>[0-9]+)/$',
     domain_tale_detail.DomainTaleDetail.as_view(),
     name='domain_tale-detail'),
    url(r'^domain_tale/edit/(?P<id>[0-9]+)$',
         domain_tale_edit.DomainTaleEdit.as_view(),
         name='domain_tale-edit'),
    url(r'^domain_tale/delete/(?P<id>[0-9]+)$',
        domain_tale_delete.DomainTaleDelete.as_view(),
        name='domain_tale-delete'),


    # Domain Vocal
    url(r'^domain_vocal/$', domain_vocal.DomainVocalView.as_view(),
        name="domain_vocal"),
    url(r'^domain_vocal/add/$',
     domain_vocal_add.DomainVocalAdd.as_view(),
     name='domain_vocal-add'),
    url(r'^domain_vocal/(?P<id>[0-9]+)/$',
     domain_vocal_detail.DomainVocalDetail.as_view(),
     name='domain_vocal-detail'),
    url(r'^domain_vocal/edit/(?P<id>[0-9]+)$',
         domain_vocal_edit.DomainVocalEdit.as_view(),
         name='domain_vocal-edit'),
    url(r'^domain_vocal/delete/(?P<id>[0-9]+)$',
        domain_vocal_delete.DomainVocalDelete.as_view(),
        name='domain_vocal-delete'),

    # Dance
    url(r'^dance/$', dance.DanceView.as_view(),
        name="dance"),
    url(r'^dance/add/$',
     dance_add.DanceAdd.as_view(),
     name='dance-add'),
    url(r'^dance/(?P<id>[0-9]+)/$',
     dance_detail.DanceDetail.as_view(),
     name='dance-detail'),
    url(r'^dance/edit/(?P<id>[0-9]+)$',
         dance_edit.DanceEdit.as_view(),
         name='dance-edit'),
    url(r'^dance/delete/(?P<id>[0-9]+)$',
        dance_delete.DanceDelete.as_view(),
        name='dance-delete'),

    # Musical Organization
    url(r'^musical_organization/$',
        musical_organization.MusicalOrganizationView.as_view(),
        name="musical_organization"),
    url(r'^musical_organization/add/$',
        musical_organization_add.MusicalOrganizationAdd.as_view(),
        name='musical_organization-add'),
    url(r'^musical_organization/(?P<id>[0-9]+)/$',
        musical_organization_detail.MusicalOrganizationDetail.as_view(),
        name='musical_organization-detail'),
    url(r'^musical_organization/edit/(?P<id>[0-9]+)$',
         musical_organization_edit.MusicalOrganizationEdit.as_view(),
         name='musical_organization-edit'),
    url(r'^musical_organization/delete/(?P<id>[0-9]+)$',
        musical_organization_delete.MusicalOrganizationDelete.as_view(),
        name='musical_organization-delete'),

    # hornbostelsachs
    url(r'^hornbostelsachs/$', hornbostelsachs.HornbostelsachsView.as_view(),
        name="hornbostelsachs"),
    url(r'^hornbostelsachs/add/$',
     hornbostelsachs_add.HornbostelsachsAdd.as_view(),
     name='hornbostelsachs-add'),
    url(r'^hornbostelsachs/(?P<id>[0-9]+)/$',
     hornbostelsachs_detail.HornbostelsachsDetail.as_view(),
     name='hornbostelsachs-detail'),
    url(r'^hornbostelsachs/edit/(?P<id>[0-9]+)$',
         hornbostelsachs_edit.HornbostelsachsEdit.as_view(),
         name='hornbostelsachs-edit'),
    url(r'^hornbostelsachs/delete/(?P<id>[0-9]+)$',
        hornbostelsachs_delete.HornbostelsachsDelete.as_view(),
        name='hornbostelsachs-delete'),

    # Musical Group
    url(r'^musical_group/$',
        musical_group.MusicalGroupView.as_view(),
        name="musical_group"),
    url(r'^musical_group/add/$',
        musical_group_add.MusicalGroupAdd.as_view(),
        name='musical_group-add'),
    url(r'^musical_group/(?P<id>[0-9]+)/$',
        musical_group_detail.MusicalGroupDetail.as_view(),
        name='musical_group-detail'),
    url(r'^musical_group/edit/(?P<id>[0-9]+)$',
         musical_group_edit.MusicalGroupEdit.as_view(),
         name='musical_group-edit'),
    url(r'^musical_group/delete/(?P<id>[0-9]+)$',
        musical_group_delete.MusicalGroupDelete.as_view(),
        name='musical_group-delete'),
]
