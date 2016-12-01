# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError
import datetime


class Holiday(models.Model):
    """
    发假
    """
    _description = 'Send Holiday'
    _name = 'holiday'

    def _get_default_id(self):
        """将发假单的员工编号变成自动生成"""
        return self.env['ir.sequence'].next_by_code('holiday')

    employee_num = fields.Char(string='员工编号', readonly=True, default=_get_default_id)
    employee_id = fields.Many2one("hr.employee", string='员工姓名')
    send_days = fields.Char(string='发假天数')
    # create_uid = fields.Many2one('res.users', default=lambda self: self.env.user)
    send_date = str(datetime.date.today())
    state = fields.Selection([('draft', '草稿'),
                              ('done', '完成')],
                             default='draft', string='State')

    @api.multi
    def send_holiday(self):
        """
        发假按钮
        """
        self.employee_id.whether_send_holiday = True
        self.write({'state': 'done'})
        for record in self:
            # 每次确认请假，将这条记录传入record表中
            record.env['send.record'].create(
                {'employee_id': self.employee_id.id, 'send_record_day': self.send_days, 'send_date': self.send_date,
                 'state': self.state, 'send_id': record.id})

    @api.multi
    def do_cancel(self):
        """
        撤销按钮
        """
        # 判断可用假期天数是否大于单次已发假数，如果小于则无法撤销
        if self.employee_id.holiday_count < self.send_days:
            raise ValidationError('无法撤销')

        # 将state状态置为草稿状态
        self.write({'state': 'draft'})
        # 将记录的state修改为draft
        for record in self:
            record.env['send.record'].search([('send_id', '=', record.id)]).write({'state': 'draft'})

    @api.multi
    def unlink(self):
        """
        重写删除逻辑
        :return:
        """
        raise ValidationError('错误!')
