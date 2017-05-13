# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    city_id = fields.Many2one(related='partner_id.city_id')
