# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class KpiDashboard(models.Model):

    _name = "kpi.dashboard"
    _description = "Dashboard"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True,)
    kpi_ids = fields.One2many(
        "kpi.dashboard.kpi", inverse_name="dashboard_id",
    )
    number_of_columns = fields.Integer(default=5, required=True)
    width = fields.Integer(default=500, required=True)
    margin_y = fields.Integer(default=10, required=True)
    margin_x = fields.Integer(default=10, required=True)
    widget_dimension_x = fields.Integer(default=140, required=True)
    widget_dimension_y = fields.Integer(default=140, required=True)

    def read_dashboard(self):
        self.ensure_one()
        return {
            "name": self.name,
            "width": self.width,
            "kpi_ids": self.kpi_ids.read_dashboard(),
            "max_cols": self.number_of_columns,
            "margin_x": self.margin_x,
            "margin_y": self.margin_y,
            "widget_dimension_x": self.widget_dimension_x,
            "widget_dimension_y": self.widget_dimension_y,
        }


class KpiDashboardKpi(models.Model):
    _name = "kpi.dashboard.kpi"
    _description = "Kpi"

    kpi_id = fields.Many2one("kpi.kpi", required=True,)
    dashboard_id = fields.Many2one("kpi.dashboard", required=True,)
    column = fields.Integer(required=True, default=1)
    row = fields.Integer(required=True, default=1)
    size_x = fields.Integer(required=True, default=1)
    size_y = fields.Integer(required=True, default=1)
    color = fields.Char()

    def _read_dashboard(self):
        return {
            "id": self.id,
            "kpi_id": self.kpi_id.id,
            "name": self.kpi_id.name,
            "value": self.kpi_id.value,
            "col": self.column,
            "row": self.row,
            "sizex": self.size_x,
            "sizey": self.size_y,
            "widget": self.kpi_id.widget,
            "color": self.color,
            "value_last_update": self.kpi_id.value_last_update,
        }

    def read_dashboard(self):
        result = []
        for kpi in self:
            result.append(kpi._read_dashboard())
        return result
