// Copyright (c) 2022, Agile.co.za and contributors
// For license information, please see license.txt

frappe.ui.form.on("Class", {
    refresh(frm) {
        frm.add_custom_button(
            "Book Class",
            () => {
                let dialog = new frappe.ui.Dialog({
                    title: "Select Member to Book",
                    fields: [
                        {
                            fieldtype: "Link",
                            fieldname: "member",
                            label: "Member",
                            options: "Member",
                        },
                    ],
                    primary_action_label: "Book Class",
                    primary_action: (data) => {
                        console.log(data);
                        let { member } = data;
                        frappe.new_doc("Booking", {
                            class: frm.doc.name,
                            member: member,
                            status: "Booked"
                        });
                    },
                });

                dialog.show();
            },
            "Actions"
        );
    },
});