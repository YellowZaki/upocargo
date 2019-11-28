# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargoguardamueble(models.Model):
    _name = 'upocargo.upocargoguardamueble'
    _inherit = 'upocargo.upocargoservicio'
   
    fecha_deposito = fields.Datetime('Fecha del depósito',required=True, autodate = True)
    fecha_recogida = fields.Datetime('Fecha de recogida',required=True, autodate = True)