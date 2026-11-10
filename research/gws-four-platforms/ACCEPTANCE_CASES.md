# Buyer, vendor and production acceptance suite

Each case records **OBSERVED / CODED / UNVERIFIED / FAILED** with release SHA and an evidence link. Do not mark paid operations passed on mocked providers.

## Checkout and payments
1. One shopper adding one unit to cart sees the same SKU/variant/quantity as Buy Now, no extra sign-in for eligible retail guest.
2. Adding two lines from one store shows separate eligible item payment or one clearly unpaid seller request. No hidden unsupported combined charge.
3. Delivery input requires a real contact, Nigerian state/LGA/city/postcode as applicable, and an actual provider rate. Error distinguishes seller pickup problem from buyer destination.
4. Review lists merchandise + courier + handling + service/processing fee + grand total; no amount charged yet.
5. Changing quantity, delivery address, selected courier or product variant invalidates previous review confirmation and quote.
6. Missing `checkoutReviewConfirmed=yes`, duplicate marker or unacknowledged review -> HTTP400; no order/Paystack attempt.
7. Expired quote -> fail-closed; fresh rate, no invented fallback courier price.
8. Seller bank not VERIFIED, missing subaccount or pending bank revision -> no payment initiation.
9. One consented authorized real-money buyer charge -> Paystack API confirms amount/NGN/reference and actual seller split; live journal matches, exactly one paid order, one inventory deduction.
10. Replayed webhook returns idempotent response, no duplicate sale or double inventory deduction.
11. Paystack return without GET/signed webhook remains Awaiting verification, not Payment confirmed.
12. Receipt recheck uses original reference and private guest token; cannot initiate another payment or expose a different buyer's receipt.
13. One existing INITIALIZED claim is reconciled before a second attempt; pending/unmatched provider evidence never marks paid.
14. Refund/reversal events mark review state; no seller notification promising non-existent payout.

## Courier and fulfillment
15. Techvault's real terminal rates show valid positive NGN and provider IDs for tested Lagos route (public quote already observed).
16. After confirmed payment, book exactly the original immutable provider rate; no re-quoting/other carrier substitution, provider booking identity checked.
17. Uncertain courier booking does not auto-repeat; status remains explicitly pending/reconciliation.
18. Pickup does not imply zero provider courier fee unless seller pickup is real and chosen.
19. Buyer receives truthful tracking; failed, returned and disputed items have separate statuses.

## Vendor/account
20. Email registration -> verification -> password sign-in -> setup -> one store + optional service office under one trial.
21. Vendor can save payout bank separately from pickup; bank verification result remains authoritative.
22. One phone-uploaded JPEG or PNG is accepted, displayed, and attached to published in-stock product (test with authorized account).
23. Malformed/oversize image gets actionable error without wiping draft or spending unexpected provider transformations.
24. Vendor product photo + video upload via authorized YouTube pipeline; provider acceptance observed (do not infer from env key).
25. Seller sees new verified paid order and can progress fulfilment; only verified order creates sale notifications.

## Discovery and quality
26. Location and price filter returns genuine listings, preserves category and responsive layout.
27. No false timer, promotion, sponsored placement, fake order count or unsupported same-day delivery.
28. Guest buyer enqueues an unpaid enquiry for pre-order/inspection service without being shown paid checkout.
29. Vendor / buyer tenant isolation, negative cases for accessing another store's listings, chat, buyer data, or payout.
30. WCAG AA spot checks on public/auth/dashboard/cart/checkout at 320, 390, 768 and desktop; light/dark/blue; focus and reduced motion.
31. Timi web/Telegram/WhatsApp returns actual purchasable SKU and same verified Paystack reference for eligible buyer.
32. Empty/abandoned cart recovery notifications only after consent; disabled/opted-out users receive nothing.

## Evidence table for each run
`Date | release SHA | route | case # | actor | observed provider response | order/reference (private) | screenshot/log URL | verdict | unresolved issue`
