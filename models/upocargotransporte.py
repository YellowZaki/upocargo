# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargotransporte(models.Model):
    _name = 'upocargo.upocargotransporte'

    #DNI = fields.Char('DNI', size=9, required=True)
    #name = fields.Char('Nombre', size=64, required=True)
    #apellidos = fields.Char('Apellidos', size=64, required=True)
    #ciudad = fields.Char('Ciudad', size =32, required=True)
    #direccion = fields.Char('Direccion', size=128, required=True)
    #avatar = fields.Binary('Avatar')
    #upocargomudanza_ids =  fields.One2many('upocargo.upocargomudanza', 'upocargocliente_id', 'Mudanzas')  
    #upocargoguardamueble_ids =  fields.One2many('upocargo.upocargoguardamueble', 'upocargocliente_id', 'Guardamuebles')
    tipo_vehiculo = fields.Selection([('trailer','Tráiler'),('camion','Camión'),('furgoneta','Furgoneta')],'Tipo de vehículo')
    matricula = fields.Char('Matrícula', size=7, required=True)
    capacidad_metros_cubicos = fields.Integer('Capacidad (en metros cúbicos)')

    upocargoservicio_id = fields.Many2one('upocargo_upocargoservicio', 'Servicio')
    
      #upocargomudanza_id = fields.Many2one('upocargo_upocargoservicio')
      #upocargoguarda_id = fields.Many2one('upocargo_upocargoservicio')