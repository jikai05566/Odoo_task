# -*- coding: utf-8 -*-
{
    'name': "holiday_manage",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "季凯",
    'website': "http://www.eroad.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/send_holiday_security.xml',
        'security/ir.rule.xml',
        'security/ir.model.access.xml',

        'views/hr_employee.xml',
        'views/holiday.xml',
        'views/leave.xml',
        'views/ir_sequence_data.xml',
        # 'wizard/leave_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}