// Copyright (c) 2022, amadhaji@open-alt.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Card', {
	onload: function(frm){
		frm.set_query("doctype_card", function(){
			return { filters:{ "issingle": 0 } };
		});
	},

	refresh: function(frm) {
		if (! frm.is_new()){
			frm.add_custom_button(__("Print Cards"), () => {
				frm.events.print_select(frm);
			});
			frm.change_custom_button_type(__("Print Cards"), null, "primary");
		}
	},

	print_select: function(frm){
		frm.selector = new frappe.ui.form.MultiSelectDialog({
			doctype: frm.doc.doctype_card,
			size: "extra-large",
			setters: JSON.parse(frm.doc.filter_fields),
			target: frm,
			add_filters_group: 1,
			data_fields: [{
					fieldname: 'select_all',
					fieldtype: 'Check',
					label: __('Select All'),
					onchange: function() {
						let select_all = frm.selector.dialog.get_value("select_all");
						frm.selector.dialog.set_df_property("results_area", "hidden", select_all);
					}
				},
			],
			primary_action_label: __("Print"),
			action: function(elements, data){
				let filters = ""
				if (data.select_all){
					delete data.filtered_children;
					delete data.select_all;
					filters = JSON.stringify(data)
				}
				else {
					filters = JSON.stringify({name: ["in", elements]});
				}

				frm.set_value("filters", filters);
				frm.save();
				frm.print_doc();

			}
		});
	},

});
