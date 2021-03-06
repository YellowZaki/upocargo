# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargotransporte(models.Model):
    _name = 'upocargo.upocargotransporte'

    tipo_vehiculo = fields.Selection([('trailer','Tráiler'),('camion','Camión'),('furgoneta','Furgoneta')],'Tipo de vehículo')
    matricula = fields.Char('Matrícula', size=7, required=True)
    capacidad_metros_cubicos = fields.Integer('Capacidad (en metros cúbicos)', default=1)

    upocargoservicio_ids = fields.Many2many('upocargo.upocargoservicio', string='Servicios')
    
    
    _sql_constraints = [('upocargo_unique_matricula','UNIQUE (matricula)','La matrícula debe ser única')]
    
      
      
      
    #Error si se intenta establecer metros cúbicos <= 0
    @api.onchange('capacidad_metros_cubicos')
    def onchange_capacidad_metros_cubicos(self):
        resultado = {}
        if self.capacidad_metros_cubicos <= 0:
            resultado = {'value': {'capacidad_metros_cubicos' : 1 },
                         'warning': {'title': 'Valores incorrectos',
                                     'message': 'Los metros cúbicos deben ser mayor o igual que 1'}}
        return resultado
    
    