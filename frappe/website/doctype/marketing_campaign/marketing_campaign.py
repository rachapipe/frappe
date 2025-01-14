# Copyright (c) 2023, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MarketingCampaign(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

<<<<<<< HEAD:frappe/website/doctype/marketing_campaign/marketing_campaign.py
		campaign_description: DF.SmallText | None
=======
		method: DF.Data | None
		scheduled_against: DF.Link
>>>>>>> 4ab7c103c1 (refactor: make scheduled_against mandatory):frappe/core/doctype/scheduler_event/scheduler_event.py
	# end: auto-generated types
	pass
