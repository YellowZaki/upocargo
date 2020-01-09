# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargoalmacen(models.Model):
    _name = 'upocargo.upocargoalmacen'

    name = fields.Char('Nombre', size=64, required=True)

    capacidad_metros_cubicos = fields.Integer('Capacidad (en metros cúbicos)', default=1)
    
    direccion = fields.Char('Dirección', size=64, required=True)

    upocargoguardamueble_ids = fields.One2many('upocargo.upocargoguardamueble', 'upocargoalmacen_id', 'Servicio')
    
    
    
      
    #Error si se intenta establecer metros cúbicos <= 0
    @api.onchange('capacidad_metros_cubicos')
    def onchange_capacidad_metros_cubicos(self):
        resultado = {}
        if self.capacidad_metros_cubicos <= 0:
            resultado = {'value': {'capacidad_metros_cubicos' : 1 },
                         'warning': {'title': 'Valores incorrectos',
                                     'message': 'Los metros cúbicos deben ser mayor o igual que 1'}}
        return resultado