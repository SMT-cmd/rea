# GWS Four-Platform REA Research MVP
**Prepared:** 10 November 2026 · **Owner fork:** [SMT-cmd/rea](https://github.com/SMT-cmd/rea) · **Target:** [Global Webstores](https://github.com/SMT-cmd/Gwebstore)

## Purpose
Reuse REA's documented, responsible browser/software-analysis workflow to *understand publicly observable patterns* at **Jumia Nigeria, Bumpa, Jiji Nigeria and Shopify**, then turn the findings into **original GWS code and verified launch acceptance**. This is a focused research starter pack, **not** a recovered copy of those services, a competitor scraper, an installed REA server, or proof that all GWS gaps are fixed.

## Contents
- `BENCHMARK_MATRIX.csv` — 34 public-pattern-to-GWS comparisons with sources, ownership and tests.
- `GWS_GAP_REGISTER.csv` — 22 P0–P3 gaps, deployed vs unverified separation, exit criteria.
- `IMPLEMENTATION_ROADMAP.md` — what to implement now, what to postpone, and payments/identity boundaries.
- `REA_WORKFLOWS.md` — prompts for lawful public-behavior analysis on each platform.
- `ACCEPTANCE_CASES.md` — checkout, onboarding, shipping, seller and discovery tests.
- `SOURCE_EVIDENCE.md` — official evidence URL catalogue, method and reliability rules.
- `audit_gws.py` — offline read-only source-presence check for your local Gwebstore clone.
- `MANIFEST.json` — provenance, version, paths and safe-use rules.

## Use in 3 steps
1. **Download the kit ZIP** in this directory or read the unpacked files here. The full REA source already lives in the parent fork; no second huge REA archive is needed.
2. Open `BENCHMARK_MATRIX.csv` and `GWS_GAP_REGISTER.csv`. Prioritize **P0 payment evidence and P1 buyer/vendor paths** before P2 polish and P3 roadmap. A `SOURCE_PRESENT` check is **not** a passed end-to-end test.
3. For a local copy of `SMT-cmd/Gwebstore`, run `python audit_gws.py /absolute/path/to/Gwebstore`. For actual REA use, follow the official instructions at https://github.com/morluto/rea (Node requirements, local setup approval and safe scopes). The prompts are ready even if REA MCP has not been connected.

## Four product lessons
| Reference | Strength to learn | Do not copy |
|---|---|---|
| Jumia | Catalogue, merchandising, order status and logistics discipline | Its vendor graphics, site code, fake sale metrics |
| Bumpa | Standalone store, CRM, invoicing, staff and stock simplicity | Its brand/assets or unsupported claims about GWS analytics |
| Jiji | Nigeria-first local search, trust, seller contact and listing velocity | Unsafe prepayment flows, fake seller ranks |
| Shopify | Cart consistency, quick checkout, payment-state clarity, customer recovery | Shop Pay's proprietary UX/data, wallet assertions |

## GWS strategy and release controls
GWS uses **one account subscription with one product storefront and one optional service office**. Timi remains a separate AI-assisted shopping channel; Paystack is the provider for verified live split collection, Terminal Africa is the carrier aggregator. The public homepage, original blue/white identity, existing SEO routes and live store checkout must be preserved. No invented shipping quotes, launch badges, carrier bookings, boosted metrics, stock, reviews or paid orders.

**Evidence as of research date:** a Techvault single-item guest cart and real courier quote/review path were verified. Paystack LIVE mode and its public key were observable. The payment claim/receipt journal remained unverified for actual money: one `INITIALIZED` claim and `PENDING_PAYMENT` order with zero verified receipts, and no confirmed paid courier bookings in a read-only checkpoint. Don't replay the same quote or mark the pending order paid without authoritative Paystack GET verification. The GWS code update must preserve the payment, payout, consent, webhook, inventory and anti-duplication checks.

**No GitHub Actions:** This documentation-only fork commit deliberately uses `[skip ci]` to avoid consuming CI minutes; REA's own source remains unchanged. Researching a competitor does not authorize inspecting private endpoints or defeating authentication, DRM, rate limits or traffic protections.
