# -*- coding: utf-8 -*-

from openerp import models, fields


class HrEmployee(models.Model):
    '''
    员工表
    '''

    _name = 'hr.employee'
    _description = 'Employee Information'

    name = fields.Char(string='Name')
    is_set_holiday = fields.Boolean(default= False, string="Set Holiday")


