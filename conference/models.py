# coding=utf-8
from __future__ import unicode_literals

from datetime import date

from django.db import models
from django.utils.encoding import smart_unicode


class Event(models.Model):
    class Meta:
        verbose_name_plural = 'Конференции'
        verbose_name = 'Конференция'

    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    text = models.TextField(verbose_name='Подробный текст')
    start = models.DateField(verbose_name='Дата Начала', default=date.today())
    finish = models.DateField(verbose_name='Дата Окончания', blank=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class Personal(models.Model):
    class Meta:
        verbose_name_plural = 'Спикеры'
        verbose_name = 'Спикер'

    conference = models.ForeignKey(Event, verbose_name='В какой конференции')
    name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=100, verbose_name='Позиция')
    image = models.ImageField(upload_to='personals/images', verbose_name='Фотография')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)
