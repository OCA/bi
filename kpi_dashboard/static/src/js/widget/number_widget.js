odoo.define('kpi_dashboard.NumberWidget', function (require) {
    "use strict";

    var AbstractWidget = require('kpi_dashboard.AbstractWidget');
    var registry = require('kpi_dashboard.widget_registry');
    var field_utils = require('web.field_utils');


    var NumberWidget = AbstractWidget.extend({
        template: 'kpi_dashboard.number',
        fillWidget: function(values) {
            var widget = this.$el;
            var value = values.value.value;
            if (value === undefined)
                value = 0;
            var item = widget.find('[data-bind="value"]')
            if (item)
                item.text(field_utils.format.integer(value));
            var previous = values.value.previous;

            var $change_rate = widget.find('.change-rate')
            if (previous === undefined) {
                $change_rate .toggleClass('active', false);
            }
            else {
                var difference = 0;
                if (previous !== 0)
                    difference = field_utils.format.integer(
                        100 * value  / previous - 100) + '%';
                $change_rate .toggleClass('active', true);
                var $difference = widget.find('[data-bind="difference"]');
                $difference.text(difference);
                var $arrow = widget.find('[data-bind="arrow"]');
                if (value < previous){
                    $arrow.toggleClass('fa-arrow-up', false);
                    $arrow.toggleClass('fa-arrow-down', true);
                }
                else {
                    $arrow.toggleClass('fa-arrow-up', true);
                    $arrow.toggleClass('fa-arrow-down', false);
                }
            }
        },
    });
    registry.add('number', NumberWidget);
    return NumberWidget;
});
