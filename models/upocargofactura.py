# -*- coding: utf-8 -*-

from odoo import models, fields

class upocargofactura(models.Model):
    _name = 'upocargo.upocargofactura'
    
    pagada = fields.Binary('Pagada')
    fecha = fields.Datetime('Fecha',required=True, autodate = True)
    metodopago = fields.Char('Metodo de pago', size=64, required=True)
    id = fields.Char('ID', size=9, required=True)
    
    upocargomudanza_ids =  fields.One2many('upocargo.upocargomudanza', 'upocargoempleado_id', 'Mudanzas')  
    upocargoguardamueble_ids =  fields.One2many('upocargo.upocargoguardamueble', 'upocargoempleado_id', 'Guardamuebles')
    
    _sql_constraints = [('upocargo_unique_id_factura','UNIQUE (ID)','El ID de la factura debe ser único')]
