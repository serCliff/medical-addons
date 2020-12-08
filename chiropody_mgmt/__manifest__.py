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
        'base_fontawesome',
    ],

    'data': [
        'security/chiropody_security.xml',
        'views/chiropody_menu.xml',
        'views/res_partner.xml',
        'views/chiropody_session.xml',
        'views/chiropody_treatment.xml',
    ],

}
