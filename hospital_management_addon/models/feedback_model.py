from odoo import api, fields, models


class FeedbackHospital(models.Model):
    _name = "feedback.hospital"
    _description = "Feedback Hospital"

    name = fields.Char(string="Name", required=True)
    hospital_name = fields.Char(string="Hospital Name", required=True)
    email_id = fields.Char(string="Email Id", required=True)
    note = fields.Text(string="Note", required=True)
    phone_number = fields.Char(string="Phone", required=True)
    #patient_id = fields.Many2one('hospital.patient')
    #hospital_id =  fields.Many2one('hospital.main', string="Hospital")