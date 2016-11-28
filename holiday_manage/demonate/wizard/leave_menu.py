# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError
import datetime


class LeaveMenu(models.Model):
    """
    请假菜单
    """
    _description = 'Leave Menu'
    _name = 'leave.menu'

    employee_id = fields.Many2one('hr.employee', string='Employee Name')
    leave_count = fields.Integer(string='Holiday Number')
    leave_date = str(datetime.date.today())

    @api.multi
    def do_confirm(self):
        """
        请假菜单确认按钮
        :return:
        """
        for record in self:
            # 校验员工的可发假天数，当发假天数不足以请假的时候不准请假
            if record.leave_count > record.employee_id.holiday_count:
                raise ValidationError('Error')
            # 每次确认请假，将这条记录传入record表中
            record.env['leave.record'].create(
                {'employee_id': self.employee_id.id, 'leave_record_day': self.leave_count,
                 'leave_date': self.leave_date})
