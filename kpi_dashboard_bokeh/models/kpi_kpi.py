# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from bokeh.plotting import figure
from bokeh.embed import components
from odoo import fields, models
import random


class KpiKpi(models.Model):

    _inherit = "kpi.kpi"

    widget = fields.Selection(selection_add=[("bokeh", "Bokeh")])

    def test_demo_bokeh(self):
        p = figure(width=1000, height=1000, sizing_mode="scale_both")
        # import that as `from bokeh.plotting import figure`
        p.line([0, 1, 2], [1, 10, random.random() * 10], line_width=5)
        # (...)
        # fill the record field with both markup and the script of a chart.
        script, div = components(p)
        return {"bokeh": "%s%s" % (div, script)}
