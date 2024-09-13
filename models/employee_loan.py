from odoo import models, fields, api

class EmployeeLoan(models.Model):

    _name = 'employee.loan'
    _description = 'employee.loan'

    employee_id = fields.Many2one('hr.employee', string="Employee Id")
    department = fields.Many2one('hr.department', string = "Department",related='employee_id.department')
    loan_type_id = fields.Many2one('employee.loan.type',string = "Loan Type")
    loan_amount = float(string = "Loan Amount")
    start_date = fields.Date(string="Start Date")
    interest_rate = fields.Float(string="Interest Date", related="loan_type_id.interest_rate")
    installment_amount= float(string = 'Installment Amount',compute="_compute_installment_amount") 
    state = fields.Selection([
        ('draft','DRaft')
         ('submit_request','submit request')
             ('department_approval','Department Approval')
             ('hr_approval','HR Approval')
              ('done','done')
    ])

    # @api.model
    # def create(self,vals):
    #     if vals.get('name',_('New'))==_('New'):
    #         vals['name']=self.env


