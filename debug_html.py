import requests

url = 'https://gulerhirsch.com/vases-1'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

with open('vases_page.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

print("Saved HTML to vases_page.html")
print(f"Page size: {len(response.text)} characters")

# Look for image patterns
import re
image_urls = re.findall(r'https://[^"\'>\s]+\.(?:jpg|jpeg|png|webp)[^"\'>\s]*', response.text)
print(f"\nFound {len(image_urls)} potential image URLs")
for url in image_urls[:20]:
    print(f"  {url}")
