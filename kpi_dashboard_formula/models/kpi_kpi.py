# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models
from odoo.tools.safe_eval import safe_eval


class KpiKpi(models.Model):

    _inherit = "kpi.kpi"
    computation_method = fields.Selection(selection_add=[("code", "Code")])
    code = fields.Text("Code",)

    def _get_code_input_dict(self):
        return {
            "self": self,
            "model": self,
        }

    def _compute_value_code(self):
        results = self._get_code_input_dict()
        safe_eval(self.code or "", results, mode="exec", nocopy=True)
        return results.get("result", {})
