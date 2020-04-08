# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class KpiDashboardMenu(models.TransientModel):

    _name = "kpi.dashboard.menu"

    dashboard_id = fields.Many2one("kpi.dashboard", required=True)
    menu_id = fields.Many2one("ir.ui.menu")

    @api.multi
    def doit(self):
        self.dashboard_id._generate_menu(self.menu_id)
