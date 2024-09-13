from odoo import models, fields

class EmployeeLoanType(models.Model):
    _name = 'employee.loan.type'
    _description = 'employee loan type'

    name = fields.Char(string='loan type')
    loan_limit = fields.Float(string='Loan Amount Limit')
    interest_rate = fields.Float(string='Interest Rate')
    account_id = fields.Many2one('account.account',string="LOan Account")






