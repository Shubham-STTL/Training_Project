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
    tag_total = fields.Integer(string='tag_total')
    total = fields.Float(string="Total Float Example")
    reference = fields.Text(string="Reference")
    patient_line_ids = fields.One2many('hospital.patient.line', 'patient_id', string="Patient Lines")
    color = fields.Integer(string="color")

    @api.model
    def create(self, vals):
        res = super(HospitalPatient, self.with_context()).create(vals)
        if res.age >= 15:
            print('Valid age')
        #print('\n\n\t\t\t   ---   RES  ---    ', res)
        ##print('\n\n\t\t\t   ---   vals  ---    ', vals)
        #print('\n\n\t\t\t   ---   patient_line_ids  ---    ', res.patient_line_ids)
        
        return res
    
    #@api.model        
    def custom_unlink(self):
        tags_list = self.env['hospital.patient'].search([('reference', '=', False)]) 
        print(tags_list, 'tags_list, ')
        tags_list.unlink()
        
        
        
    
    #@api.model
    def write(self, vals):
        #print("WRITE EXEUCTING ")
        #print('\t\t -- vals --- ', vals, 'vals')
        #print('\t\t -- dir(vals) --- ', dir(vals), 'dir(vals)')
        #list1 = vals.get('tag_ids')[0][2]
        print(vals, "vals")
        if vals.get('tag_ids'):
            values = list(vals.get('tag_ids'))
            print(values, 'values')
            values_list = values[0][2]
            tags_list = self.env['patient.tags'].search([('id', 'in', values_list)]) 
            list_number = tags_list.mapped('number')
            vals['tag_total'] = sum(list_number)
            res = super(HospitalPatient, self.with_context()).write(vals) # write method should be called any the end every time after making updated in vals dictionary        
        else:
            res = super(HospitalPatient, self.with_context()).write(vals)

    def test_orm(self):
        print("TEST ORM operations clicking")
        #to search all fetch all the data from hospital.patient
        search_method = self.env['hospital.patient'].search([])#.mapped('name')
        print(search_method, 'search_method')
        #get name field data from hospital.patient table that has been searched above
        mapped_method = search_method.mapped('name')
        print(mapped_method, 'mapped_method')
        #sorting by id
        sorted_method = search_method.sorted(lambda x: x.id)
        print(sorted_method, 'sorted_method')
        #sorting by write_date
        sorted_method_write_date = search_method.sorted(lambda x: x.write_date)
        print(sorted_method_write_date, 'sorted_method_write_date')
        #reverse the sorted data from write_date field
        sorted_method_write_date_reverse = search_method.sorted(lambda x: x.write_date, reverse=True)
        print(sorted_method_write_date_reverse, 'sorted_method_write_date_reverse')
        #filtered the data where active is True
        sorted_method_filtered  = search_method.filtered(lambda x: x.active)
        print(sorted_method_filtered, 'sorted_method_filtered')
        #browse searches from the list of ids
        #browse_method = self.env['hospital.patient'].browse([45, 25, 22])#.mapped('name')
        #print(browse_method, 'browse_method')
        """
        for i in browse_method:
            print(i.name)
        """
        #we can stack up mulitple field to search in a database
        search_method = self.env['hospital.patient'].search([('gender', '=', 'male'), ('age', '>', '100')])#.mapped('name')
        #search_all = self.env['hospital.patient'].search([])
        #filtered_example = search_all.filtered(lambda x: x.tag_total).read()    
        
        
        

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