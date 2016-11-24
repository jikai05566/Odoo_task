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

    num = fields.Integer(string='Number', readonly=True, default=_get_default_id)
    employee_name= fields.Many2one("hr.employee", string='Employee')
    day = fields.Integer(string='Days')
    state = fields.Selection([('draft', 'Draft'),
                              ('done', 'Done')],
                             default='draft', string='State')

    @api.multi
    def send_holiday(self):
        '''发假按钮'''
        self.employee_name.is_set_holiday = True
        self.write({'state': 'done'})

    @api.multi
    def do_cancel(self):
        '''撤销按钮'''
        self.write({'state': 'draft'})
        if self.env['hr.employee'].holiday_count < self.day:
            raise ValidationError('无法撤销')

    @api.multi
    def unlink(self):
        raise ValidationError('错误!')

