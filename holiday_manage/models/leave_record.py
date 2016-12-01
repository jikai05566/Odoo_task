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
    state = fields.Selection([('draft', '已撤销'),
                              ('done', '已完成')], string='状态')
    leave_id = fields.Many2one('leave')



