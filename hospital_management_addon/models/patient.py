from datetime import datetime, timedelta, date
from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(compute='_compute_age', store=True, string="Age") #default=False#tracking=True #store=True  #to store the computed data
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string = 'Gender')
    hospital_id = fields.Many2one('hospital.main', string="Hospital")
    address_hospital_fetch = fields.Text("address fetch")#,readonly=True [readonly is to just display - to store remove read_only] 
    phone_hospital_fetch = fields.Text("phone fetch", readonly=True)
    active = fields.Boolean(string="Active", default=True)
    tag_ids = fields.Many2many('patient.tags', string="Tags")
    tag_total = fields.Integer()
    total = fields.Float(string="Total Float Example")
    reference = fields.Text(string="Reference")
    patient_line_ids = fields.One2many('hospital.patient.line', 'patient_id', string="Patient Lines")
    color = fields.Integer(string="color")

    @api.model
    def create(self, vals):
        res = super(HospitalPatient, self.with_context()).create(vals)
        if res.age >= 15:
            print('Valid age')
        print('\n\n\t\t\t   ---   RES  ---    ', res)
        print('\n\n\t\t\t   ---   vals  ---    ', vals)
        print('\n\n\t\t\t   ---   patient_line_ids  ---    ', res.patient_line_ids)
        
        return res
        
    @api.depends('dob')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 0

    @api.constrains('age') 
    def _constrains_age(self):
        for record in self:
            if record.age < 15:
                raise ValidationError("cannot submit if age is less than 15")

    @api.onchange('hospital_id')
    def _onchange_address(self):
        if self.hospital_id:
            self.address_hospital_fetch = self.hospital_id.address
            self.phone_hospital_fetch = self.hospital_id.phone
            


class HospitalPatientLine(models.Model):
    _name = "hospital.patient.line"
    _description = "Hospital Patient Line"

    patient_id = fields.Many2one('hospital.patient')
    appointment_date = fields.Date('appointment date')
    age = fields.Integer('Age')
    prescription = fields.Text("Prescription")
    note = fields.Char('note')