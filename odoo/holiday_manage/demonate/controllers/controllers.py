# -*- coding: utf-8 -*-
from openerp import http

# class Demonate(http.Controller):
#     @http.route('/demonate/demonate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demonate/demonate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demonate.listing', {
#             'root': '/demonate/demonate',
#             'objects': http.request.env['demonate.demonate'].search([]),
#         })

#     @http.route('/demonate/demonate/objects/<model("demonate.demonate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demonate.object', {
#             'object': obj
#         })