# -*- coding: utf-8 -*-
##############################################################################
#
#    LeanTic (www.leantic.com)
#    Copyright (c) 2017 Leantic S.A. (http://leantic.com)
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

{
    'name': 'Paraguay - Accounting',
    'version': '1.0',
    'description': """
Paraguayan accounting chart and tax localization.
==================================================

Plan contable paraguayo e impuestos de acuerdo a disposiciones vigentes

    """,
    'author': ['Leantic S.A.'],
    'website': 'http://leantic.com',
    'category': 'Localization',
    'depends': ['account'],
    'data':[
        'data/l10n_py_chart_data.xml',
        'data/account_tax_data.xml',
        'data/account_chart_template_data.yml',
    ],
'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
}