# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import senaite.impress.templates


class SenaiteImpressTemplatesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=senaite.impress.templates)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'senaite.impress.templates:default')


SENAITE_IMPRESS_TEMPLATES_FIXTURE = SenaiteImpressTemplatesLayer()


SENAITE_IMPRESS_TEMPLATES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SENAITE_IMPRESS_TEMPLATES_FIXTURE,),
    name='SenaiteImpressTemplatesLayer:IntegrationTesting',
)


SENAITE_IMPRESS_TEMPLATES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SENAITE_IMPRESS_TEMPLATES_FIXTURE,),
    name='SenaiteImpressTemplatesLayer:FunctionalTesting',
)


SENAITE_IMPRESS_TEMPLATES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SENAITE_IMPRESS_TEMPLATES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SenaiteImpressTemplatesLayer:AcceptanceTesting',
)
