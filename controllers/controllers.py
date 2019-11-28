# -*- coding: utf-8 -*-
from odoo import http

# class Upocargo(http.Controller):
#     @http.route('/upocargo/upocargo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upocargo/upocargo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upocargo.listing', {
#             'root': '/upocargo/upocargo',
#             'objects': http.request.env['upocargo.upocargo'].search([]),
#         })

#     @http.route('/upocargo/upocargo/objects/<model("upocargo.upocargo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upocargo.object', {
#             'object': obj
#         })