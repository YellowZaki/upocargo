# -*- coding: utf-8 -*-

from odoo import models, fields, api

class upocargoservicio(models.Model):
    _name = 'upocargo.upocargoservicio'

    name = fields.Char('Nombre', size=64, required=True)
    precio = fields.Float('Precio', (3, 2), default=1)
     
    upocargocliente_id = fields.Many2one('upocargo.upocargocliente', 'Cliente')   
    
    upocargoempleado_id = fields.Many2one('upocargo.upocargoempleado', 'Empleado')
    
    upocargobien_ids =  fields.Many2many('upocargo.upocargobien',string='Bienes') 
    
    upocargotransporte_ids = fields.Many2many('upocargo.upocargotransporte', string='Transportes')
    
    
    metros_cubicos_usados = fields.Integer(compute='_metrosCubicosUsados', string='Metros cúbicos usados', store=True, default=1)

                                             
                                           
                                            
    
    #Cuando se agregue/elimine un bien al servicio, se actualizará los metros cúbicos usados                                        
    @api.one
    @api.depends('upocargobien_ids')
    def _metrosCubicosUsados(self):
        metros_cubicos = 0
        for bien in self.upocargobien_ids:
            metros_cubicos = metros_cubicos + bien.metros_cubicos                        
        self.metros_cubicos_usados = metros_cubicos                      
        
        
        
    #Error si se intenta establecer precio <= 0
    @api.onchange('precio')
    def onchange_precio(self):
        resultado = {}
        if self.precio <= 0:
            resultado = {'value': {'precio' : 1 },
                         'warning': {'title': 'Valores incorrectos',
                                     'message': 'El precio debe ser mayor o igual que 1'}}
        return resultado               
    
    
    #Comprobar si hay capacidad necesaria para transportar
    @api.one
    @api.constrains('upocargotransporte_ids','upocargobien_ids')
    def _checkMetrosCubicosAvailableForTransporte(self):
        #Si aun no se le ha asignado ningun vehiculo, dejar pasar
        if len(self.upocargotransporte_ids) > 0:        
            capacidad_min = 999999999999999
            for transporte in self.upocargotransporte_ids:
                if transporte.capacidad_metros_cubicos < capacidad_min:
                    capacidad_min = transporte.capacidad_metros_cubicos
            if self.metros_cubicos_usados > capacidad_min:
                raise models.ValidationError('Todos los vehículos deben tener capacidad necesaria para transportar los bienes')      
        
        
        
        
        