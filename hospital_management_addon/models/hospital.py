from odoo import api, fields, models




class HospitalMain(models.Model):
    _name = "hospital.main"
    _description = "Hospital Main"

    name = fields.Char(string="Name")
    address = fields.Text(string="Address")
    phone = fields.Char(string="Phone")
    city = fields.Char(string="City")
    email_id = fields.Char(string="Email")
    website = fields.Char(string="website")