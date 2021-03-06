# coding=utf-8
"""Example URLConf for a contact form.

If all you want is the basic ContactForm with default behavior, just
include this URLConf somewhere in your URL hierarchy (for example, at
``/contact/``)>
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ContactFormView


urlpatterns = [
    url(r'^$',
        ContactFormView.as_view(),
        name='contact_form'),
    url(r'^sent/$',
        TemplateView.as_view(
            template_name='contact_form/contact_form_sent.html'),
        name='contact_form_sent'),
]
