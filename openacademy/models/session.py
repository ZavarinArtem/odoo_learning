
from datetime import timedelta, date
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Session(models.Model):

    _name = 'openacademy.session'
    _description = 'Course sessions'

    name = fields.Char(string='Title', required=True)
    active = fields.Boolean(string="Active", default=True)
    course_id = fields.Many2one(comodel_name='openacademy.course', string='Course', required=True)
    instructor_id = fields.Many2one(comodel_name='res.partner',
                                 string='Instructor',
                                 domain="""["|", 
                                                ('instructor', '=', 'True'),
                                                '&',
                                                    ('category_id.parent_id.name', '=like', 'Teacher'),
                                                    ('category_id.name', '=like', 'Level _')]""")
    start_date = fields.Date(string='Start date', default=date.today())
    duration = fields.Integer(string='Duration', help='Session duration in days')
    seats_number = fields.Integer(string='Number of seats')
    pers_of_taken_seats = fields.Float(string='% taken', compute='_compute_pers_of_taken_seats')
    attendee_ids = fields.Many2many(comodel_name='res.partner', string='Attendees')

    attendees_count = fields.Integer(string='Attendees count', compute='_get_attendees_count', store=True)
    end_date = fields.Date(string="End Date", store=True,
                           compute='_get_end_date')
    color = fields.Integer()

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for rec in self:
            rec.attendees_count = len(rec.attendee_ids)

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for rec in self:
            if not rec.duration:
                rec.end_date = rec.start_date
                continue

            rec.end_date = rec.start_date + timedelta(days=rec.duration, seconds=-1)

    @api.depends('seats_number', 'attendee_ids')
    def _compute_pers_of_taken_seats(self):
        for rec in self:
            rec.pers_of_taken_seats = 0 if rec.seats_number == 0 \
                else len(rec.attendee_ids) / float(rec.seats_number) * 100

    @api.onchange('seats_number')
    def _onchange_seats_number(self):
        if self.seats_number <0:
            self.seats_number = 0
            return {
                'warning':
                    {
                        'title': 'Wrong number of seats',
                        'message': 'Number of seats must be a positive number'
                    }
            }

    @api.onchange('attendee_ids')
    def _onchange_attendees(self):
        if len(self.attendee_ids) > self.seats_number:
            return {
                'warning':
                    {
                        'title': 'All seats taken',
                        'message': 'All seats in auditory have been taken'
                    }
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for rec in self:
            if len(rec.instructor_id) > 0 and rec.instructor_id in rec.attendee_ids:
                raise ValidationError('Instructor can not be among attendee_ids')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Instructor')
    sessions_ids = fields.One2many(comodel_name='openacademy.session',
                                   inverse_name='instructor_id',
                                   string='Open Academy sessions')
