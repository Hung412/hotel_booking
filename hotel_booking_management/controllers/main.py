# -*- coding: utf-8 -*-
import odoo

from odoo import http, _
from odoo.http import request


class BookingRoomPortal(http.Controller):

    @http.route(['/booking_room'], type='http', auth="user", website=True)
    def get_url_portal_document(self, new=False):
        # new = '/booking_room/new' in request.httprequest.path
        # if new:
        hotel_booking_ids = request.env['hotel.booking.management'].sudo().search([])
        total_available_room = len(hotel_booking_ids.filtered(lambda x: x.status == 'available'))
        total_booked_room = len(hotel_booking_ids.filtered(lambda x: x.status == 'booked'))
        total_fixing_room = len(hotel_booking_ids.filtered(lambda x: x.status == 'fixing'))

        data = {
            'hotel_booking_ids': hotel_booking_ids,
            'total_available_room': total_available_room,
            'total_booked_room': total_booked_room,
            'total_fixing_room': total_fixing_room,
            'room_status': ['available', 'booked', 'fixing']
        }

        return request.render('hotel_booking_management.portal_hotel_booking_room', data)
