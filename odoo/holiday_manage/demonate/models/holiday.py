# -*- coding: utf-8 -*-

from openerp import models, fields


class Holiday(models.Model):
    '''
    发假
    '''

    _name = 'holiday'
    _description = 'Send Holiday'

    num = fields.Integer(string='Number')
    employee= fields.Many2one("hr.employee", string="Employee")


