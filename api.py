import frappe

@frappe.whitelist() 
def get_books():
    books = frappe.get_all("Book", 
        fields=["title", "author", "publish_date","isbn","status","image"]
        )
    return books

@frappe.whitelist() 
def add_books():
    title = frappe.form_dict.get("title")
    author = frappe.form_dict.get("author")
    publish_date = frappe.form_dict.get("publish_date")
    isbn = frappe.form_dict.get("isbn")
    status = 'Available'
    image = frappe.form_dict.get('image')

    book = frappe.get_doc({
        "doctype": "Book", 
        "title": title ,
        "author": author,
        "publish_date":publish_date,
        "isbn":isbn,
        "status":status,
        "image":image
    })
    
    book.save()
    return {"message": "Book created successfully"}

@frappe.whitelist() 
def delete_books():
    book = frappe.get_doc("Book", frappe.form_dict.get("name"))
    book.delete()

    return {"message": "Book deleted successfully"}

@frappe.whitelist()
def update_books():
    title = frappe.form_dict.get("title")
    author = frappe.form_dict.get("author")
    publish_date = frappe.form_dict.get("publish_date")
    isbn = frappe.form_dict.get("isbn")
    status = 'Available'
    image = frappe.form_dict.get('image')

    book = frappe.get_doc("Book",title) 
    book.author = author
    book.publish_date = publish_date
    book.isbn = isbn
    book.status = status
    book.image = image
    
    book.save()
    return {"message": "Book Updated successfully"}


@frappe.whitelist() 
def get_members():
    members = frappe.get_all("Member", 
        fields=["name1", "email", "phone_number","membership_id"]
        )
    return members

@frappe.whitelist() 
def add_members():
    name1 = frappe.form_dict.get("name1")
    email = frappe.form_dict.get("email")
    phone_number = frappe.form_dict.get("phone_number")
    password = frappe.form_dict.get("password")

    member = frappe.get_doc({
        "doctype": "Member", 
        "name1": name1,
        "email": email,
        "phone_number":phone_number,
        "password":password
    })
    
    member.save()
    return {"message": "Member created successfully"}

@frappe.whitelist() 
def delete_members():
    member = frappe.get_doc("Member", frappe.form_dict.get("membership_id"))
    member.delete()

    return {"message": "Member deleted successfully"}

@frappe.whitelist()
def update_members():
    name1 = frappe.form_dict.get("name1")
    email = frappe.form_dict.get("email")
    phone_number = frappe.form_dict.get("phone_number")
    membership_id = frappe.form_dict.get("membership_id")

    member = frappe.get_doc("Member",membership_id) 
    member.name1 = name1
    member.email = email
    member.phone_number = phone_number
    
    member.save()
    return {"message": "Member Updated successfully"}


@frappe.whitelist()
def update_passwords():
    password = frappe.form_dict.get('password')
    membership_id = frappe.form_dict.get('membership_id')
    
    member = frappe.get_doc("Member",membership_id)
    member.password = password

    member.save()
    return {"message" : "Member Password Updated Successfully"}

