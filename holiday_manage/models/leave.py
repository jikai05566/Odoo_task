# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime
from openerp.exceptions import ValidationError


class Leave(models.Model):
    """
    请假
    """
    _description = 'Leave holiday'
    _name = 'leave'

    employee_id = fields.Many2one('hr.employee', string='员工姓名')
    leave_count = fields.Char(string='请假天数')
    leave_date = fields.Date(string='请假日期')
    state = fields.Selection([('draft', '草稿'),
                              ('done', '完成')],
                             default='draft', string='State')
    leave_record_id = fields.Many2one('leave.record')

    @api.multi
    def do_confirm(self):
        """
        请假菜单确认按钮
        :return:
        """

        if self.leave_date < str(datetime.date.today()):
            raise ValidationError('日期错误')

        for record in self:
            # 校验员工的可发假天数，当发假天数不足以请假的时候不准请假
            if record.leave_count > record.employee_id.holiday_count:
                raise ValidationError('Error')

            record.write({'state': 'done'})
            # 每次确认请假，将这条记录传入record表中
            record.env['leave.record'].create(
                {'employee_id': self.employee_id.id, 'leave_record_day': self.leave_count,
                 'leave_date': self.leave_date, 'state': self.state, 'leave_id': record.id})

    @api.multi
    def do_cancel(self):
        """
        撤销按钮
        """
        # 将state状态置为草稿状态
        self.write({'state': 'draft'})
        # 将leave.record表中状态为draft的记录删除
        for record in self:
            record.env['leave.record'].search([('leave_id', '=', record.id)]).write({'state': 'draft'})
