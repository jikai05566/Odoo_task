# -*- coding: utf-8 -*-

from openerp import models, fields, api


class SendRecord(models.Model):
    """
    发假记录
    """
    _description = 'Send Record'
    _name = 'send.record'

    send_date = fields.Date(string='发假时间', required=True)
    employee_id = fields.Many2one('hr.employee', string='员工姓名')
    send_record_day = fields.Char(string='发假天数')
    state = fields.Selection([('draft', '已撤销'),
                              ('done', '已完成')], string='状态')
    send_id = fields.Many2one('holiday')

