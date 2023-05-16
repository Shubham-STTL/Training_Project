from datetime import datetime, timedelta, date
from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    

    name = fields.Char(string="Name")
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute='_compute_age')#tracking=True #need to understand tracking #store=True  #to store the computed data
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string = 'Gender')
    hospital_id = fields.Many2one('hospital.main', string="Hospital")
    active = fields.Boolean(string="Active", default=True)
    tag_ids = fields.Many2many('patient.tags', string="Tags")
    total = fields.Float(string="Total Float Example")
    reference = fields.Text(string="Reference")
    patient_line_ids = fields.One2many('hospital.patient.line', 'hospital_patient_id', string="Patient Lines")

 
    @api.depends('dob')
    def _compute_age(self):
        print(self, "self")
        today = date.today()
        for rec in self:
            if rec.dob:
                print(today.year, rec.dob, rec.dob.year, "if condition")
                rec.age = today.year - rec.dob.year
            else:
                print('else condition')
                rec.age = 0
            return rec.age

class HospitalPatientLine(models.Model):
    _name = "hospital.patient.line"
    _description = "Hospital Patient Line"

    name = fields.Char('name')
    age = fields.Integer('Age')
    city = fields.Char('City')
    hospital_patient_id = fields.Many2one('hospital.patient')