// Copyright (c) 2023, Quantbit Team and contributors
// For license information, please see license.txt


frappe.ui.form.on('Ticket Track History', {
    refresh: function(frm) {
        $('.layout-side-section').hide();
        $('.layout-main-section-wrapper').css('margin-left', '0');
    }
});

frappe.ui.form.on('Ticket Track History', {
	refresh: function(frm) {
		frm.clear_table("child_ticket")
		frm.refresh_field('child_ticket')
		frm.call({
			method:'get_ticket_list',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});

frappe.ui.form.on('Ticket Track History', {
	onload: function(frm) {
		frm.call({
			method:'set_default_date',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});
frappe.ui.form.on('Ticket Track History', {
	ticket_name: function(frm) {
		frm.clear_table("child_ticket")
		frm.refresh_field('child_ticket')
		frm.refresh_field('custom_serial_number')
		frm.call({
			method:'get_ticket_list',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});

frappe.ui.form.on('Ticket Track History', {
	custom_serial_number: function(frm) {
		frm.clear_table("child_ticket")
		frm.refresh_field('child_ticket')
		frm.refresh_field('ticket_name')
		frm.call({
			method:'get_ticket_list',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});

frappe.ui.form.on('Ticket Track History', {
	to_date: function(frm) {
		frm.clear_table("child_ticket")
		frm.refresh_field('child_ticket')
		frm.call({
			method:'get_ticket_list',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});


