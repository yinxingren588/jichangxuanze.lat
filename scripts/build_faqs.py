# -*- coding: utf-8 -*-
import json
import os
import sys

# Add current dir to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_cat1_client import CLIENT_FAQS
from data_cat2_connection import CONNECTION_FAQS
from data_cat3_ai import AI_FAQS
from data_cat4_streaming import STREAMING_FAQS
from data_cat5_routing import ROUTING_FAQS
from data_cat6_subscription import SUBSCRIPTION_FAQS
from data_cat7_protocols import PROTOCOLS_FAQS
from data_cat8_hardware import HARDWARE_FAQS

all_faqs = (
    CLIENT_FAQS +
    CONNECTION_FAQS +
    AI_FAQS +
    STREAMING_FAQS +
    ROUTING_FAQS +
    SUBSCRIPTION_FAQS +
    PROTOCOLS_FAQS +
    HARDWARE_FAQS
)

print(f"Total FAQs aggregated: {len(all_faqs)}")
assert len(all_faqs) == 150, f"Expected 150 FAQs, got {len(all_faqs)}"

# Check duplicate slugs
slugs = [faq["slug"] for faq in all_faqs]
duplicate_slugs = set([x for x in slugs if slugs.count(x) > 1])
if duplicate_slugs:
    print(f"Error: Duplicate slugs found: {duplicate_slugs}")
    sys.exit(1)

# Check duplicate IDs
ids = [faq["id"] for faq in all_faqs]
duplicate_ids = set([x for x in ids if ids.count(x) > 1])
if duplicate_ids:
    print(f"Error: Duplicate IDs found: {duplicate_ids}")
    sys.exit(1)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "data", "faqs.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_faqs, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(all_faqs)} professional FAQs to {output_path}!")
