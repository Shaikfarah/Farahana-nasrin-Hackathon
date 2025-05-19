import argparse, cv2, numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import json, os

def load_image(path_or_url):
    if path_or_url.startswith('http'):
        import requests, io
        resp = requests.get(path_or_url)
        img = Image.open(io.BytesIO(resp.content)).convert('RGB')
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    else:
        return cv2.imread(path_or_url)

def extract_colors(img, k=5):
    img_resized = cv2.resize(img, (600, 400))
    pixels = img_resized.reshape(-1, 3)
    kmeans = KMeans(n_clusters=k, n_init='auto').fit(pixels)
    colors = np.round(kmeans.cluster_centers_).astype(int)
    return colors

def to_hex(color):
    return '#%02x%02x%02x' % tuple(color.astype(int))

def main():
    parser = argparse.ArgumentParser(description='Detect dominant colors')
    parser.add_argument('--image', required=True, help='Image path or URL')
    parser.add_argument('--colors', type=int, default=5, help='Number of colors')
    parser.add_argument('--out', default='palette.json', help='Output JSON')
    args = parser.parse_args()

    img = load_image(args.image)
    colors = extract_colors(img, args.colors)
    palette = [{'rgb': color.tolist(), 'hex': to_hex(color)} for color in colors]

    with open(args.out, 'w') as f:
        json.dump(palette, f, indent=2)

    print(f'Palette saved to {args.out}')
    for c in palette:
        print(c)

if __name__ == '__main__':
    main()
