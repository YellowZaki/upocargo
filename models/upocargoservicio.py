# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargoservicio(models.Model):
    _name = 'upocargo.upocargoservicio'

    name = fields.Char('Nombre', size=64, required=True)
    precio = fields.Float('Precio', (3, 2))
     
    upocargocliente_id = fields.Many2one('upocargo.upocargocliente', 'Cliente')   
    
    upocargobien_ids =  fields.Many2many('upocargo.upocargobien',string='Bienes') 
    
    upocargotransporte_ids = fields.One2many('upocargo.upocargotransporte', 'upocargoservicio_id', 'Transportes')
                                             
                                            # fields.One2many('upocargo.upocargomudanza', 'upocargocliente_id', 'Mudanzas')  )