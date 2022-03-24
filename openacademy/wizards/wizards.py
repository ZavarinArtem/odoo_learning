from odoo import models, fields, api

class AttendeesRegistrationWizard(models.TransientModel):

    _name = 'openacademy.wizard'
    _description = 'Wizard to add attendees to sessions'

    def _get_default_session(self):
        return self._context.get('active_ids')

    session_ids = fields.Many2many(comodel_name='openacademy.session',
                                   string='Session',
                                   required=True,
                                   default=_get_default_session)
    attendee_ids = fields.Many2many(comodel_name='res.partner', string='Attendees')

    def add_attendees(self):
        for session in self.session_ids:
            session.attendee_ids = self.attendee_ids
