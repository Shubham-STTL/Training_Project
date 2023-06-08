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
    prescription_detail = fields.One2many('hospital.patient.line', 'hospital_main_line')
    patient_detail = fields.One2many('hospital.patient', 'hospital_id')