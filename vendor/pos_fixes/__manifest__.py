{
    'name': 'POS Fixes',
    'summary': 'Point of Sale Fixes',
    'description': """
    Fixes included:
    - Fix POS invoices payments by reconciling them automatically on POS session closing to get them paid.
    - Complete the Gr/Ir anglo-saxon journal entries missing in POS.
    - prevent barcode on payment screen using js events .

    ToDo:
    - Reimplement Support & Process sales of product packs by IngAdhoc's product_pack.
    - Improve performance by reconciling invoices per order close not in session close .
     """,
    'version': '10.0.1.5',
    'category': 'Point of Sale',
    'author': 'DVIT.me',
    'website': 'http://dvit.me',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'account_voucher',
        'point_of_sale',
        ],
    'data': ['views.xml'],
    'installable': True,
    'auto_install': True,
    'application': False,

}
