# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargocliente(models.Model):
    _name = 'upocargo.upocargocliente'

    DNI = fields.Char('DNI', size=9, required=True),
    name = fields.Char('Nombre', size=64, required=True),
    apellidos = fields.Char('Apellidos', size=64, required=True),
    direccion = fields.Char('Direccion', size=128, required=True)
    upocargoservicio_ids =  fields.One2many('upocargo.upocargoservicio','Servicios')  

