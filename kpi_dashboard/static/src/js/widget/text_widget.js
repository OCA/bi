odoo.define('kpi_dashboard.TextWidget', function (require) {
    "use strict";

    var AbstractWidget = require('kpi_dashboard.AbstractWidget');
    var registry = require('kpi_dashboard.widget_registry');
    var core = require('web.core');
    var qweb = core.qweb;


    var TextWidget = AbstractWidget.extend({
        template: 'kpi_dashboard.base_text',
        fillWidget: function (values) {
            return;
        }
    });

    registry.add('base_text', TextWidget);
    return TextWidget;
});
