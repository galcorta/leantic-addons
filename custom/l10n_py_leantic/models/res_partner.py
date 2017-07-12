# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    bussines_name = fields.Char('Bussines name')
    fiscal_stamp_ids = fields.One2many('account.fiscal.stamp', 'partner_id', 'Fiscal stamps')
