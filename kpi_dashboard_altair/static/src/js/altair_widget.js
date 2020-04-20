odoo.define('kpi_dashboard.AltairWidget', function (require) {
    "use strict";

    var AbstractWidget = require('kpi_dashboard.AbstractWidget');
    var registry = require('kpi_dashboard.widget_registry');
    var DashboardView = require('kpi_dashboard.DashboardView');

    var AltairWidget = AbstractWidget.extend({
        template: 'kpi_dashboard.altair',
        fillWidget: function(values) {
            var widget = this.$el.find('[data-bind="value"]');
            widget.css('height', this.widget_size_y - 90);
            vegaEmbed(
                widget[0],
                values.value.altair,
                this.altairOptions(values)
            );
            console.log(this.widget_size_y - 90)
        },
        altairOptions: function (values) {
            return {
                //mode: "vega-lite",
                height: this.widget_size_y - 135,
                width: this.widget_size_x - 20,
                actions: false,
            }
        }
    });

    registry.add('altair', AltairWidget);
    return AltairWidget;
});
