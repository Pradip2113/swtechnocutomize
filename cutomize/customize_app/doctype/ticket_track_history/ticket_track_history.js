// Copyright (c) 2023, Quantbit Team and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ticket Track History', {

});
// frappe.ui.form.on('Ticket Track History', {
// 	show: function(frm) {
// 		frm.call({
// 			method:'get_data',//function name defined in python
// 			doc: frm.doc, //current document
// 		});
// 	}
// });

// frappe.ui.form.on('Ticket Track History', {
//     refresh: function(frm) {
//         $('.layout-side-section').hide();
//         $('.layout-main-section-wrapper').css('margin-left', '0');
//          frm.add_custom_button(__('Get Report'), function() {
//             // exportToExcel(frm);
//             frappe.msgprint("Hi")
//         });
//         loadVersionData(frm);
//         frm.page.clear_primary_action();
//     },
//     ticket_name: function(frm) {
//         loadVersionData(frm);
//         frm.page.clear_primary_action();
//     },
//     from_date: function(frm) {
//         loadVersionData(frm);
//         frm.page.clear_primary_action();
//     },
//     to_date: function(frm) {
//         loadVersionData(frm);
//         frm.page.clear_primary_action();
//     }
// });

// function loadVersionData(frm) {
//     var page_length = 200;
//     var page_number = 1;
//     var from_date = frm.doc.from_date || '';
//     var to_date = frm.doc.to_date || '';
//     var ticket_name = frm.doc.ticket_name || '';

//     var filters = {
//         'docname': ['like', '%' + ticket_name + '%'],
//         'ref_doctype': 'Issue',
//     };
//     if (from_date && to_date) {
//         filters['modified'] = ['between', [from_date + ' 00:00:00', to_date + ' 23:59:59']];
//     } else if (ticket_name) {
//         filters['docname'] = ['like', '%' + ticket_name + '%'];
//     }

//     frappe.call({
//         method: 'frappe.client.get_list',
//         args: {
//             doctype: 'Version',
//             fields: ['docname', 'data', 'modified', 'modified_by', 'ref_doctype'],
//             limit_start: (page_number - 1) * page_length,
//             limit_page_length: page_length,
//             filters: filters,
//         },
//         callback: function(response) {
//             var data = response.message;
//             var help_content = `
//                 <div class="table-responsive">
//                     <table class="table table-bordered">
//                         <thead>
//                             <tr>
//                                 <th style="position: sticky; top: 0; background-color: white; width:10%">Ticket Name</th>
//                                 <th style="position: sticky; top: 0; background-color: white;width:10%">Date</th>
//                                 <th style="position: sticky; top: 0; background-color: white;">Field</th>
//                                 <th style="position: sticky; top: 0; background-color: white;">Old data</th>
//                                 <th style="position: sticky; top: 0; background-color: white;">New data</th>
//                                 <th style="position: sticky; top: 0; background-color: white;">User</th>
//                             </tr>
//                         </thead>
//                         <tbody>
//             `;

//             for (var i = 0; i < data.length; i++) {
//                 var docname = data[i].docname || '';
//                 var modified = data[i].modified || '';
//                 var userValue = data[i].modified_by || '';
//                 var changesData = JSON.parse(data[i].data);
//                 var changes = changesData.changed || [];

//                 for (var j = 0; j < changes.length; j++) {
//                     var field = changes[j][0];
//                     var oldValue = changes[j][1];
//                     var newValue = changes[j][2];
//                     if (field == "signature") {
//                         if (oldValue) {
//                             oldValue = "True"
//                         }

//                         if (newValue) {
//                             newValue = "True"
//                         }
//                     }
//                     help_content += `
//                         <tr>
//                             <td>${j === 0 ? docname : ''}</td>
//                             <td>${j === 0 ? modified : ''}</td>
//                             <td>${field}</td>
//                             <td>${oldValue}</td>
//                             <td>${newValue}</td>
//                             <td>${j === 0 ? userValue : ''}</td>
//                         </tr>
//                     `;
//                 }
//             }

//             help_content += `
//                         </tbody>
//                     </table>
//                 </div>
//             `;

//             // Insert HTML content into the specified field
//             frm.fields_dict["show_html"].$wrapper.html(help_content);
//         }
//     });
// }

