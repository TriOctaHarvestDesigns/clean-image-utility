"""
clean_images_recursive.py — Tri-Octa Harvest Designs Utility
Removes metadata (EXIF, device info, timestamps, etc.) from PNG and JPG images.

Now scans through all sub-folders automatically.

Usage:
1. Place this script at the root of the directory you want cleaned.
2. Run in PowerShell or Terminal:
       python clean_images_recursive.py
3. Cleaned copies are saved as  clean_<originalname>.<ext>  beside each file.
"""

import os
from PIL import Image

def clean_metadata(folder_path):
    cleaned = 0
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                file_path = os.path.join(root, filename)
                try:
                    with Image.open(file_path) as img:
                        data = list(img.getdata())
                        clean = Image.new(img.mode, img.size)
                        clean.putdata(data)
                        base, ext = os.path.splitext(filename)
                        clean_name = f"clean_{base}{ext}"
                        clean_path = os.path.join(root, clean_name)
                        clean.save(clean_path)
                        cleaned += 1
                        print(f"✅  {os.path.relpath(file_path, folder_path)} → {clean_name}")
                except Exception as e:
                    print(f"⚠️  Skipped {filename}: {e}")
    print(f"\n✨ Done! {cleaned} images cleaned.\n")

if __name__ == "__main__":
    folder = input("Enter folder path (default: current folder): ").strip() or "."
    if not os.path.exists(folder):
        print("❌ Folder not found.")
    else:
        clean_metadata(folder)
