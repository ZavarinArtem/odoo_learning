# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teachers(models.Model):

    _name = 'academy.teachers'
    _description = 'Teachers'

    name = fields.Char(string="Name")
    biography = fields.Html()

    course_ids = fields.One2many(comodel_name='academy.courses', inverse_name='teacher_id', string='Courses')


class Courses(models.Model):
    _name = 'academy.courses'
    _description = 'Courses'
    _inherit = 'mail.thread'

    name = fields.Char()
    teacher_id = fields.Many2one(comodel_name='academy.teachers', string='Teacher')

