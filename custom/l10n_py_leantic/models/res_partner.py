# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    business_name = fields.Char('Business name')
    fiscal_stamp_ids = fields.One2many('account.fiscal.stamp', 'partner_id', 'Fiscal stamps')

