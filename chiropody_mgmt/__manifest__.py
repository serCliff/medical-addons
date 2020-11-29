# -*- coding: utf-8 -*-
{
    'name': "Chiropody Management",

    'summary': """
        Medical Clinic of chiropody Management
        """,

    'author': "Sergio Del Castillo",
    'website': "https://github.com/serCliff/",

    'category': 'medical',
    "contributors": [
        "Sergio Del Castillo <serdelcas1990@gmail.com>",
    ],
    'version': '2.0',

    'depends': [
        'sale',
        'medical_fields',
    ],

    'data': [
        'security/chiropody_security.xml',
        # # 'security/ir.model.access.csv',
        # 'views/physiotherapy_view.xml',
        'views/res_partner.xml',
        # 'views/treatment_history.xml',
        # 'views/partner_treatment.xml',
    ],

}
