from plone.app.layout.viewlets import ViewletBase
from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class IconifiedDocumentActionsViewlet(ViewletBase):
    def update(self):
        super(IconifiedDocumentActionsViewlet, self).update()

        self.context_state = getMultiAdapter((self.context, self.request),
                                             name=u'plone_context_state')
        self.actions = self.context_state.actions().get('document_actions', None)

    index = ViewPageTemplateFile("iconified_document_actions.pt")
