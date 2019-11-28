# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargoservicio(models.Model):
    _name = 'upocargo.upocargoservicio'

    name = fields.Char('Nombre', size=64, required=True)
    precio = fields.Float('Precio', (3, 2))
    #upocargobien_ids =  fields.Many2many('upocargo.upocargobien','Bienes')  
    #upocargocliente_id = fields.Many2one('upocargo.upocargocliente', 'Cliente')    
    
    
