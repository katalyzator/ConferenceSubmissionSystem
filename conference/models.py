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
    image = models.ImageField(upload_to='conference/images', verbose_name='Картинка')

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


class Application(models.Model):
    class Meta:
        verbose_name_plural = 'Заявки на конференцию'
        verbose_name = 'Заявка на конференцию'

    conference = models.ForeignKey(Event, verbose_name='В какой конференции')
    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.CharField(max_length=255, verbose_name='Email')
    number = models.CharField(max_length=255, verbose_name='Номер Телефона')

    def __unicode__(self):
        return smart_unicode(self.name)


class Feedback(models.Model):
    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'

    title = models.CharField(max_length=255, verbose_name='Название конференции')
    person = models.CharField(max_length=255, verbose_name='ФИО')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='feedback/images', verbose_name='Фотография', blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)
