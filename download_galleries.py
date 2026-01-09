import requests
import json
from pathlib import Path
import time

# Load the image URLs
with open('gallery_images.json', 'r') as f:
    all_images = json.load(f)

# Create output directory
output_dir = Path('public/img/galleries')
output_dir.mkdir(parents=True, exist_ok=True)

total_downloaded = 0

for project_name, image_urls in all_images.items():
    print(f"\n{'='*60}")
    print(f"Downloading {len(image_urls)} images for {project_name}...")
    print('='*60)
    
    # Create project directory
    project_dir = output_dir / project_name
    project_dir.mkdir(exist_ok=True)
    
    for i, url in enumerate(image_urls, 1):
        # Extract filename from URL
        filename = f"{project_name}_{i:02d}.jpg"
        filepath = project_dir / filename
        
        try:
            print(f"  [{i}/{len(image_urls)}] Downloading {filename}...", end=' ')
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
            response.raise_for_status()
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            file_size = len(response.content) / 1024  # KB
            print(f"✓ ({file_size:.1f} KB)")
            total_downloaded += 1
            
            # Be nice to the server
            time.sleep(0.5)
            
        except Exception as e:
            print(f"✗ Error: {e}")

print(f"\n{'='*60}")
print(f"✅ Downloaded {total_downloaded} images to {output_dir}")
print('='*60)
