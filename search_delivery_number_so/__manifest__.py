{
    'name': 'Search Delivery Reference Number in SO',
    'version': '1.0',
    'author': 'Aktiv Software',
    'website': 'http://www.aktivsoftware.com',
    'summary': 'Delivery Reference number search , group by , filter in sale order',
    'category': 'Sale',
    'license': 'AGPL-3',
    'depends': ['stock','sale'],
    'data': [
        'view/sale_order.xml',
        'wizard/delivery_reference_sale_wizard.xml',
    ],
    'description': """
        This Module is For Delivery Reference number search , group by , filter in sale order
        For already existed so creating wizard and assign delivery number.
        
    """,
    'images': [],
    'auto_install': False,
    'installable': True,
}

