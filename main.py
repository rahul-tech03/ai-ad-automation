import csv
import json
from openai_copy import generate_ads
from heygen_video import create_video

with open("products.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"Processing product: {row['product_name']}")

        ads_json = generate_ads(row["description"], row["audience"])
        ads = json.loads(ads_json)["ads"]

        for index, ad in enumerate(ads):
            print(f"  Creating video {index + 1}")
            video_response = create_video(ad["script"])
            print(video_response)
