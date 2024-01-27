# -*- coding: utf-8 -*-
import odoo

from odoo import http, _


class BookingRoomPortal(http.Controller):

    @http.route('/booking_room', type='http', auth="user", website=True)
    def booking_room(self):
        return "Welcome to Hc Hotel Booking Room"
