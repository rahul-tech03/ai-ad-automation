import json
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
def generate_ads():
    product_name = "Smart Water Bottle"
    description = (
        "A smart water bottle that tracks hydration, "
        "sends reminders via LED alerts and mobile notifications, "
        "syncs with fitness apps, and keeps water cold for 24 hours."
    )
    audience = "Fitness enthusiasts, office workers, health-conscious individuals"

    prompt = f"""
You are a performance marketing expert.

Create 3 ad variations for the following product.

For each variation, generate:
- A hook (under 7 seconds)
- A headline
- A 15-second video script

Each variation should use a different angle:
1. Pain point
2. Benefit driven
3. Curiosity based

Product Name:
{product_name}

Product Description:
{description}

Target Audience:
{audience}

Return ONLY valid JSON in this exact format:
{{
  "product": "{product_name}",
  "ads": [
    {{
      "hook": "",
      "headline": "",
      "script": ""
    }}
  ]
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    # Extract raw text
    raw_output = response.choices[0].message.content.strip()

    # Parse JSON safely
    try:
        parsed_output = json.loads(raw_output)
    except json.JSONDecodeError as e:
        print("Failed to parse OpenAI response as JSON")
        print("Raw response:")
        print(raw_output)
        raise e

    # Write JSON to file
    output_file = "openai_output.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(parsed_output, f, indent=2)

    print(f"OpenAI output saved to {output_file}")

if __name__ == "__main__":
    generate_ads()