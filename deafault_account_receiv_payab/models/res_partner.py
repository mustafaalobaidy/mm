

from odoo import api, fields, models, _


class ResPartnerHere(models.Model):
    _inherit = 'res.partner'
    _description = 'Res PBARTNER'


    # @api.depends('property_account_payable_id')
    # def set_acc_here_payable(self):
    #     print("test")
    #     payable_acc_browsed = self.env['account.account'].search(
    #         [('code', '=', '200002'), ('company_id', '=', self.company_id.id)])
    #     # receivable_acc_browsed = self.env['account.account'].search(
    #     #     [('code', '=', '100020'), ('company_id', '=', self.company_id.id)])
    #     for rec in self:
    #         if payable_acc_browsed:
    #             rec.property_account_payable_id = payable_acc_browsed
    #         else:
    #             rec.property_account_payable_id = False
    #         # if receivable_acc_browsed:
    #         #     rec.property_account_receivable_id = receivable_acc_browsed.id
    #         # else:
    #         #     rec.property_account_receivable_id = False
    #




    property_account_payable_id = fields.Many2one('account.account', company_dependent=True,
                                                  string="Account Payable",
                                                  domain="[('internal_type', '=', 'payable'), ('deprecated', '=', False), ('company_id', '=', current_company_id)]",
                                                  help="This account will be used instead of the default one as the payable account for the current partner",
                                                  required=True,
                                                  default=39
                                                 )
    property_account_receivable_id = fields.Many2one('account.account', company_dependent=True,
                                                     string="Account Receivable",
                                                     domain="[('internal_type', '=', 'receivable'), ('deprecated', '=', False), ('company_id', '=', current_company_id)]",
                                                     help="This account will be used instead of the default one as the receivable account for the current partner",
                                                     required=True,default=40)

