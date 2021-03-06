# Copyright (c) 2010-2012 Robin Jarry
#
# This file is part of EVE Corporation Management.
#
# EVE Corporation Management is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# EVE Corporation Management is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# EVE Corporation Management. If not, see <http://www.gnu.org/licenses/>.

__date__ = "2012 08 01"
__author__ = "diabeteman"

from django.conf.urls.defaults import patterns

urlpatterns = patterns('ecm.apps.corp.views',
    (r'^$',                             'corp'),
    (r'^standings/$',                   'standings.corp_standings'),

    # multi-corp urls
    (r'^contact/$',                     'contact.handle_contact'),
    (r'^auth/startsession/$',           'auth.start_session'),
    (r'^auth/endsession/$',             'auth.end_session'),
    (r'^share/allowed/$',               'share.list_allowed_shares'),
    
    # shared data
    (r'^share/details/$',               'share.details'),
    (r'^share/standings/corp/$',        'share.corp_standings'),
    (r'^share/standings/alliance/$',    'share.alliance_standings'),
)

