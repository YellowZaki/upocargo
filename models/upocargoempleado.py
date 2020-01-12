# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargoempleado(models.Model):
    _name = 'upocargo.upocargoempleado'

    DNI = fields.Char('DNI', size=9, required=True)
    name = fields.Char('Nombre', size=64, required=True)
    puesto = fields.Selection([('encargado','Encargado'),('conductor','Conductor'),('operario','Operario')],'Puesto')
    avatar = fields.Binary('Avatar')
    upocargomudanza_ids =  fields.Many2many('upocargo.upocargomudanza', string='Mudanzas')  
    upocargoguardamueble_ids =  fields.Many2many('upocargo.upocargoguardamueble', string='Guardamuebles')
    
    _sql_constraints = [('upocargo_unique_dni_empleado','UNIQUE (DNI)','El DNI del empleado debe ser único')]
