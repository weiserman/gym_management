// Copyright (c) 2022, Agile.co.za and contributors
// For license information, please see license.txt

// we have a cancel docfield button, set booking to cancelled and save
frappe.ui.form.on("Booking", {
    cancel(frm) {
        frm.set_value({
            status: 'Cancelled'
        }).then(() => {
            frm.save()
        })

    },
    class_date(frm) {
        if (frm.doc.class_date < frappe.datetime.get_today()) {
            frappe.call({
                method: 'gym_management.gym_management.doctype.booking.booking.check_in_past',
                callback: function (data) {
                    if (data.message == true) { frm.set_intro('Warning, this booking is in the past', 'red') }
                }
            }
            )
        }
    }
});