from odoo import api,fields,models,_  # underscore is for language translator based on user defined
from odoo.exceptions import ValidationError, UserError
from datetime import datetime

class HospitalManagement(models.Model):
    _name = "sd.patient"  # Also this is the name of model in UI
    _description = "Patient Records"
    _inherit = "mail.thread"  # we can confirm this will add or not by checking settings/technical/fields or models the mail.thread also included here

    name = fields.Char(string='Patient Name' , required= True, tracking=True)
    age =fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('Male','Male'),('Female','Female'),('others','others')],string='Gender', required=True, tracking=True)
    is_child = fields.Boolean(string="Is child?" , tracking=True)
    doctor = fields.Selection(string='Doctor name', selection='_get_doctor_name')
    partner = fields.Many2one('res.partner', string="Partner name")
    partner_many = fields.Many2many('res.partner', "sd_hospital_pt_many","patient_reg_id","patient_name", string="Many 2 many")
    invoice_date = fields.Text(string="code")

    def _get_doctor_name(self):
        doctors = self.env['res.partner'].search([])
        # Fetch values from 'hospital.patient' and create a list of tuples for Selection field
        return [(record.id, record.name) for record in doctors if record.name]
    @api.model   #  if we try to use api.model_creat_multi decortor then sequence generator index true and logic not works
    def create(self, vals_list):
        vals_list['sequence_number'] = self.env['ir.sequence'].next_by_code('sd.patient')
        return super(HospitalManagement,self).create(vals_list)

    sequence_number = fields.Char(string='Sequence Number', index=True, readonly=True)

    def _compute_current_time(self):
        return fields.datetime.now().strftime("%H:%M:%S")

    time = fields.Text(string="Current Time", default=_compute_current_time, store=True, readonly=True)


    @api.onchange('age')    # this decorator helps to call function ..here when name changed this func will call
    def onchange_patient_id(self):
        for rec in self:
            if rec.is_child and rec.age >= 10:
                raise ValidationError(_("Child age limit exceeded"))

class AccountMoveInherit(models.Model):
   _inherit = 'account.move'

   def action_update_invoice_date(self):
       self.write({'invoice_date': fields.Date.today()})