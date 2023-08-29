# Copyright (c) 2023, Quantbit Team and contributors
# For license information, please see license.txt

import json
import os
import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta

class TicketTrackHistory(Document):
	@frappe.whitelist()
	def get_ticket_list(self):
		filters = {"ref_doctype": 'Issue'}
		if self.from_date and self.to_date:
			filters["modified"] = ["between", [self.from_date, self.to_date]]
		if self.ticket_name:
			filters["docname"] = self.ticket_name
		
		data = frappe.get_list("Version",
							filters=filters,
							fields=['docname', 'modified', 'modified_by', 'data'])
		
		for item in data:
			docname = item.docname or ''
			modified = item.modified or ''
			user_value = item.modified_by or ''
			data_dict = json.loads(item.data)
			changes = data_dict.get("changed", [])
			for change in changes:
				field, old_value, new_value = change[0], change[1], change[2]
				if old_value is None:
					old_value = 0
				if new_value is None:
					new_value = 0
				if field == 'description':
					old_value = "Yes" if old_value else ""
					new_value = "Yes" if new_value else ""
				if field == "signature":
					old_value = "Yes" if old_value else ""
					new_value = "Yes" if new_value else ""

				issue_serial = frappe.get_value("Issue", filters={"name": docname}, fieldname='serial_number') or ''
				if(self.custom_serial_number):
					if(self.custom_serial_number==issue_serial):
						self.append(
								"child_ticket",	
								{
									'ticket_name':docname,
									'serial_no':issue_serial,
									'date_time':str(modified),
									'field':str(field),
									'previous_value':str(old_value),
									'modified_value':str(new_value),
									'modified_user_email': str(user_value),
										
								}
						)
				else:
					self.append(
							"child_ticket",	
							{
								'ticket_name':docname,
								'serial_no':issue_serial,
								'date_time':str(modified),
								'field':str(field),
								'previous_value':str(old_value),
								'modified_value':str(new_value),
								'modified_user_email': str(user_value),
									
							}
					)
					
	@frappe.whitelist()
	def set_default_date(self):
		current_year = datetime.now().year
		current_month = datetime.now().month
		default_from_date, default_to_date =self.generate_default_date_range(current_year, current_month)
		self.from_date = default_from_date.strftime("%Y-%m-%d %H:%M:%S")
		self.to_date = default_to_date.strftime("%Y-%m-%d %H:%M:%S")

	def generate_default_date_range(self,year,month):
		default_from_date = datetime(year, month, 1)
		default_to_date = default_from_date.replace(day=28) + timedelta(days=3)
		if default_to_date.month != month:
			default_to_date = default_from_date.replace(day=28) + timedelta(days=2)
		return default_from_date, default_to_date