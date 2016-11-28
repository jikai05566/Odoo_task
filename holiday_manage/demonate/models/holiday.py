# -*- coding: utf-8 -*-

from openerp import models, fields,api
from openerp.exceptions import ValidationError


class Holiday(models.Model):
    '''
    发假
    '''
    _description = 'Send Holiday'
    _name = 'holiday'

    def _get_default_id(self):
        return self.env['ir.sequence'].next_by_code('holiday')

    employee_num = fields.Integer(string='Number', readonly=True, default=_get_default_id)
    employee_id= fields.Many2one("hr.employee", string='Employee')
    send_days = fields.Integer(string='Days')
    create_uid = fields.Many2one('res.users', default=lambda self: self.env.user)
    state = fields.Selection([('draft', 'Draft'),
                              ('done', 'Done')],
                             default='draft', string='State')

    @api.multi
    def send_holiday(self):
        '''发假按钮'''
        self.employee_id.whether_send_holiday = True
        self.write({'state': 'done'})

    @api.multi
    def do_cancel(self):
        '''撤销按钮'''
        if self.employee_id.holiday_count < self.send_days:
            raise ValidationError('无法撤销')
        self.write({'state': 'draft'})

    # @api.multi
    # def unlink(self):
    #     raise ValidationError('错误!')

