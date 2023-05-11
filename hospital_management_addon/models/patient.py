from datetime import datetime, timedelta, date
from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    

    name = fields.Char(string="Name")
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age")#, compute='_compute_age')#tracking=True #need to understand tracking #store=True  #to store the computed data
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string = 'Gender')
    reference = fields.Char(string="Reference")
    hospital_id = fields.Many2one('hospital.main', string="Hospital")

"""
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
"""