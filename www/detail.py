import frappe



@frappe.whitelist(allow_guest=True)  # Allow access from the frontend
def get_context():
    # Get the form data, including the CSRF token
    csrf_token = frappe.form_dict.get('csrf_token')

    title = frappe.form_dict.get("name")
    Titles = frappe.get_doc("Book", title)
    return {"response":Titles}