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
        frappe.local.login_manager.login_as(email)
        x = frappe.session.user
        book = frappe.get_all("Book", 
        fields=["title", "author", "publish_date","isbn","status","image"]
        )
    # return frappe.render_template("test_app/www/list.html", {"todos": todos})
        return {"book": book,
        "token" : x}
    else:
        return frappe.respond_as_web_page(
        ("logins"),html
    )

        # context = {"INvlue"}
        # return frappe.render_template("/www/login.html",context)