from odoo import models, fields, api
# from odoo.tools.float_utils import float_round as round


class PosOrder(models.Model):
    _inherit = "pos.order"

    '''This code will complete the anglo-saxon STJ entries
        in COGS / Stock accounts per order'''

    @api.multi
    def pos_fixes(self, ids):
        # print ('------------ POSFIX --start---oids - ' + str(ids) + ' ------------')

        # account_move_obj = self.env['account.move']
        move_line_obj = self.env['account.move.line']
        for order in self.browse(ids):
            # print ('------------ POSFIX --start---order - ' + str(order.name) + ' ------------')
            if order.state == 'invoiced' or order.invoice_id:
                continue

            o_lines = order.lines.filtered(lambda l: \
                l.product_id.categ_id.property_valuation == 'real_time' and \
                l.product_id.type in ['product', 'consu'] )

            if o_lines:
                company_id = order.company_id.id
                session = order.session_id
                move = self._create_account_move(session.start_at,
                                                     order.name,
                                                     int(session.config_id.journal_id.id),
                                                     company_id,
                                                     )
                # print ('------------ POSFIX --move-name - ' + str(move.name) + ' ------------')
                # print ('------------ POSFIX --move-id - ' + str(move.id) + ' ------------')
                amount_total = order.amount_total

                for o_line in o_lines :
                    # print ('------------ POSFIX --- ' + str(o_line.name) + ' ------------')
                    amount = 0
                    stkacc = o_line.product_id.categ_id.property_stock_account_output_categ_id and \
                        o_line.product_id.categ_id.property_stock_account_output_categ_id
                    # print ('------------ POSFIX --- ' + str(stkacc.name) + ' ------------')

                    # cost of goods account cogacc
                    cogacc = o_line.product_id.property_account_expense_id and \
                        o_line.product_id.property_account_expense_id
                    # print ('------------ POSFIX --- ' + str(cogacc.name) + ' ------------')

                    if not cogacc:
                        cogacc = o_line.product_id.categ_id.property_account_expense_categ_id and \
                            o_line.product_id.categ_id.property_account_expense_categ_id

                    amount = o_line.qty * o_line.product_id.standard_price
                    line_vals = {
                        'name': o_line.product_id.name,
                        'move_id': move.id,
                        'journal_id': move.journal_id.id,
                        'date': move.date,
                        'product_id': o_line.product_id.id,
                        'partner_id': order.partner_id and order.partner_id.id or False,
                        'quantity': o_line.qty,
                        'ref': o_line.name
                    }
                    # print ('------------ POSFIX line_vals --- ' + str(line_vals) + ' ------------')

                    if amount_total > 0:
                            # create move.lines to credit stock and debit cogs
                        caml = {
                            'account_id': stkacc.id,
                            'credit': amount,
                            'debit': 0.0,
                        }
                        caml.update(line_vals)
                        daml = {
                            'account_id': cogacc.id,
                            'credit': 0.0,
                            'debit': amount,
                        }
                        daml.update(line_vals)
                        # print ('------------ POSFIX caml --- ' + str(caml) + ' ------------')
                        # print ('------------ POSFIX daml --- ' + str(daml) + ' ------------')

                        move_line_obj.with_context(check_move_validity=False).create( caml)
                        move_line_obj.with_context(check_move_validity=False).create( daml)
                        move.post()

                    if amount_total < 0:
                        # create move.lines to credit cogs and debit ?stock?
                        # ToDo: return goods directly to inv. valuation account instead of GRNI/GSNI acc.
                        caml = {
                            'account_id': cogacc.id,
                            'credit': -amount,
                            'debit': 0.0,
                        }
                        caml.update(line_vals)
                        daml = {
                            'account_id': stkacc.id,
                            'credit': 0.0,
                            'debit': -amount,
                        }
                        daml.update(line_vals)
                        move_line_obj.with_context(check_move_validity=False).create( caml)
                        move_line_obj.with_context(check_move_validity=False).create( daml)
                        move.sudo().post()


        return True

    @api.model
    def create_from_ui(self, orders):
        o_ids = super(PosOrder, self).create_from_ui(orders)
        self.pos_fixes(o_ids)
        return o_ids

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
