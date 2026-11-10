# REA workflows for lawful competitor feature research

Use REA **only** when it is actually installed/connected, the operator owns or is authorized to inspect the target, and the advertised provider supports the operation. This kit was prepared from public official documentation and GWS source checks—not from a live REA extraction. Public browser screenshots and visual observation are enough to inform original design. Do not assume browser CDP attachment works in this ChatGPT session.

## A. Jumia Nigeria — shopping path (public pages only)
```
Investigate public Jumia Nigeria shopping discovery and checkout communication.
Use public pages and official VendorHub guidance. Map global search, category
hierarchy, listing images, stock messaging, shipping/collection choices,
order tracking and returns. Produce a click-path diagram with source URLs,
observed/unknown fields, mobile pain points and an ORIGINAL GWS adaptation.
Do not log in, crawl private listings, intercept sessions, automate purchases,
or copy protected artwork/source.
```

## B. Bumpa — small merchant journey (public pages only)
```
Study Bumpa's documented merchant onboarding and store operations from official
public pages. Map website creation, inventory, invoices/receipts, CRM, staff roles,
analytics, logistics and payment-state language. Classify which features are
plan-dependent and which cannot be tested without a consenting account.
Compare to GWS's one-account subscription and one storefront plus optional
service office. Recommend original dashboard components, acceptance tests,
and safe backlog ownership. Do not use private API probes.
```

## C. Jiji Nigeria — local marketplace communication (public pages only)
```
Inspect publicly documented search filters, saved searches, seller contacts,
listing creation requirements, feedback, report mechanisms and visibility labels.
Explain how GWS can improve city/LGA search, unpaid enquiry, chat, listing
trust and assisted Timi shopping. Keep buyer warnings honest; do not present
a private negotiation as a completed Paystack order. Never harvest seller
phone numbers or generate spam.
```

## D. Shopify — cart and after-checkout (public documentation only)
```
Study Shopify's official 2026 checkout/customer-account/cart-sync notes.
Write a state machine: cart_saved -> delivery_quoted -> review_acknowledged ->
payment_initialized -> provider_verified -> order_paid -> fulfilled/refunded.
List the differences between a hosted Paystack redirect and a verified receipt.
Recommend the simplest no-new-paid-service implementation for GWS.
Never scrape account data or imply GWS has Shop Pay credentials.
```

## E. Inspect the GWS code you own (REA optional; repository tools preferred)
```
In SMT-cmd/Gwebstore at the current main SHA, map the actual public and
vendor routes and each state transition, plus tests and provider guards.
Run the local read-only audit_gws.py from this kit; it establishes only
presence of source markers. For each candidate improvement provide:
route/components, real evidence, current status, proposed small patch,
negative test, expected provider behavior, rollback, owner decision.
Never bypass payment signature, signed quote, bank verification or idempotency.
No GitHub Actions; verify latest Vercel READY and browser acceptance.
```

## REA bootstrap
The fork already contains REA's implementation. To use its MCP locally,
follow https://github.com/morluto/rea and `npx rea-agents setup` after reviewing
Node version and the installation plan. The tool's agent skill expressly says
**skip REA for ordinary source-repository architecture analysis**, which is why
the GWS local source audit runs without REA. Analyze browser runtime only
when the browser profile and target are authorized and actually accessible.
