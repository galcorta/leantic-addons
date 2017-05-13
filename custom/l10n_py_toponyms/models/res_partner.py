# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one('res.country.state.city', string='City', ondelete='restrict')

    # @api.multi
    # def onchange_city(self, city_id):
    #     if city_id:
    #         city = self.env['res.country.state.city'].browse(city_id)
    #         return {'value': {'state_id': city.state_id.id}}
    #     return {}

    @api.onchange('state_id')
    def _onchange_state_id(self):
        if self.state_id:
            return {'domain': {'city_id': [('state_id', '=', self.state_id.id)]}}
        else:
            return {'domain': {'city_id': []}}
