# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class upocargoguardamueble(models.Model):
    _name = 'upocargo.upocargoguardamueble'
    _inherit = 'upocargo.upocargoservicio'
    fecha_deposito = fields.Datetime('Fecha del depósito',required=True, autodate = True)
    fecha_recogida = fields.Datetime('Fecha de recogida',required=True, autodate = True)
    upocargoalmacen_id = fields.Many2one('upocargo.upocargoalmacen','Almacen')
    
    
    
     #Una vez la factura está pagada/cancelada, ya no se puede editar
    @api.onchange('fecha_deposito','fecha_recogida','upocargoalmacen_id')
    def onchange_fieldsguardamueble(self):
        if self.state == 'pagado' or self.state == 'cancelado':
            raise models.ValidationError('No puedes editar los datos una vez el servicio está pagado o cancelado')  
        
        
     #Error si se intenta establecer fecha_recogida < fecha_deposito
    @api.onchange('fecha_deposito','fecha_recogida')
    def onchange_Fecha(self):
        if self.fecha_deposito and self.fecha_recogida:
            if datetime.strptime(self.fecha_recogida, "%Y-%m-%d %H:%M:%S") < datetime.strptime(self.fecha_deposito, "%Y-%m-%d %H:%M:%S"):
                raise models.ValidationError('La fecha de recogida debe ser posterior a la de depósito')  
            
            
    #Comprobar si hay capacidad necesaria en el almacen
    @api.one
    @api.constrains('upocargoalmacen_id','upocargobien_ids')
    def _checkMetrosCubicosAvailableForAlmacen(self):
        #Si aun no se le ha asignado ningun vehiculo, dejar pasar
        metros_cubicos_en_almacen = 0
        if self.upocargoalmacen_id:
            for guardamueble in self.upocargoalmacen_id.upocargoguardamueble_ids:
                metros_cubicos_en_almacen = metros_cubicos_en_almacen + guardamueble.metros_cubicos_usados
            if metros_cubicos_en_almacen > self.upocargoalmacen_id.capacidad_metros_cubicos:
                raise models.ValidationError('El almacén ha superado su capacidad máxima') 