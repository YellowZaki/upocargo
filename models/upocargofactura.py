# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime


class upocargofactura(models.Model):
    _name = 'upocargo.upocargofactura'

    fecha_creacion = fields.Datetime('Fecha de creación',required=True, autodate = True)
    fecha_limite = fields.Datetime(compute='_fechaLimit', string='Fecha límite', store=True)
    fecha_pago = fields.Datetime('Fecha de pago')
    upocargomudanza_ids = fields.One2many('upocargo.upocargomudanza', 'upocargofactura_id', 'Servicios de mudanza')  
    upocargoguardamueble_ids = fields.One2many('upocargo.upocargoguardamueble', 'upocargofactura_id', 'Servicios de guardamueble')  
    state = fields.Selection([('creada','Creada'),
                              ('pagada','Pagada'),
                              ('cancelada','Cancelada'),
                              ('atrasada','Atrasada'),],
                              'Estado',
                              default='creada')  
    
    
    
    @api.one
    def btn_pagarFactura(self):
        for mudanza in self.upocargomudanza_ids:
            mudanza.state = 'pagado'
        for guardamueble in self.upocargoguardamueble_ids:
            guardamueble.state = 'pagado'
        now = fields.datetime.now()   
        if now > datetime.strptime(self.fecha_limite, "%Y-%m-%d %H:%M:%S") :
            self.state = 'atrasada' 
        else:
            self.state = 'pagada' 
        self.fecha_pago = now
        
    #Cuando se agregue la fecha creacion, se autocalcula la límite (1 mes)                                      
    @api.one
    @api.depends('fecha_creacion')
    def _fechaLimit(self):
        if self.fecha_creacion:
            date = datetime.strptime(self.fecha_creacion, "%Y-%m-%d %H:%M:%S") 
            self.fecha_limite = date + relativedelta(days =+ 30)