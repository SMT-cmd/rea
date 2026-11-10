#!/usr/bin/env python3
"""Read-only source-presence checklist for a local authorized GWS checkout.
NO network, no shell, no credentials, no DB mutations and no test payments.
Presence of text patterns is never evidence that a feature works in production.
"""
import argparse
import json
import pathlib
import re
import sys

CHECKS = [
 ("P0","Paystack split initialization","lib/payments/live-marketplace-adapter.ts",["initializeLiveMarketplaceSplit","subaccount","transaction_charge"]),
 ("P0","Server-side verified payment proof","lib/payments/live-marketplace-journal.ts",["verifyLivePaystackReference","recordVerifiedCharge"]),
 ("P0","Signed webhook handling","app/api/webhooks/paystack/route.ts",["timingSafeEqual","charge.success","verifyLivePaystackReference"]),
 ("P0","Courier original-rate booking","lib/services/live-courier-dispatch.ts",["rateId","booking"]),
 ("P1","Explicit final checkout consent","app/api/orders/route.ts",["hasConfirmedCheckoutReview"]),
 ("P1","Buyer review checkbox","components/storefront/StorefrontCheckoutPageView.tsx",["checkoutReviewConfirmed","orderReviewed"]),
 ("P1","Cart Buy Now parity","lib/cart-checkout-navigation.ts",["cartLineCheckoutHref"]),
 ("P1","Vendor photo upload API","app/api/vendor/product-images/upload/route.ts",["POST"]),
 ("P1","Payout account UI","components/dashboard/PayoutSettingsForm.tsx",["bank"]),
 ("P1","Customer/seller messaging","lib/business-chat.ts",["user"]),
 ("P1","In-stock product inventory reservations","lib/inventory-reservations.ts",["reserveInventory"]),
 ("P2","Explore page","app/(marketing)/explore/page.tsx",["Explore"]),
 ("P2","Explore editorial showcase","components/explore/ExploreMarketplaceShowcase.tsx",["Explore"]),
 ("P2","Verified product ratings","lib/storefront-product-ratings.ts",["rating"]),
 ("P2","Local shopper discovery","lib/explore/discovery.ts",["search"]),
 ("P2","Shared theme contrast","app/globals.css",["theme-text","theme-muted"]),
]

def audit(root: pathlib.Path):
    result=[]
    for priority,name,path,markers in CHECKS:
        file=root/path
        if not file.is_file():
            status="NOT_FOUND"
            missing=list(markers)
        else:
            text=file.read_text(encoding="utf-8",errors="replace")
            missing=[m for m in markers if re.search(re.escape(m),text,re.IGNORECASE) is None]
            status="SOURCE_PRESENT" if not missing else "NEEDS_REVIEW"
        result.append({"priority":priority,"name":name,"path":path,"source_status":status,"missing_markers":missing,"production_verified":False})
    return result

def main():
    p=argparse.ArgumentParser(description="Read-only GWS source inventory (not QA certification)")
    p.add_argument("repo",type=pathlib.Path,help="Local SMT-cmd/Gwebstore checkout")
    p.add_argument("--json",action="store_true",help="Machine-readable output")
    args=p.parse_args()
    root=args.repo.expanduser().resolve()
    if not (root/"package.json").is_file():
        print("Expected a local Gwebstore checkout with package.json; no files changed.",file=sys.stderr)
        return 2
    result=audit(root)
    if args.json:
        print(json.dumps({"scope":"source_only","production_tested":False,"checks":result},indent=2))
    else:
        print("GWS source inventory ONLY — never report SOURCE_PRESENT as a passed production test")
        for c in result: print(f"{c['priority']:3} {c['source_status']:14} {c['name']} ({c['path']})")
    return 0

if __name__=="__main__":
    sys.exit(main())
