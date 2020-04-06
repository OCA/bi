odoo.define('kpi_dashboard.AbstractWidget', function (require) {
    "use strict";
    var Widget = require('web.Widget');
    var field_utils = require('web.field_utils');
    var time = require('web.time');
    var registry = require('kpi_dashboard.widget_registry');

    var AbstractWidget = Widget.extend({
        template: 'kpi_dashboard.base_widget',
        cssLibs: [],
        jsLibs: [],
        init: function(parent, kpi_values) {
            this._super(parent);
            this.col = kpi_values.col;
            this.row = kpi_values.row;
            this.sizex = kpi_values.sizex;
            this.sizey = kpi_values.sizey;
            this.color = kpi_values.color;
            this.values = kpi_values;
            this.margin_x = parent.state.specialData.margin_x;
            this.margin_y = parent.state.specialData.margin_y;
            this.widget_dimension_x = parent.state.specialData.widget_dimension_x;
            this.widget_dimension_y = parent.state.specialData.widget_dimension_y;
            this.widget_size_x = this.widget_dimension_x * this.sizex +
                (this.sizex - 1) * this.margin_x;
            this.widget_size_y = this.widget_dimension_y * this.sizey +
                (this.sizey - 1) * this.margin_y;
        },
        renderElement: function () {
            var result = this._super.apply(this, arguments);
            this.$el.css('background-color', this.color);
            this._fillWidget(this.values);
            return result
        },
        _fillWidget: function(values) {
            this.fillWidget(values);
            var value = field_utils.parse.datetime(values.value_last_update);
            var item = this.$el.find('[data-bind="value_last_update_display"]');
            if (item)
                item.text(value.clone().add(
                    this.getSession().getTZOffset(value), 'minutes').format(
                    time.getLangDatetimeFormat()
                ));
        },
        fillWidget: function(values) {
            var value = values.value;
            var self = this;
            _.each(value, function(val, key) {
                var item = self.$el.find('[data-bind=' + key + ']')
                if (item)
                    item.text(val);
            })
        },
    });
    registry.add('abstract', AbstractWidget);
    return AbstractWidget;
});
