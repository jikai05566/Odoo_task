# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class HrEmployee(models.Model):
    '''
    员工信息
    '''
    _description = 'Employee Information'
    _name = 'hr.employee'

    name = fields.Char(string='Name')
    whether_send_holiday = fields.Boolean('Set Holiday', default=False)
    holiday_count = fields.Integer(string='Holiday_count', compute='_compute_holiday_count')
    leave_record_ids = fields.One2many('leave.record', 'employee_id', string='Leave Record')
    create_uid = fields.Many2one('res.users')
    active = fields.Boolean(default=True, string='Active')

    @api.depends('holiday_count')
    def _compute_holiday_count(self):
        '''计算可用假期天数'''
        for record in self:
            holiday_day = sum(
                [count.send_days for count in record.env['holiday'].search([('employee_id', '=', record.id)]) if
                 count.state == 'done'])
            leave_day = sum([num.leave_record_day for num in
                             record.env['leave.record'].search([('employee_id', '=', record.id)])])
            record.holiday_count = holiday_day - leave_day

    @api.multi
    def unlink(self):
        for record in self:
            record.active = False

