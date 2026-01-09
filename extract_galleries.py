import requests
import re
import json
from pathlib import Path

projects = {
    'vases': 'https://gulerhirsch.com/vases-1',
    'stratum': 'https://gulerhirsch.com/stratum',
    'cloud': 'https://gulerhirsch.com/shall-i-be-a-cloud-2',
    'graces': 'https://gulerhirsch.com/3-graces'
}

all_images = {}

for name, url in projects.items():
    print(f"\n{'='*60}")
    print(f"Fetching {name} from {url}...")
    print('='*60)
    
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    # Find all image URLs
    image_urls = re.findall(r'https://cdn\.myportfolio\.com/[^"\'>\s]+\.(?:jpg|jpeg|png|webp)[^"\'>\s]*', response.text)
    
    # Filter to get only the high-res versions (_rw_1200 or _rw_1920)
    unique_images = {}
    for img_url in image_urls:
        # Extract the base ID
        match = re.search(r'([a-f0-9-]+)_rw_(\d+)', img_url)
        if match:
            img_id = match.group(1)
            size = int(match.group(2))
            
            # Keep the largest version of each image
            if img_id not in unique_images or size > unique_images[img_id][1]:
                unique_images[img_id] = (img_url, size)
    
    # Get just the URLs
    final_images = [url for url, size in unique_images.values()]
    
    all_images[name] = final_images
    print(f"Found {len(final_images)} unique images")
    for i, img_url in enumerate(final_images, 1):
        print(f"  {i}. {img_url[:80]}...")

# Save to JSON
with open('gallery_images.json', 'w') as f:
    json.dump(all_images, f, indent=2)

print(f"\n{'='*60}")
print(f"✅ Saved to gallery_images.json")
print(f"Total images found: {sum(len(v) for v in all_images.values())}")
print('='*60)
