# The MIT License - EVE Corporation Management
# 
# Copyright (c) 2010 Robin Jarry
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from ecm.view.auth.forms import PasswordChangeForm, PasswordResetForm, PasswordSetForm
from ecm.data.roles.models import RoleType

__date__ = "2010-01-24"
__author__ = "diabeteman"

from django.conf.urls.defaults import patterns, include
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    ###########################################################################
    # MISC VIEWS
    (r'^admin/',                                    include(admin.site.urls)),
    (r'^captcha/',                                  include('captcha.urls')),
    # static file serving for the development server
    (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],  'django.views.static.serve', 
                                                    {'document_root' : settings.MEDIA_ROOT}),
)

urlpatterns += patterns('django.contrib.auth.views',
    ###########################################################################
    # DJANGO BUILT-IN AUTH VIEWS
    (r'^account/login$',                'login', 
                                            {'template_name' : 'auth/login.html'}),
    (r'^account/logout$',               'logout', 
                                            {'next_page' : '/'}),
    (r'^account/passwordchange$',       'password_change', 
                                            {'template_name' : 'auth/password_change.html', 
                                            'password_change_form' : PasswordChangeForm}),
    (r'^account/passwordchange/done$',  'password_change_done', 
                                            {'template_name' : 'auth/password_change_done.html'}),
    (r'^account/passwordreset$',        'password_reset', 
                                            {'template_name' : 'auth/password_reset.html',
                                             'email_template_name' : 'auth/password_reset_email.txt',
                                             'password_reset_form' : PasswordResetForm,
                                             'post_reset_redirect' : '/account/passwordreset/sent'}),
    (r'^account/passwordreset/sent$',   'password_reset_done', 
                                            {'template_name' : 'auth/password_reset_done.html'}),
    (r'^account/passwordreset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$','password_reset_confirm', 
                                            {'template_name' : 'auth/password_reset_confirm.html',
                                             'set_password_form' : PasswordSetForm}),
    (r'^account/passwordreset/complete$','password_reset_complete',
                                            {'template_name' : 'auth/password_reset_complete.html'}),
                                                    
)
 
urlpatterns += patterns('ecm.view.auth',
    ###########################################################################
    # ECM AUTH + USER PROFILE VIEWS
    (r'^account$',                       'account.account'),
    (r'^account/addapi$',                'account.add_api'),
    (r'^account/deleteapi/(\d+)$',       'account.delete_api'),
    (r'^account/deletecharacter/(\d+)$', 'account.delete_character'),
    (r'^account/editapi/(\d+)$',         'account.edit_api'),
    (r'^account/create$',                'signup.create_account'),
    (r'^account/activate/(\w+)$',        'signup.activate_account'),
    (r'^players$',                       'players.player_list'),
    (r'^players/data$',                  'players.player_list_data'),
    (r'^players/(\d+)$',                 'players.player_details'),
    (r'^players/(\d+)/data$',            'players.player_details_data'),
)

urlpatterns += patterns('ecm.view',
    ###########################################################################
    # COMMON VIEWS
    (r'^$',                     'common.corp'),
    (r'^dashboard$',            'dashboard.dashboard'),
    (r'^cron$',                 'common.trigger_scheduler'),
    (r'^tasks/launch/([^/]+)$', 'common.launch_task'),
)

urlpatterns += patterns('ecm.view.members',
    ###########################################################################
    # MEMBERS VIEWS
    (r'^members$',                          'list.all'),
    (r'^members/data$',                     'list.all_data'),
    (r'^members/history$',                  'history.history'),
    (r'^members/history/data$',             'history.history_data'),
    (r'^members/unassociated$',             'list.unassociated'),
    (r'^members/unassociated/data$',        'list.unassociated_data'),
    (r'^members/unassociated/clip$',        'list.unassociated_clip'),
    (r'^members/accesschanges$',            'access.access_changes'),
    (r'^members/accesschanges/data$',       'access.access_changes_data'),
    (r'^members/(\d+)$',                    'details.details'),
    (r'^members/(\d+)/accesschanges/data',  'details.access_changes_member_data'),
)

urlpatterns += patterns('ecm.view.titles',
    ###########################################################################
    # TITLES VIEWS
    (r'^titles$',                        'list.all'),
    (r'^titles/data$',                   'list.all_data'),
    (r'^titles/changes$',                'changes.changes'),
    (r'^titles/changes/data$',           'changes.changes_data'),
    (r'^titles/(\d+)$',                  'details.details'),
    (r'^titles/(\d+)/composition/data$', 'details.composition_data'),
    (r'^titles/(\d+)/compodiff/data$',   'details.compo_diff_data'),
    (r'^titles/(\d+)/members$',          'members.members'),
    (r'^titles/(\d+)/members/data$',     'members.members_data'),
)

urlpatterns += patterns('ecm.view.roles',
    ###########################################################################
    # ROLES VIEWS
    (r'^roles$',                         'list.root'),
    (r'^roles/update$',                  'list.update_access_level'),
    (r'^roles/([a-zA-Z_]+)$',            'list.role_type'),
    (r'^roles/([a-zA-Z_]+)/data$',       'list.role_type_data'),
    (r'^roles/([a-zA-Z_]+)/(\d+)$',      'details.role'),
    (r'^roles/([a-zA-Z_]+)/(\d+)/data$', 'details.role_data'),
)

urlpatterns += patterns('ecm.view.assets.normal',
    ###########################################################################
    # ASSETS VIEWS
    (r'^assets$',                                   'root'),
    (r'^assets/data$',                              'systems_data'),
    (r'^assets/(\d+)/data$',                        'stations_data'),
    (r'^assets/(\d+)/(\d+)/data$',                  'hangars_data'),
    (r'^assets/(\d+)/(\d+)/(\d+)/data$',            'hangar_content_data'),
    (r'^assets/(\d+)/(\d+)/(\d+)/(\d+)/data$',      'can1_content_data'),
    (r'^assets/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/data$', 'can2_content_data'),
    (r'^assets/search$',                            'search_items'),
)

DATE = r"(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})"

urlpatterns += patterns('ecm.view.assets.diff',
    ###########################################################################
    # ASSET DIFF VIEWS
    (r'^assets/changes$',                           'last_date'),
    (r'^assets/changes/' + DATE + r'$',              'root'),
    (r'^assets/changes/' + DATE + r'/data$',         'systems_data'),
    (r'^assets/changes/' + DATE + r'/(\d+)/data$',   'stations_data'),
    (r'^assets/changes/' + DATE + r'/(\d+)/(\d+)/data$', 'hangars_data'),
    (r'^assets/changes/' + DATE + r'/(\d+)/(\d+)/(\d+)/data$', 'hangar_contents_data'),
    (r'^assets/changes/' + DATE + r'/search$',       'search_items'),
)

role_types = []
for rt in RoleType.objects.all().order_by('id'):
    role_types.append({'item_title': rt.dispName, 'item_url': '/roles/%s' % rt.typeName})

ecm_menus = [
    {'menu_title': 'Home',      'menu_url': '/',            'menu_items': []},
    {'menu_title': 'Dashboard', 'menu_url': '/dashboard',   'menu_items': []},
    {'menu_title': 'Members',   'menu_url': '/members',     'menu_items': [
        {'item_title': 'History', 'item_url': '/members/history'},
        {'item_title': 'Access Changes', 'item_url': '/members/accesschanges'},
        {'item_title': 'Unassociated Members', 'item_url': '/members/unassociated'},
    ]},
    {'menu_title': 'Titles',    'menu_url': '/titles',      'menu_items': [
        {'item_title': 'Changes', 'item_url': '/titles/changes'},
    ]},
    {'menu_title': 'Roles',     'menu_url': '/roles',       'menu_items': role_types},
    {'menu_title': 'Assets',    'menu_url': '/assets',      'menu_items': [
        {'item_title': 'Changes', 'item_url': '/assets/changes'},
    ]},
    {'menu_title': 'Players',   'menu_url': '/players',     'menu_items': []},
]
