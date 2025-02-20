import frappe



@frappe.whitelist(allow_guest=True)  # Allow access from the frontend
def get_context():
    # Get the form data, including the CSRF token
    csrf_token = frappe.form_dict.get('csrf_token')

    title = frappe.form_dict.get("name")
    x = frappe.session.user
    doctype = "Member"
    filters = {"email": x}
    fields = ["name"]

    # Retrieve a list of records matching the filters
    records = frappe.get_list(doctype, filters=filters, fields=fields)
    for x in records:
        value = x.name
    values = str(value)
    user= values
    member = frappe.get_doc("Member",user)
    user_id = member.membership_id 
        
    loans = frappe.get_doc({
        "doctype": "Loan", 
        "member": user_id,
        "book": title
    })
    loans.save()
    books = frappe.get_doc("Book",title)
    books.status = 'Reserved'
    books.save()
    frappe.db.commit() 
    return {"message": "Successfully Resevered, Go to the library to get the book."}
