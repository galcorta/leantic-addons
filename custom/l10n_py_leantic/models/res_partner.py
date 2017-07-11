# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    fantasy_name = fields.Char('Fantasy name')
    fiscal_stamp_ids = fields.One2many('account.fiscal.stamp', 'partner_id', 'Fiscal stamps')

