# -*- coding: utf-8 -*-
{
    'name': "library_app",
    'summary': """ App para gerenciamento de biblioteca. """,
    'description': """ App para gerenciamento de biblioteca. """,
    'author': "Leonardo Vieira",
    'depends': ['base'],
    'application': True,
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml'
    ],
}