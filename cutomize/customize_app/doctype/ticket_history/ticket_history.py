# Copyright (c) 2023, Quantbit Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
class TicketHistory(Document):
	pass
#     def refresh(self):
#         frappe.db.set_value("Ticket History", self.name, "layout_side_section", 0)
#         frappe.db.set_value("Ticket History", self.name, "layout_main_section_wrapper", 0)
#         self.add_custom_button("Get Report", self.export_to_excel)
#         self.load_version_data()
#         self.clear_primary_action()

#     def ticket_name(self):
#         self.load_version_data()
#         self.clear_primary_action()

#     def from_date(self):
#         self.load_version_data()
#         self.clear_primary_action()

#     def to_date(self):
#         self.load_version_data()
#         self.clear_primary_action()

#     def load_version_data(self):
#         page_length = 200
#         page_number = 1
#         from_date = self.from_date or ''
#         to_date = self.to_date or ''
#         ticket_name = self.ticket_name or ''

#         filters = {
#             'docname': ['like', '%' + ticket_name + '%'],
#             'ref_doctype': 'Issue',
#         }

#         if from_date and to_date:
#             filters['modified'] = ['between', [from_date + ' 00:00:00', to_date + ' 23:59:59']]
#         elif ticket_name:
#             filters['docname'] = ['like', '%' + ticket_name + '%']

#         data = frappe.get_list(
#             doctype='Version',
#             fields=['docname', 'data', 'modified', 'modified_by', 'ref_doctype'],
#             limit_start=(page_number - 1) * page_length,
#             limit_page_length=page_length,
#             filters=filters
#         )

#         help_content = """
#             <div class="table-responsive">
#                 <table class="table table-bordered">
#                     <thead>
#                         <tr>
#                             <th style="position: sticky; top: 0; background-color: white; width:10%">Ticket Name</th>
#                             <th style="position: sticky; top: 0; background-color: white;width:10%">Date</th>
#                             <th style="position: sticky; top: 0; background-color: white;">Field</th>
#                             <th style="position: sticky; top: 0; background-color: white;">Old data</th>
#                             <th style="position: sticky; top: 0; background-color: white;">New data</th>
#                             <th style="position: sticky; top: 0; background-color: white;">User</th>
#                         </tr>
#                     </thead>
#                     <tbody>
#         """

#         for item in data:
#             docname = item.docname or ''
#             modified = item.modified or ''
#             user_value = item.modified_by or ''
#             changes_data = frappe.parse_json(item.data)
#             changes = changes_data.get('changed', [])

#             for j, change in enumerate(changes):
#                 field = change[0]
#                 old_value = change[1]
#                 new_value = change[2]
#                 if field == "signature":
#                     if old_value:
#                         old_value = "True"
#                     if new_value:
#                         new_value = "True"
#                 help_content += """
#                     <tr>
#                         <td>{}</td>
#                         <td>{}</td>
#                         <td>{}</td>
#                         <td>{}</td>
#                         <td>{}</td>
#                         <td>{}</td>
#                     </tr>
#                 """.format(docname if j == 0 else '', modified if j == 0 else '', field, old_value, new_value, user_value if j == 0 else '')

#         help_content += """
#                     </tbody>
#                 </table>
#             </div>
#         """

#         # Set HTML content in the specified field
#         self.show_html = help_content

#     def clear_primary_action(self):
#         self.get("__onload").clear_primary_action()

#     def export_to_excel(self):
#         frappe.msgprint("Hi")  # Placeholder for export action

# # Example usage:
# doc = Document('Ticket History', 'your_document_name')  # Replace 'your_document_name'
# doc.refresh()
# doc.export_to_excel()

