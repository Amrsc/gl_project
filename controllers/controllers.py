# -*- coding: utf-8 -*-
# from odoo import http


# class Snop(http.Controller):
#     @http.route('/snop/snop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/snop/snop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('snop.listing', {
#             'root': '/snop/snop',
#             'objects': http.request.env['snop.snop'].search([]),
#         })

#     @http.route('/snop/snop/objects/<model("snop.snop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('snop.object', {
#             'object': obj
#         })
