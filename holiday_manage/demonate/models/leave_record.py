# -*- coding: utf-8 -*-

from openerp import models, fields, api


class LeaveRecord(models.Model):
    '''
    请假记录
    '''
    _description = 'Leave Record'
    _name = 'leave.record'

    leave_date = fields.Date(string='Leave Date', required=True)
    employee_id = fields.Many2one('hr.employee', string='Leave Employee Name')
    leave_record_day = fields.Integer(string='Leave Day')



