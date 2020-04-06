# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
import ast
import random


class KpiKpi(models.Model):
    _name = "kpi.kpi"
    _description = "Kpi Kpi"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    cron_id = fields.Many2one("ir.cron", readonly=True, copy=False)
    computation_method = fields.Selection(
        [("function", "Function")], required=True
    )
    value = fields.Serialized()
    dashboard_ids = fields.One2many("kpi.dashboard.kpi", inverse_name="kpi_id")
    model_id = fields.Many2one("ir.model",)
    function = fields.Char()
    args = fields.Char()
    kwargs = fields.Char()
    widget = fields.Selection(
        [("number", "Number"), ("meter", "Meter")],
        required=True,
        default="number",
    )
    value_last_update = fields.Datetime(readonly=True)

    def _cron_vals(self):
        return {
            "name": self.name,
            "model_id": self.env.ref("kpi_dashboard.model_kpi_kpi").id,
            "interval_number": 1,
            "interval_type": "hours",
            "state": "code",
            "code": "model.browse(%s).compute()" % self.id,
            "active": True,
        }

    def compute(self):
        for record in self:
            record._compute()
        return True

    def _compute(self):
        self.write(
            {
                "value": getattr(
                    self, "_compute_value_%s" % self.computation_method
                )()
            }
        )
        notifications = []
        for dashboard_kpi in self.dashboard_ids:
            channel = "kpi_dashboard_%s" % dashboard_kpi.dashboard_id.id
            notifications.append([channel, dashboard_kpi._read_dashboard()])
        if notifications:
            self.env["bus.bus"].sendmany(notifications)

    def _compute_value_function(self):
        obj = self
        if self.model_id:
            obj = self.env[self.model_id.model]
        args = ast.literal_eval(self.args or "[]")
        kwargs = ast.literal_eval(self.kwargs or "{}")
        return getattr(obj, self.function)(*args, **kwargs)

    def test_demo_number(self):
        return {
            "value": random.random() * 10000,
            "previous": random.random() * 10000,
        }

    def test_demo_meter(self):
        return {
            "min": 0,
            "max": 100,
            "value": random.random() * 100,
        }

    def generate_cron(self):
        self.ensure_one()
        self.cron_id = self.env["ir.cron"].create(self._cron_vals())

    @api.multi
    def write(self, vals):
        if "value" in vals:
            vals["value_last_update"] = fields.Datetime.now()
        return super().write(vals)