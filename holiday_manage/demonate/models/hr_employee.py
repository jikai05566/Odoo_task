# -*- coding: utf-8 -*-

from openerp import models, fields, api


class HrEmployee(models.Model):
    '''
    员工信息
    '''
    _description = 'Employee Information'
    _name = 'hr.employee'

    name = fields.Char(string='Name')
    is_set_holiday = fields.Boolean('Set Holiday', default=False)
    holiday_count = fields.Integer(string='Holiday_count',compute='_compute_holiday_count')

    @api.depends('holiday_count')
    def _compute_holiday_count(self):
        '''计算可用假期天数'''
        for record in self:
            record.holiday_count = sum([count.day for count in record.env['holiday'].search([('employee', '=', record.id)])])
