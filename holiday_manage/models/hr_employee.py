# -*- coding: utf-8 -*-

from openerp import models, fields, api


class HrEmployee(models.Model):
    """
    员工信息
    """
    _description = 'Employee Information'
    _name = 'hr.employee'

    name = fields.Char(string='员工姓名')
    whether_send_holiday = fields.Boolean('是否发假', default=False)
    holiday_count = fields.Char(string='可用假期', compute='_compute_holiday_count')
    leave_record_ids = fields.One2many('leave.record', 'employee_id', string='请假记录')
    send_record_ids = fields.One2many('send.record', 'employee_id', string='发假记录')
    create_uid = fields.Many2one('res.users', default=lambda self: self.env.user)
    active = fields.Boolean(default=True, string='Active')

    @api.depends('holiday_count')
    def _compute_holiday_count(self):
        """计算可用假期天数"""
        for record in self:
            # 总发假数
            holiday_day = sum(
                [int(count.send_days) for count in
                 record.sudo().env['holiday'].search([('employee_id', '=', record.id)]) if
                 count.state == 'done'])
            # 总请假数
            leave_day = sum([int(num.leave_count) for num in
                             record.env['leave'].search([('employee_id', '=', record.id)]) if num.state == 'done'
                             ])
            # 可用假期天数的计算
            record.holiday_count = holiday_day - leave_day

    @api.multi
    def unlink(self):
        """
        重写删除逻辑
        :return:
        """
        for record in self:
            record.active = False
