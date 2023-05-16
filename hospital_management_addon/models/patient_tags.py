from datetime import datetime, timedelta, date
from odoo import api, fields, models
from datetime import date




class PatientTags(models.Model):
    _name = "patient.tags"
    _description = "Patient Tags"
    
    name = fields.Char(string="Name")
    active = fields.Boolean(string="Active", default=True)
    