# -*- coding: utf-8 -*-
# from odoo import http


# class ThemeTest(http.Controller):
#     @http.route('/theme_test/theme_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_test/theme_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_test.listing', {
#             'root': '/theme_test/theme_test',
#             'objects': http.request.env['theme_test.theme_test'].search([]),
#         })

#     @http.route('/theme_test/theme_test/objects/<model("theme_test.theme_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_test.object', {
#             'object': obj
#         })
