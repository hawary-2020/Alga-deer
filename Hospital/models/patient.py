# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models


class Hospitalpatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Health Care"
    name = fields.Char(string='Name', tracking=True, required=True)
    date_of_birth = fields.Date(string="Brith Date")
    _rec_name = 'name'

    age = fields.Integer(string='Age', compute='_compute_age', tracking=True, )
    name = fields.Char(string='Doctor Name', tracking=True, required=True)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'low'),
        ('2', 'High'),
        ('3', 'Very high')], string="priority")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Canceled')], string="status")

    Phone = fields.Char(string='Phone Number')
    doctor_id = fields.Many2one('res.users',string='Doctor')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('kid', 'Kid')], required=True, string='Gender',
                              tracking=True)
    insurance = fields.Selection([('sudan health', 'Sudan Health'), ('blue health', 'Blue Health'), ], required=True,
                                 string='Insurance')
    depart = fields.Char(string='Dept')

    ref = fields.Char(string='Reference', help="reference of the patient")
    active = fields.Boolean(string="Archive", default=True)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointments")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0


class HospitalKids(models.Model):
    _name = 'hospital.kids'
    _description = "Health Care for kids"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Kid Name', tracking=True, required=True)
    # age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('kid', 'Kid')], required=True,
                            string='Gender', tracking=True)
    ref = fields.Char(string='Reference')

    doctor = fields.Char(string='Doctor Name')
    depart = fields.Char(string='Dept')
    insurance = fields.Selection([('sudan health', 'Sudan Health'), ('blue health', 'Blue Health'), ], required=True,
                                 string='Insurance')


class Hospitallaboratory(models.Model):e
    _name = 'hospital.laboratory'
    _description = "Blood Test"
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointments")
    active = fields.Boolean(string="Archive", default=True)
    situation = fields.Selection([('stable', 'Stable'), ('danger', 'Danger')], required=True, string='Situation')


depart = fields.Char(string='Dept')
insurance = fields.Selection([('sudan health', 'Sudan Health'), ('blue health', 'Blue Health'), ], required=True,
                             string='Insurance')


class Hospitaldoctors(models.Model):
    _name = 'hospital.doctors'
    _description = "Doctors Details"
    name = fields.Char(string='Doctor Name', tracking=True, required=True)
    age = fields.Integer(string='Doctor Age')
    phone = fields.Char(string='Phone Number')
    ref = fields.Char(string='Reference', help="reference of the doctor")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], required=True, string='Gender')
    department = fields.Char(string='Doctor Department')
