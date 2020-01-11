# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargomudanza(models.Model):
    _name = 'upocargo.upocargomudanza'
    _inherit = 'upocargo.upocargoservicio'
   
    fecha = fields.Datetime('Fecha',required=True, autodate = True)
    
    
     #Una vez la factura está pagada/cancelada, ya no se puede editar
    @api.onchange('fecha')
    def onchange_fieldsmudanza(self):
        if self.state == 'pagado' or self.state == 'cancelado':
            raise models.ValidationError('No puedes editar los datos una vez el servicio está pagado o cancelado')  