# -*- coding: utf-8 -*-
# (c) 2017 Guido Alcorta - Leantic
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields, api


class Partner(models.Model):
    _inherit = "res.partner"

    device_water_meters = fields.One2many(
        string='Water Meters', comodel_name='device.water.meter',
        inverse_name='holder_partner')

    water_meters_count = fields.Integer(
        compute='_compute_water_meter_count', string='Water Meters')

    @api.multi
    @api.depends('device_water_meters')
    def _compute_water_meter_count(self):
        for partner in self:
            partner.water_meters_count = len(partner.device_water_meters)
