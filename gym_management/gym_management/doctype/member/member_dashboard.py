from frappe import _


def get_data():
	return {
		"heatmap": True,
		"heatmap_message": _(
			"Member Measurements"
		),
		"fieldname": "member",
		"transactions": [
			{
				"label": _("Membership Contracts"),
				"items": ["Gym Membership"],
			},
            {
				"label": _("Bookings"),
				"items": ["Class Booking", "Locker Booking"],
			},
            {
				"label": _("Health Tracking"),
				"items": ["Member Measurements"],
			}
		],
	}