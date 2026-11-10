# GWS implementation roadmap · evidence-first

## P0 — money and order integrity (blocking fully paid launch)
**P0-A Original live Paystack reference:** There is a recorded payment claim `INITIALIZED`, but no stored verified receipt at checkpoint. Owner/Funder page `/office/live-tests` has provider-read reconciliation. Never infer charge success from initialization/return URL or initiate duplicate attempt. Need exact receipt or provider `success` with matching amount, NGN, metadata, verified seller subaccount and fee; signed webhook, single order, correct inventory.
**P0-B Courier post-payment:** Reuse immutable quoted rate and verified shipment/provider IDs; paid booking and tracking must be proven on the *same* order, after payment only. No synthetic courier rates or unapproved delivery.
**P0-C Seller settlement:** Five published checkout-enabled stores were missing verified bank/subaccount at checkpoint. Show actionable owner-facing steps; do not bypass bank owner verification or create a silent subaccount. Test payout editor separately with an authorized vendor.
**P0-D Production alerts:** Group errors by route, deployment, count, time and real cause; distinguish historic deployment errors from current. Never log buyer addresses, phone numbers, Paystack secrets or full payloads.

## P1 — customer/vendor MVP (fix before broad promotion)
1. **Unified shopper path (Shopify/Jumia):** Product page -> Add to Cart/Buy Now -> same single-item delivery quote -> final total breakdown -> explicit consent -> Paystack -> private receipt. Multi-line cart must state that combined live payment is not ready; keep a request-only alternative, not an unsafe payment shortcut.
2. **Vendor start (Bumpa/Jiji):** Email verified -> business details -> trial/subscription -> one storefront -> image/variant upload -> publication -> real Explore discovery -> enquiry. Preserve draft on failures and show next missing action. Test on phone width too.
3. **Local discovery (Jiji/Jumia):** Product name+price, category, city/LGA/state filters and graceful "no results". Do not replace real catalogue results with generated examples.
4. **Timi conversion (GWS differentiator):** WhatsApp/Telegram/web suggestions -> actual published SKU -> correct state/variant -> original hosted checkout and ledger -> paid status. Never infer delivery/read from provider acceptance.
5. **Seller and buyer trust:** Private buyer/seller chat; reviewed reports; seller pickup readiness; clear courier fee and refund policy. Reviews only from actual eligible transactions.

## P2 — upgrade after core reliability
- Source-backed **Explore rails** from Jumia, using owner-approved GWS artwork and real listing data; no artificial flash-sales timers, stock or rankings.
- Bumpa-like **vendor operations cockpit**: 3–5 primary actions, meaningful invoices/receipts, actual sales/profit after refunds, first-listing milestone, inventory warnings. Do not confuse pending payment with revenue.
- Jiji-like **saved search and favourite reminders**, opt-in only, local filters preserved.
- Shopify-like **abandoned-cart recovery**, only opt-in, no generic guest contact harvesting; record consent and provider delivery.
- Cross-site contrast/keyboard/mobile checks: public, auth, dashboard, vendor, cart, order, dark/blue/light. A source CSS pass alone cannot certify contrast on every nested page.
- Merchant SEO: verified storefront titles, categories, structured data, media, canonical/sitemaps and noindex drafts.

## P3 — additional scope, not a surprise launch promise
- Multi-item, cross-vendor checkout with multiple seller splits; one paid order per merchant grouping and exact fee ledger.
- Offline POS/barcodes, multiple merchant staff roles/locations, customer group analytics, advanced promotions, premium placement funding and brand/official certification.
- Shopify app-like integrations, Bumpa CRM export, Jiji-style promotions, third-party ad buying **only after** provider approval and finance controls.

## Implementation safeguards
- Keep `SMT-cmd/Gwebstore/main`, never replace with REA's repository.
- No GitHub Actions, paid infra, fake data, test-secret disclosure, payment-gate bypass, production DB resets or third-party asset reuse.
- Always label completion as **built**, **tests passed**, **Vercel READY**, **public-browser verified**, **authenticated verified**, **provider paid verified** separately.
- Do not expand account slots: **one storefront plus optional one service office per account**, under one subscription.
- Follow the verified Paystack single-vendor split path and Terminal Africa original-rate identity, not deprecated escrow.
