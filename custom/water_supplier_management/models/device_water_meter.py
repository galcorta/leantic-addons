# -*- coding: utf-8 -*-
# (c) 2017 Guido Alcorta - Leantic
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields


class WaterMeter(models.Model):
    _name = "device.water.meter"
    _description = "Holds records of devices water meters"

    def _def_company(self):
        return self.env.user.company_id.id

    name = fields.Char('Meter name', required=True)
    company = fields.Many2one('res.company', 'Company', required=True,
                              default=_def_company)
    year = fields.Char('Year')
    model = fields.Char('Model')
    holder_partner = fields.Many2one(
        comodel_name='res.partner', string='Holder partner',
        help="This partner holds the device water meter")
    meter_value = fields.Char('Meter Value')
    device_water_meters_reads = fields.One2many(
        string='Water meter reads', comodel_name='device.water.meter.read',
        inverse_name='device_water_meter_id')


class WaterMeterRead(models.Model):
    _name = "device.water.meter.read"
    _description = "Records of meter readings"

    device_water_meter_id = fields.Many2one(
        comodel_name='device.water.meter', string='Water meter',
        help="This is the water meter related", required=True)
    date_read = fields.Datetime('Read date')
    meter_value = fields.Char('Meter Value')
    date_created = fields.Datetime('Date created', required=False, readonly=False, select=True,
                                   default=lambda self: fields.datetime.now())


