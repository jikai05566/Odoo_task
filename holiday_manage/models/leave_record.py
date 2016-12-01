# -*- coding: utf-8 -*-

from openerp import models, fields, api


class LeaveRecord(models.Model):
    """
    请假记录
    """
    _description = 'Leave Record'
    _name = 'leave.record'

    leave_date = fields.Date(string='请假日期', required=True)
    employee_id = fields.Many2one('hr.employee', string='员工姓名')
    leave_record_day = fields.Char(string='请假天数')
    state = fields.Selection([('draft', '草稿'),
                              ('done', '完成')], string='State')
    leave_id = fields.Many2one('leave')



