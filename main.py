"""Write the 30-day plan to /output/entry.txt (pure stdlib, deterministic)."""

import os

PLAN = (
    "Day 1: pull 200 plumbers off Google Maps with stale profiles. "
    "Email each: free week of review replies and posts, then $99/month. "
    "Spend $100 on a domain, email tool, API credits. "
    "Deliver by code in hours, 24/7. "
    "Win 8 clients by day 30: ~$800 in. "
    "Edge: humans charge $500+."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(PLAN)
