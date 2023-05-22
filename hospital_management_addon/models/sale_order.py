from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    inherited_name = fields.Char(string="Inherited Name")
    inherited_sale_contact_ids = fields.One2many('contact.info', 'contact_id', string="Sale Contact Ids Inherited")
    state = fields.Selection(selection_add=[
        ('TEST_state', 'TEST_state'),], string='Custom Status', readonly=True, copy=False, index=True, tracking=3, default='TEST_ state')
    
    
class ContactInfo(models.Model):
    _name = "contact.info"
    _description = "Inherited Contact Info"

    contact_id = fields.Many2one('sale.order')
    inherited_note = fields.Text(string='Notes')



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    inherited_rejected_quantity = fields.Integer(string="Inherited rejected quantity")
    
    

    
    