from odoo import http
from odoo.http import request
from werkzeug.utils import redirect


class Feedback(http.Controller):

    @http.route('/hospital/feedback/', auth="public", website=True)
    def feedback_controller(self, **kwargs):
        print("EXECUTUGBGG 10")
        hospitals = request.env['hospital.main'].search([])
        return request.render('hospital_management_addon.feedback_template', {'hospital_names': hospitals})


    @http.route('/create/feedback/', auth="public", website=True)
    def create_feedback(self, **kwargs):
        #feedback = request.env['feedback.hospital'].sudo().search([])
        record = request.env['feedback.hospital'].create(kwargs)
        return request.render('hospital_management_addon.feedback_success_template', {})


    # @http.route('/hospital/success/', website=True, csrf=False , auth='public')
    # def success_template(self, **kwargs):
    #     print("EXECUTING SUCCESS PAGE!!!")
    #     return request.render('hospital_management_addon.feedback_success_page', {}) # {'feedback': feedback})

"""
    @http.route('/hospital/feedback/success/', website=True, auth='public')
    def feedback_success_controller(self, **kwargs):
        return request.render('hospital_management_addon.feedback_success_template')
"""