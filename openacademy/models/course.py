# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Academy courses'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one(comodel_name='res.users', string='Responsible')
    sessions_ids = fields.One2many(comodel_name='openacademy.session', inverse_name='course_id', string='Sessions')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Course name must be unique'),
        ('name_desc_differ', 'CHECK(name <> description)', 'Name and description must differ')
    ]

    def copy(self, default=None):
        self.ensure_one()
        default = {'name': self.name + ' (copy)'}
        return super().copy(default)
