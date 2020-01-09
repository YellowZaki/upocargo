# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargobien(models.Model):
    _name = 'upocargo.upocargobien'

    name = fields.Char('Nombre', size=64, required=True)
    metros_cubicos = fields.Float('Metros cúbicos', size=64, required=True, default=1)
    tipo = fields.Selection([('mueble','Mueble'),('electrodomestico','Electrodomestico'),('animal','Animal')],'Tipo de bien')
    upocargoservicio_ids =  fields.Many2many('upocargo.upocargoservicio',string='Servicios')  




    #Error si se intenta establecer metros cúbicos <= 0
    @api.onchange('metros_cubicos')
    def onchange_metros_cubicos(self):
        resultado = {}
        if self.metros_cubicos <= 0:
            resultado = {'value': {'metros_cubicos' : 1 },
                         'warning': {'title': 'Valores incorrectos',
                                     'message': 'Los metros cúbicos deben ser mayor o igual que 1'}}
        return resultado