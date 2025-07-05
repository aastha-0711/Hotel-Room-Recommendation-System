import os
import requests
from pandas import read_csv

# Create folder if not exists
os.makedirs("static/images", exist_ok=True)

# Load image URLs from CSV
data = read_csv("listings.csv")
images = data['picture_url'].tolist()

# Headers to avoid 403 Forbidden
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36',
    'Referer': 'https://www.airbnb.com/'  # Helps in some cases
}

# Log failed URLs
failed_urls = []

# Download images in range
for i in range(1000, min(1500, len(images))):  # change range if needed
    try:
        url = images[i]
        filename = url.split("/")[-1]
        if '.' not in filename:
            filename += '.jpg'  # Ensure proper extension

        path = f"static/images/{filename}"

        # Skip already downloaded
        if os.path.exists(path):
            print(f"{i + 1} / {len(images)}: Skipped -> {filename}")
            continue

        # Send request
        response = requests.get(url, headers=headers, timeout=10)

        # Success
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)
            print(f"{i + 1} / {len(images)}: Downloaded -> {path}")
        else:
            print(f"{i + 1} / {len(images)}: Failed -> {response.status_code} {response.reason}")
            failed_urls.append(url)

    except Exception as e:
        print(f"{i + 1} / {len(images)}: Error -> {e}")
        failed_urls.append(url)

# Save failed URLs to file
if failed_urls:
    with open("failed_urls.txt", "w") as f:
        f.write("\n".join(failed_urls))
    print(f"\nSaved {len(failed_urls)} failed URLs to 'failed_urls.txt'")
else:
    print("\n✅ All downloads successful in this batch.")
