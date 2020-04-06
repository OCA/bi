odoo.define('kpi_dashboard.DashboardController', function (require) {
    "use strict";

    var BasicController = require('web.BasicController');
    var core = require('web.core');
    var QWeb = core.qweb;

    var DashboardController = BasicController.extend({
        renderPager: function ($node, options) {
            options = _.extend({}, options, {
                validate: this.canBeDiscarded.bind(this),
            });
            this._super($node, options);
        },
        _pushState: function (state) {
            state = state || {};
            var env = this.model.get(this.handle, {env: true});
            state.id = env.currentId;
            this._super(state);
        },
    });

    return DashboardController ;

});
