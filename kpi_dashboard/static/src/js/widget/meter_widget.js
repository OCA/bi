odoo.define('kpi_dashboard.MeterWidget', function (require) {
    "use strict";

    var AbstractWidget = require('kpi_dashboard.AbstractWidget');
    var registry = require('kpi_dashboard.widget_registry');


    var MeterWidget = AbstractWidget.extend({
        template: 'kpi_dashboard.meter',
        fillWidget: function(values) {
            var input = this.$el.find('[data-bind="value"]');
            var options = this._getMeterOptions(values);
            var margin = (this.widget_dimension_x - options.size)/2;
            input.gaugeMeter(options);
            input.parent().css('padding-left', margin);
        },
        _getMeterOptions: function(values) {
            var size = Math.min(
                this.widget_size_x,
                this.widget_size_y - 40,) - 10;
            return {
                percent: values.value.value,
                style: 'Semi',
                width: 6,
                size: size,
            };
        },
    });

    registry.add('meter', MeterWidget);
    return MeterWidget;
});
