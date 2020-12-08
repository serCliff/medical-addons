# -*- coding: utf-8 -*-
{
    'name': "Medical fields",

    'summary': """
        Troncal fields used to manage a partern medical treatments
        """,

    'author': "Sergio Del Castillo",
    'website': "https://github.com/serCliff/",

    'category': 'medical',
    "contributors": [
        "Sergio Del Castillo <serdelcas1990@gmail.com>",
    ],
    'version': '0.1',

    'depends': [
        'sale',
    ],

    'data': [
        'security/ir.model.access.csv',
        'security/medical_security.xml',
        'views/res_partner.xml',
    ],

}
