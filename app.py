import numpy as np
import pandas as pd
import cv2
import os
from DeepImageSearch import LoadData, SearchImage

# ---------- Load Dataset ----------
print("\n🔄 Loading images and metadata...")
try:
    image_list = LoadData().from_folder(folder_list=['images'])
except Exception as e:
    print("❌ Error loading images:", e)
    exit()

try:
    data = pd.read_csv("listings.csv")
    name_list = data['name'].tolist()
    desc_list = data['description'].tolist()
    cap_list = data['accommodates'].tolist()
    book_list = data['listing_url'].tolist()
    price_list = data['price'].tolist()
    tag_list = data['amenities'].tolist()
    rating_list = data['review_scores_rating'].tolist()
except Exception as e:
    print("❌ Error loading listings.csv:", e)
    exit()

# ---------- Title ----------
print("\n📘 CSE3013 Artificial Intelligence Project Review 2")
print("📌 Title: Hotel Room Recommendation System Using Image Similarity")
print("👥 Team Members:\n19BCI0001: Dayeem Parkar\n19BCI0036: Akashdeep\n19BCE0891: Anmol")

# ---------- User Input ----------
try:
    ipImg = input("\n🖼️ Enter filename (e.g., room1.jpg): ").strip()
    image_path = os.path.join("images", ipImg)
    if not os.path.isfile(image_path):
        print(f"❌ Image file '{ipImg}' not found in 'images/' folder.")
        exit()

    matches = int(input("🔢 Enter number of desired recommendations: "))
    if matches <= 0:
        raise ValueError("Number of recommendations must be positive.")

except Exception as e:
    print("❌ Invalid input!", e)
    exit()

# ---------- Find Matches ----------
print("\n🔍 Finding similar rooms...")
try:
    result = SearchImage().get_similar_images(image_path, number_of_images=matches)
except Exception as e:
    print("❌ Error in finding similar images:", e)
    exit()

# ---------- Display Results ----------
print("\n🏨 Best room matches:")
counter = 1
for key in result.keys():
    print(f"\n{'=' * 60}\n{counter}. \033[1mName:\033[0m {name_list[key]}")
    print("🔗 Book Room:", book_list[key])
    print("👥 Accommodates:", cap_list[key])
    print("💵 Price:", price_list[key])
    print("📝 Description:", desc_list[key])
    print("⭐ Rating:", "Not Rated" if pd.isna(rating_list[key]) else rating_list[key])
    print("🏷️ Tags:", tag_list[key])
    print("🖼️ Image File:", result[key])

    # ---------- Show Image ----------
    img = cv2.imread(result[key])
    if img is None:
        print("⚠️ Could not load image:", result[key])
    else:
        cv2.imshow(f"Match {counter}", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    counter += 1
