# -*- coding: utf-8 -*-
from odoo import http

# class NebizProductLabels(http.Controller):
#     @http.route('/nebiz_product_labels/nebiz_product_labels/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nebiz_product_labels/nebiz_product_labels/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nebiz_product_labels.listing', {
#             'root': '/nebiz_product_labels/nebiz_product_labels',
#             'objects': http.request.env['nebiz_product_labels.nebiz_product_labels'].search([]),
#         })

#     @http.route('/nebiz_product_labels/nebiz_product_labels/objects/<model("nebiz_product_labels.nebiz_product_labels"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nebiz_product_labels.object', {
#             'object': obj
#         })