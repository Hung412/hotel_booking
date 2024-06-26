# -*- coding: utf-8 -*-
import odoo

from odoo import http, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class BookingRoomPortal(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True,)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super(BookingRoomPortal, self).shop(page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post)
        val = res.qcontext.get('products')
        room_available = request.env['product.template'].sudo().search([('state', '=', 'available')])
        res.qcontext['products'] = room_available
        res.qcontext['search_product'] = room_available
        return res

    @http.route(['/booking/checkout'], type='http', auth="user", website=True)
    def get_url_portal_document(self, new=False):
        # new = '/booking_room/new' in request.httprequest.path
        # if new:
        # hotel_booking_ids = request.env['hotel.booking.management'].sudo().search([])
        # total_available_room = len(hotel_booking_ids.filtered(lambda x: x.status == 'available'))
        # total_booked_room = len(hotel_booking_ids.filtered(lambda x: x.status == 'booked'))
        # total_fixing_room = len(hotel_booking_ids.filtered(lambda x: x.status == 'fixing'))

        # data = {
        #     'hotel_booking_ids': hotel_booking_ids,
        #     'total_available_room': total_available_room,
        #     'total_booked_room': total_booked_room,
        #     'total_fixing_room': total_fixing_room,
        #     'room_status': ['available', 'booked', 'fixing']
        # }

        return request.render('hotel_booking_management.portal_hotel_booking_room', {})

    @http.route(['/my-booking'], type='http', auth="user", website=True)
    def my_hotel_booking(self, new=False):
        room_ids = request.env['hotel.booking.management'].sudo().search([('user_id', '=', request.env.user.id)])
        return request.render('hotel_booking_management.my_booking_room', {'room_ids': room_ids})
