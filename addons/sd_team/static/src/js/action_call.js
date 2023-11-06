odoo.define('module-name.tree_button', function (require) {
"use strict";
var ListController = require('web.ListController');
var ListView = require('web.ListView');
var viewRegistry = require('web.view_registry');
var TreeButton = ListController.extend({
   buttons_template: 'module_name.buttons',
   events: _.extend({}, ListController.prototype.events, {
       'click .import_your_action': '_OpenWizard',
   }),
   _OpenWizard: function () {
       var self = this;

   }
});
var InputListView = ListView.extend({
   config: _.extend({}, ListView.prototype.config, {
       Controller: TreeButton,
   }),
});
viewRegistry.add('button_in_tree', InputListView);
});