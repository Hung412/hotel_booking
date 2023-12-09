{
    'name': 'Hotel Booking Management',
    'version': '15.0.1.0',
    'category': 'Human Resources/Employees',
    'summary': 'Hotel Booking Management',
    'description': """
        Hotel Booking Management
    """,
    'author': 'Le Hong Ngoc - Hc',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        # 'security/hotel_booking_security.xml',
        'views/hotel_booking_management.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True
}
