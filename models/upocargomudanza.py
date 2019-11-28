# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargomudanza(models.Model):
    _name = 'upocargo.upocargomudanza'
    _inherit = 'upocargo.upocargoservicio'
   
    fecha = fields.Datetime('Fecha',required=True, autodate = True)