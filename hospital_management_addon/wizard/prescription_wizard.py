from odoo import api, fields, models



class PrescriptionWizard(models.TransientModel):
    _name = "prescription.wizard"
    _description = "precription wizard description"

    patient_id = fields.Many2one('hospital.patient')
    prescription_text = fields.Char('prescription')
    appointment_date = fields.Date('appointment date')
    note = fields.Text("Note")


    def save_prescription(self):
        for i in self:
            attachment = self.env['hospital.patient.line'].create({
                        'prescription': i.prescription_text,
                        'appointment_date': i.appointment_date,
                        'patient_id': self.patient_id.id,
                        'note': i.note,
                        'hospital_main_line': self.patient_id.hospital_id.id,
                        
                    })