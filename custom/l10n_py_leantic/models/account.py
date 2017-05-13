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

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class FiscalStamp(models.Model):
    _name = 'account.fiscal.stamp'
    _order = 'due_date desc'

    @api.depends('number', 'due_date')
    def _is_valid(self):
        for fs in self:
            if fs.number and \
                    fs.due_date and \
                    fs.due_date >= fields.Date.context_today(self):
                fs.is_valid = True
            else:
                fs.is_valid = False

    number = fields.Char('Fiscal Stamp', required=True)
    name = fields.Char(string='Name', related='number')
    start_date = fields.Date('Start date', required=True)
    due_date = fields.Date('Due date', required=True)
    is_valid = fields.Boolean('Is valid?',
                              compute=_is_valid)
    partner_id = fields.Many2one('res.partner', 'Partner',
                                 ondelete='cascade',
                                 required=True)


class DispatchPoint(models.Model):
    _name = 'account.dispatch.point'

    name = fields.Char('Name', required=True)
    legal_id = fields.Char('Legal ID', size=3, default='001')
    company_id = fields.Many2one('res.company', 'Company',
                                 ondelete='cascade',
                                 required=True,
                                 default=lambda self: self.env.user.company_id.id)

    fiscal_stamp_id = fields.Many2one('account.fiscal.stamp', 'Fiscal stamp')
    sequence = fields.Many2one('ir.sequence', 'Invoice Sequence',
                               copy=False,
                               help="This sequence is automatically created by Odoo but you can change it " \
                                    "to customize the reference numbers of your dispatch points.")
    sequence_next = fields.Integer('Next value',
                                   related='sequence.number_next',
                                   readonly=True)
    usage = fields.Selection([
                    ('general', 'General'),
                    ('pos', 'Point of Sales')], 'Usage', required=True, default='general')

    _sql_constraints = [
        ('dispatch_point_legal_id_res_branch_uniq', 'unique (legal_id,company_id)',
         'The dispatch point legal ID must be unique per company!'),
        ('dispatch_point_name_company_uniq', 'unique (name,company_id)',
         'The dispatch point name must be unique per company!'),
    ]


# class DispatchPointFiscalStamp(models.Model):
#     _name = 'account.dispatch.point.account.fiscal.stamp.rel'
#
#     account_dispatch_point_id = fields.Many2one('account.dispatch.point')
#     account_fiscal_stamp_id = fields.Many2one('account.fiscal.stamp')
#     is_valid = fields.Boolean('account.fiscal.stamp', related='account_fiscal_stamp_id.is_valid')
#
#     def _check_is_valid(self, cr, uid, ids, context=None):
#
#         dispatch_point_fiscal_stamps = self.search([('account_dispatch_point_id', '=', self.account_dispatch_point_id)])
#
#         for record in dispatch_point_fiscal_stamps:
#             if record.is_valid and self.is_valid:
#                 return False
#
#     _constraints = [
#         (_check_is_valid, 'The dispatch point can only have one valid fiscal stamp!', ['account_dispatch_point_id, is_valid'])
#     ]
#
#     _sql_constraints = [
#         ('account_dispatch_point_account_fiscal_stamp_id_acc_key',
#          'unique (account_dispatch_point_id,account_fiscal_stamp_id)',
#          'The dispatch point fiscal stamp must be unique!')
#     ]
