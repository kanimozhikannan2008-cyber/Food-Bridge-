# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    # Export CSV
    (
        '<button class="btn btn-outline-sm" onclick="exportCategoryHistoryCSV()">📥 Export CSV</button>',
        '<button class="btn btn-outline-sm" onclick="exportCategoryHistoryCSV()" data-i18n="btn_export_csv">📥 Export CSV</button>',
    ),

    # Donor History Metrics & Headers
    (
        '<span class="hm-lbl">Total Surplus Postings</span>',
        '<span class="hm-lbl" data-i18n="lbl_total_postings">Total Surplus Postings</span>',
    ),
    (
        '<span class="hm-lbl">Meals Successfully Rescued</span>',
        '<span class="hm-lbl" data-i18n="lbl_rescued_meals">Meals Successfully Rescued</span>',
    ),
    (
        '<span class="hm-lbl">Active In-Transit / Dispatched</span>',
        '<span class="hm-lbl" data-i18n="lbl_active_intransit">Active In-Transit / Dispatched</span>',
    ),
    (
        '<span class="hm-lbl">FSSAI Safety Compliance</span>',
        '<span class="hm-lbl" data-i18n="lbl_safety_compliance">FSSAI Safety Compliance</span>',
    ),
    (
        '<th>Posting ID</th>\n                  <th>Food Item & Description</th>\n                  <th>Quantity & Type</th>\n                  <th>Pickup Hub</th>\n                  <th>Matched Shelter</th>\n                  <th>Courier Assigned</th>\n                  <th>Status</th>\n                  <th>Action</th>',
        '<th data-i18n="th_posting_id">Posting ID</th>\n                  <th data-i18n="th_food_desc">Food Item & Description</th>\n                  <th data-i18n="th_qty_type">Quantity & Type</th>\n                  <th data-i18n="th_pickup_hub">Pickup Hub</th>\n                  <th data-i18n="th_matched_shelter">Matched Shelter</th>\n                  <th data-i18n="th_courier_assigned">Courier Assigned</th>\n                  <th data-i18n="th_status">Status</th>\n                  <th data-i18n="th_action">Action</th>',
    ),

    # Recipient History Metrics & Headers
    (
        '<span class="hm-lbl">Total Batches Claimed</span>',
        '<span class="hm-lbl" data-i18n="lbl_batches_claimed">Total Batches Claimed</span>',
    ),
    (
        '<span class="hm-lbl">Shelter Residents Fed</span>',
        '<span class="hm-lbl" data-i18n="lbl_residents_fed">Shelter Residents Fed</span>',
    ),
    (
        '<span class="hm-lbl">Mutex Lock Protection</span>',
        '<span class="hm-lbl" data-i18n="lbl_mutex_protection">Mutex Lock Protection</span>',
    ),
    (
        '<span class="hm-lbl">Couriers Reviewed</span>',
        '<span class="hm-lbl" data-i18n="lbl_couriers_reviewed">Couriers Reviewed</span>',
    ),
    (
        '<th>Claim / Order ID</th>\n                  <th>Rescued Food Title</th>\n                  <th>Donor Establishment</th>\n                  <th>Portions</th>\n                  <th>Delivery Partner</th>\n                  <th>Status</th>\n                  <th>Partner Rating & Feedback</th>\n                  <th>Action</th>',
        '<th data-i18n="th_claim_id">Claim / Order ID</th>\n                  <th data-i18n="th_rescued_title">Rescued Food Title</th>\n                  <th data-i18n="th_donor_org">Donor Establishment</th>\n                  <th data-i18n="th_portions">Portions</th>\n                  <th data-i18n="th_courier_assigned">Delivery Partner</th>\n                  <th data-i18n="th_status">Status</th>\n                  <th data-i18n="th_partner_rating">Partner Rating & Feedback</th>\n                  <th data-i18n="th_action">Action</th>',
    ),

    # Rider History Metrics & Headers
    (
        '<span class="hm-lbl">Accepted Runs</span>',
        '<span class="hm-lbl" data-i18n="lbl_accepted_runs">Accepted Runs</span>',
    ),
]

updated = content
applied = 0
not_found = []

for old, new in replacements:
    if old in updated:
        updated = updated.replace(old, new)
        applied += 1
    else:
        not_found.append(old.splitlines()[0][:100])

# Save as a separate output so the original index.html is not overwritten.
Path("index_i18n_updated.html").write_text(updated, encoding="utf-8")

print(f"Created index_i18n_updated.html")
print(f"Replacement patterns applied: {applied}/{len(replacements)}")
if not_found:
    print("Patterns not found (check spacing/text in your index.html):")
    for item in not_found:
        print(f"- {item}")
