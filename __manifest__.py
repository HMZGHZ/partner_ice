{
    'name': 'Partner ICE',
    'version': '17.0',
    'category': 'Custom',
    'summary': 'Ajoute le champ ICE aux clients et fournisseurs',
    'description': """
        Ajout du champ ICE sur la fiche client et fournisseur, ainsi que sur les documents de vente, d'achat et de comptabilité.
    """,
    'depends': ['base', 'sale', 'purchase', 'account'],
    'data': [
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
        'views/account_move_view.xml',
        'report/sale_order_report.xml',
        'report/purchase_order_report.xml',
        'report/account_invoice_report.xml',
    ],
}
