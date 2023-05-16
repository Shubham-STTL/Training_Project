from odoo import api, fields, models




class Appointment(models.Model):
    _name = "hospital.main"
    _description = "Hospital Main"

    name = fields.Char(string="Name")
    address = fields.Text(string="Address")
    contact_no = fields.Char(string="Phone")