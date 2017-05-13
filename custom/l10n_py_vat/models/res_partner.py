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


class ResPartner(models.Model):
    _inherit = "res.partner"

    business_name = fields.Char('Business name')

    def check_vat_py(self, vat):
        ruc = ''
        basemax = 11
        for c in str(vat).replace('-', ''):
            ruc += c.isdigit() and c or str(ord(c))
        k = 2
        total = 0
        for c in reversed(ruc[:-1]):
            n = int(c)
            if n > basemax:
                k = 2
            total += n * k
            k += 1
        resto = total % basemax
        if resto > 1:
            n = basemax - resto
        else:
            n = 0
        return n == int(ruc[-1])