# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Kpi Dashboard",
    "summary": """
        Create Dashboards using kpis""",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "author": "Creu Blanca,Odoo Community Association (OCA)",
    "website": "www.creublanca.es",
    "depends": ["bus", "web", "base_sparse_field", "web_widget_color"],
    "qweb": ["static/src/xml/dashboard.xml"],
    "data": [
        "security/ir.model.access.csv",
        "views/webclient_templates.xml",
        "views/kpi_kpi.xml",
        "views/kpi_dashboard.xml",
    ],
    "demo": [],
}
