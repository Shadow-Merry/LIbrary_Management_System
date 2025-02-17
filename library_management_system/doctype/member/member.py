# Copyright (c) 2025, Unknown and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Member(Document):
	def before_save(self):
 		self.membership_id = f'{self.name}'
