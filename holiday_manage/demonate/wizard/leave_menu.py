# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError
import datetime


class LeaveMenu(models.Model):
    '''
    请假菜单
    '''
    _description = 'Leave Menu'
    _name = 'leave.menu'

    employee_name = fields.Many2one('hr.employee', string='Employee Name')
    leave_count = fields.Integer(string='Holiday Number')
    leave_date = str(datetime.date.today())

    @api.multi
    def do_confirm(self):
        for record in self:
            if record.leave_count > record.employee_name.holiday_count:
                raise ValidationError('Error')
            record.env['leave.record'].create(
                {'leave_record_employee': self.employee_name.id, 'leave_record_day': self.leave_count,
                 'leave_date': self.leave_date})
