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
    holiday_count = fields.Integer(string='Holiday_count', compute='_compute_holiday_count')
    leave_record = fields.One2many('leave.record', 'leave_record_employee', string='Leave Record')

    @api.depends('holiday_count')
    def _compute_holiday_count(self):
        '''计算可用假期天数'''
        for record in self:
            holiday_day = sum(
                [count.day for count in record.env['holiday'].search([('employee_name', '=', record.id)]) if
                 count.state == 'done'])
            leave_day = sum([num.leave_record_day for num in
                             record.env['leave.record'].search([('leave_record_employee', '=', record.id)])])
            record.holiday_count = holiday_day - leave_day
