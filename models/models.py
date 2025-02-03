from odoo import models, fields, api

class AccountPayment(models.Model):
    _inherit = "account.payment"

    bank_fee = fields.Monetary(string="Bank Fee", currency_field="currency_id", help="Fee charged by the bank.")
    fee_included = fields.Selection(
        selection=[
            ('bank_fee_excluded', 'Excluded'),
            ('bank_fee_included', 'Included'),
        ],
        string="Bank Fee", help="Check if the bank fee is included in the payment amount.")

    def _prepare_move_line_default_vals(self, write_off_line_vals=None):

        line_vals = super()._prepare_move_line_default_vals(write_off_line_vals=write_off_line_vals)

        if self.fee_included == 'bank_fee_included':
            if self.bank_fee > 0:

                for line in line_vals:
                    if line['amount_currency'] > 0:
                        line['amount_currency'] -= self.bank_fee
                        break

                bank_fee_line = {
                    'name': "Bank Fee",
                    'account_id': 176,
                    'debit': self.bank_fee,
                    'credit': 0.0,
                    'payment_id': self.id,
                    'partner_id': self.partner_id.id,
                    'currency_id': self.currency_id.id,
                }

                line_vals.append(bank_fee_line)

        elif self.fee_included == 'bank_fee_excluded':
            if self.bank_fee > 0:

                bank_fee_line = [{
                    'name': "Bank Fee",
                     'account_id': 111,
                    'debit': 0.0,
                    'credit': self.bank_fee,
                    'payment_id': self.id,
                    'partner_id': self.partner_id.id,
                    'currency_id': self.currency_id.id,
                },
                {
                    'name': "Bank Fee",
                    'account_id': 176,
                    'debit': self.bank_fee,
                    'credit': 0.0,
                    'payment_id': self.id,
                    'partner_id': self.partner_id.id,
                    'currency_id': self.currency_id.id,
                }]
                line_vals.extend(bank_fee_line)

        return line_vals