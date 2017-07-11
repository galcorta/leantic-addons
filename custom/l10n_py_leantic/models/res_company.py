# -*- coding: utf-8 -*-
##############################################################################
#
#    Leantic S.A., Open Source Management Solution
#    Copyright (C) 2017-TODAY Leantic S.A. (<http://leantic.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    fantasy_name = fields.Char(related='partner_id.fantasy_name')

    fiscal_stamp_ids = fields.One2many('account.fiscal.stamp',
                                       string='Fiscal stamps',
                                       related='partner_id.fiscal_stamp_ids')
    is_branch = fields.Boolean('Is a Branch?')

