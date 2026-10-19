# Costs, Free Tiers, and Student Benefits

**Official information checked on 2026-10-06.** USD amounts below are the providers' displayed prices. Taxes, exchange rates, region, payment channel, and promotions can affect the final amount. Confirm the total at checkout.

Distinguish free plans, time-limited offers, institutional access, and usage-based APIs. Signing in with a student email address does not make every product free.

## Choose an accessible starting route

If you already have an approved tool that can assist with local Python files, use that route. Otherwise, look at the **General free access** column and follow the matching [tool setup page](index.md#choose-your-tool-page). Confirm your own account can use the interface before proceeding. A student offer is an option, not a prerequisite for this exercise.

Choose one route and continue to installation; return to the detailed offer sections only if they apply to your account. There is no need to claim benefits from every provider. When a limit is reached, you can wait for it to reset rather than purchase extra usage.

## Comparison

| Product | General free access | Student benefits | Paid access and conditions |
| --- | --- | --- | --- |
| Antigravity | Individual is $0/month with basic weekly rate limits | Google AI student offers depend on region and plan. The Japan announcement offers one year of AI Plus and discounts on AI Pro. An Antigravity limit increase is not established by that offer alone | Google AI Pro / Ultra provide higher limits and a credit pool. Confirm regional prices at checkout |
| Grok Build | Grok has a $0 Free plan, but Build's free allowance and request counts could not be established from the retrieved pricing-table text | No Build-specific free student offer was found in the official pages reviewed | SuperGrok is $30/month; Plus is $100/month. Plus explicitly includes higher Build usage. Confirm Build eligibility on lower tiers at checkout. API billing is separate |
| GitHub Copilot | Copilot Free includes 2,000 completions/month and an AI credit allowance | Copilot Student is free for GitHub Education verified students, with monthly eligibility reevaluation | Pro $10/month, Pro+ $39/month, Max $100/month. AI usage is credit-based; check additional usage separately |
| Codex | Included in ChatGPT Free, with desktop-app availability and rollout conditions | No ongoing free offer for all individual students was found on the reviewed pricing page. Edu is institutional access | Plus $20/month supports CLI, IDE, web, and other surfaces. Pro starts at $100/month. API-key usage is separately billed |
| Claude Code | Do not treat Claude's free chat allowance as free Claude Code access | No universal individual-student free Code offer was found. Education is a university-level contract | Pro includes Code: $20 monthly, or $200 paid upfront annually. Max and API access are alternatives. Usage limits apply |

Sources: [Antigravity pricing](https://antigravity.google/pricing), [Google's Japan student announcement](https://blog.google/intl/ja-jp/company-news/technology/gemini-student-offer-google-ai/), [Grok pricing](https://x.ai/pricing), [Copilot plans](https://docs.github.com/en/copilot/get-started/plans), [student activation](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students), [Codex pricing](https://learn.chatgpt.com/docs/pricing), and [Claude pricing](https://claude.com/pricing).

## Before claiming a student offer

### Google / Antigravity

Google's Japan announcement describes 12 months of AI Plus at no charge for eligible university students and discounts on AI Pro. Do not reuse older claims that AI Pro is free without checking the current offer. Visit the [student signup page](https://gemini.google/students/) to check region, eligibility, deadline, verification, and payment-method requirements. Personal and school accounts may have different eligibility rules.

Check both the offer you claimed and the plan, models, and remaining allowance actually active in Antigravity. Do not infer Pro-level Antigravity access from an AI Plus offer. Record the renewal price after the free period and the cancellation deadline in ENVIRONMENT.md. [Official announcement, Japan-specific](https://blog.google/intl/ja-jp/company-news/technology/gemini-student-offer-google-ai/).

### GitHub Copilot

Apply to GitHub Education, complete student verification, activate Copilot Student, and sign in to your development environment with the same account. Verification documents do not need to be shared with an AI tool or uploaded to a public repository. [Official activation instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students).

The June 1 update to the official student announcement states **200 monthly AI credits and unlimited code completions**. The reviewed plan documentation limits Free / Student model selection to Auto. Do not reuse older descriptions such as “300 premium requests per month” or “students get the same plan as Pro.” [Official student announcement](https://github.com/orgs/community/discussions/189268), [plan documentation](https://docs.github.com/en/copilot/get-started/plans).

AI credits are a usage allowance rather than a fixed number of conversations. Consumption depends on the model and tokens (chunks of input/output text) used. Long agent tasks can use more credits. [Billing explanation](https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing).

### Codex / Claude Code / Grok Build

Institutional Edu / Education contracts are separate from free offers for individual students. Even if your school has a contract, confirm whether Code, CLI access, and external connections are allowed. [Codex pricing](https://learn.chatgpt.com/docs/pricing), [Claude Education](https://claude.com/solutions/education).

For Grok, inspect Build support indicators in the pricing table in a browser, then confirm your signed-in eligibility and remaining allowance. This guide does not establish that Build is free for everyone or requires one particular paid plan. [Pricing table](https://x.ai/pricing), [Build setup](https://docs.x.ai/build/overview).

## Subscription and extra-cost checklist

Use this checklist if you claim a trial, enable paid usage, or already use a paid plan. For a free route without a payment method, fields such as renewal price can be marked “not applicable.”

- [ ] Confirm the plan name, price, currency, and monthly or annual billing.
- [ ] Check the free period, application deadline, and student reverification rules.
- [ ] Record the next renewal date, renewal amount, and cancellation location.
- [ ] Check whether reaching a limit stops work or enables extra credits or API billing.
- [ ] If using extra usage, automatic top-ups, or APIs, set limits within your budget.
- [ ] Confirm which payment source is attached to your account.

If a free allowance is insufficient, reduce task scope, save progress to files, and wait or move to another accessible environment. Preparing a [handoff](workflow/handoff.md) first gives you time to make a deliberate billing decision.
