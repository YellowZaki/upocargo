# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargobien(models.Model):
    _name = 'upocargo.upocargobien'

    name = fields.Char('Nombre', size=64, required=True)

    metros_cubicos = fields.Float('Metros cúbicos', size=64, required=True)
    tipo = fields.Selection([('mueble','Mueble'),('electrodomestico','Electrodomestico'),('animal','Animal')],'Tipo de bien')
    upocargoservicio_ids =  fields.Many2many('upocargo.upocargoservicio',string='Servicios')  

