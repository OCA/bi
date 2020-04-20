# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models
import json
import altair as alt
import pandas as pd


class KpiKpi(models.Model):

    _inherit = "kpi.kpi"

    widget = fields.Selection(selection_add=[("altair", "Altair")])

    def test_demo_altair(self):
        source = pd.DataFrame(
            {
                "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
                "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
            }
        )
        chart = alt.Chart(source).mark_bar().encode(x="a", y="b")
        return {"altair": json.loads(chart.to_json())}
