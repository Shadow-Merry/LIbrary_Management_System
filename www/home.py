import frappe
import html


@frappe.whitelist(allow_guest=True)  # Allow access from the frontend
def get_context():
    # Get the form data, including the CSRF token
    csrf_token = frappe.form_dict.get('csrf_token')

    email = frappe.form_dict.get("email")
    password = frappe.form_dict.get("password")
    
    
    exists = frappe.db.exists(
        "Member",
        {
        "email": email,
        "password": password
        },
        )
    if exists:
 
        # values ={'email' : email}
        # data = frappe.db.sql("""
        # SELECT 
        #     me.name 
        # FROM 
        #     `tabMemeber` me
        # WHERE 
        #     me.email = %(email)s
        # """,values=values, as_dict=0)
        # doc = frappe.db.get_value("Member", ["email",email], as_dict=True)
        # Example usage
        doctype = "Member"
        filters = {"email": email}
        fields = ["name"]

        # Retrieve a list of records matching the filters
        records = frappe.get_list(doctype, filters=filters, fields=fields)
        for x in records:
            value = x.name
        values = str(value)
        frappe.local.login_manager.login_as(email)
        frappe.session.data[id] = values 
        frappe.local.session_obj.update()
        # x = frappe.session.user
    book = frappe.get_all("Book", 
    fields=["title", "author", "publish_date","isbn","status","image"]
    )
        
    return {"book": book}
    # else:
    #     return frappe.respond_as_web_page(
    #     ("logins"),html
    # )

        # context = {"INvlue"}
        # return frappe.render_template("/www/login.html",context)