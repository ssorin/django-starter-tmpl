from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class MDPToolbar(CMSToolbar):

    def populate(self):
        menu = self.toolbar.get_or_create_menu('user', 'Utilisateur')
        url = "/admin/password_change/"
        menu.add_sideframe_item(_('Changer de mot de passe'), url=url)

@toolbar_pool.register
class FilerToolbar(CMSToolbar):

    def populate(self):
        menu = self.toolbar.get_or_create_menu('filer', _('Medias'))
        url = reverse('admin:filer-directory_listing-root')
        menu.add_sideframe_item(_('Folder'), url=url)

