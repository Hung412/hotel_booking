from odoo import api, models, fields, _

class HotelBookingManagement(models.Model):
    _name = 'hotel.booking.management'

    room_name = fields.Char(string='Room Name', required=True)
    status = fields.Selection([('available', 'Available'), ('booked', 'Booked'), ('fixing', 'Fixing')],
                              string='Status', default='available', required=True)
    room_type = fields.Selection([('single', 'Single'), ('double', 'Double')],
                                 string='Room Type', default='single', required=True)
    room_price = fields.Float(string='Price', compute='_compute_room_price', store=True)
    rental_type = fields.Selection([('hour', 'Hour'), ('overnight', 'Overnight')],
                                   string='Rental Type', default='hour', required=True)
    hour_rental = fields.Integer(string="Hour rental", default=2)
    room_image = fields.Image(string='Image', attachment=True)

    @api.depends('room_type')
    def _compute_room_price(self):
        for rec in self:
            if rec.room_type == 'single':
                rec.room_price = 15
            else:
                rec.room_price = 30
