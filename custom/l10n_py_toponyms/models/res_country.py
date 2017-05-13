# -*- coding: utf-8 -*-

from odoo import models, fields, api


@api.model
def city_name_search(self, name='', args=None, operator='ilike', limit=100):
    if args is None:
        args = []

    records = self.browse()
    # if len(name) == 2:
    #     records = self.search([('code', 'ilike', name)] + args, limit=limit)

    search_domain = [('name', operator, name)]
    if records:
        search_domain.append(('id', 'not in', records.ids))
    records += self.search(search_domain + args, limit=limit)

    # the field 'display_name' calls name_get() to get its value
    return [(record.id, record.display_name) for record in records]


class CountryStateCity(models.Model):
    _name = 'res.country.state.city'
    _description = "Country state city"
    _order = 'name'

    state_id = fields.Many2one('res.country.state', string='State', required=True)
    name = fields.Char('City name', required=True)

    name_search = city_name_search
