# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

DRAFT = 'draft'
FINISHED = 'finished'

STATUS = (
    (DRAFT, _('Draft')),
    (FINISHED, _('Finished')),
)
