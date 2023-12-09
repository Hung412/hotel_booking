from odoo import api, models, fields, _

class HotelBookingManagement(models.Model):
    _name = 'hotel.booking.management'

    room_name = fields.Char(string='Room Name')
    status = fields.Selection([('available', 'Available'), ('booked', 'Booked')], string='Status')
