# -*- coding: utf-8 -*-
from datetime import date
from odoo import fields, api, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Health Care"
    _rec_name = 'patient_id'
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    ref = fields.Char(string='Reference', help="reference of the patient")
    doctor = fields.Char(string='Doctor Name')
    depart = fields.Char(string='Dept')
    gender = fields.Selection(related='patient_id.gender')
    Phone = fields.Char(related='patient_id.Phone')
    date_of_birth = fields.Date(string="Brith Date")
    prescription = fields.Html(string="Prescription")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'low'),
        ('2', 'High'),
        ('3', 'Very high')], string="priority")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Canceled')], defualt='draft', string="status")
    doctor_id = fields.Many2one('res.users', string='Doctor')
    pharmacy_lines_ids = fields.One2many('appointment.pharmacy.lines','appointment_id',string='Pharmacy Lines')

    @api.depends('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    def action_test(self):
        print("Button clicked success")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Object Click success',
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = "Appointment pharmacy lines"
    product_id = fields.Many2one('product.product')
    price_unit = fields.Float(string = 'Price')
    qty = fields.Integer(string = 'Quantity')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')