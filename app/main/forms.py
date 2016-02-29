# -*- coding: utf-8; -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, DateField, DateTimeField
from wtforms.validators import Required, Length, Regexp, EqualTo



class QueryForm(Form):

    shipper = StringField(u'Грузоотправитель ( ФИО или название организации) контактные тел.', validators=[Required()])
    place = StringField(u'Место загрузки')
    #date = DateField(u'Дата загрузки', format='%Y-%m-%d')
    #time = DateTimeField(u'Время загрузки')
    contact_face_in = StringField(u'Контактное лицо на погрузке, тел.')
    place_in = StringField(u'Место затаможки')
    custom_way = StringField(u'Погран переход')
    place_out = StringField(u'Место выгрузки')
    contact_face_out = StringField(u'Контактное лицо на выгрузке, тел.')
    cargo_info = StringField(u'Информация о грузе')
    cargo_name = StringField(u'Наименование груза')
    weight = StringField(u'Весгруза')
    volume = StringField(u'Объем груза')
    for_m_cargo = StringField(u'Для сборных грузов: точные размеры или длина по полу')
    type = StringField(u'Тип подвижного соства')
    count = StringField(u'Количество подвижного соства')
    add_cond = StringField(u'Дополнительные условия')
    contact_info = StringField(u'Ваша контактная иформация для обратной связи')
    submit = SubmitField(u'Отправить запрос')




