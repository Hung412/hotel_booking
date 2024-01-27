from odoo import api, models, fields, _


class RoomManagement(models.Model):
    _name = 'room.management'

    name = fields.Char(string='Name')
