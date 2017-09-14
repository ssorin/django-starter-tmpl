from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AnonymousUser

from cms.utils.urlutils import add_url_parameters, admin_reverse
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils import page_permissions
from cms.models import CMSPlugin, Title, Page
from cms.api import get_page_draft, can_change_page

@toolbar_pool.register
class UserToolbar(CMSToolbar):

    def get_username(self, user=None, default=''):
        user = user or self.request.user
        try:
            name = user.get_full_name()
            if name:
                return name
            else:
                return user.get_username()
        except (AttributeError, NotImplementedError):
            return default

    def populate(self):

        user_name = self.get_username()
        user_menu_text = _('User') + ' (%s)' % user_name if user_name else _('User')
        logout_menu_text = _('Logout %s') % user_name if user_name else _('Logout')

        menu = self.toolbar.get_or_create_menu('user', user_menu_text)
        menu.add_sideframe_item(_('Password change'), url=admin_reverse('password_change'))
        menu.add_sideframe_item(_('User settings'), url=admin_reverse('cms_usersettings_change'))

        menu.add_break()
        self.page = get_page_draft(self.request.current_page)
        if (self.page and self.page.is_published(self.current_lang) and not self.page.login_required and
                page_permissions.user_can_view_page(AnonymousUser(), page=self.page)):
            on_success = self.toolbar.REFRESH_PAGE
        else:
            on_success = '/'

        menu.add_ajax_item(logout_menu_text, action=admin_reverse('logout'), active=True, on_success=on_success)


@toolbar_pool.register
class FilerToolbar(CMSToolbar):

    def populate(self):
        menu = self.toolbar.get_or_create_menu('filer', _('Medias'))
        menu.add_sideframe_item(_('Folder'), url=admin_reverse('filer-directory_listing-root'))

