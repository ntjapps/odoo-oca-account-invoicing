# Copyright 2024 Moduon Team S.L.
# Copyright 2026 NTJ (https://www.ntj.co.id)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

# v19-incompat: Removed in v19: res.partner.invoice_warn Selection field gone (parent_view_buttons no longer has invoice_warn_msg).
{
    "name": "Account Warn Option",
    "summary": "Add Options to Account Warn Messages",
    "version": "19.0.1.0.0",
    "development_status": "Alpha",
    "category": "Accounting/Accounting",
    "website": "https://github.com/OCA/account-invoicing",
    "author": "Moduon, Odoo Community Association (OCA)",
    "maintainers": ["Shide", "rafaelbn"],
    "license": "LGPL-3",
    "application": False,
    "installable": False,
    "auto_install": True,
    "depends": ["account", "base_warn_option"],
    "data": [
        "views/res_partner_views.xml",
    ],
}
