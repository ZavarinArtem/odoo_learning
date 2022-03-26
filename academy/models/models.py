# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teachers(models.Model):

    _name = 'academy.teachers'
    _description = 'Teachers'

    name = fields.Char(string="Name")
    biography = fields.Html()
