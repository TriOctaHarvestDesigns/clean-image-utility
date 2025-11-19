# clean-image-utility
Remove hidden metadata (EXIF, device info, timestamps, editor history) from all PNG and JPG images in your entire directory tree. Perfect for creators, developers, PKM users, and anyone preparing screenshots for public release. This utility recursively scans every subfolder under a directory, generates safe, metadata-free duplicates of each image.

# 🧽 Clean Images Utility — v1.1
**By Tri-Octa Harvest Designs**

Remove hidden metadata (EXIF, timestamps, device info) from your screenshots and images in seconds.
Keep your work clean, private, and ready for public release.

---

## 🚀 Quick Start

1. Place `clean_images_recursive.py` in the folder containing your screenshots.
2. Open **PowerShell**, **Terminal**, or **VS Code** in that directory.
3. Run:

   ```
   python clean_images_recursive.py
   ```
4. Press Enter to use the current folder, or provide a custom path.
5. The tool scans through **all subfolders**, cleaning every `.png`, `.jpg`, or `.jpeg`.

Each cleaned image is saved beside the original as:

```
clean_<originalname>.png
```

---

## ⚙️ Features

* 🔍 **Recursive cleaning:** Scans all sub-folders automatically.
* 🧼 **No quality loss:** Rebuilds each image pixel-for-pixel without EXIF data.
* 🗂️ **Safe workflow:** Originals remain untouched; cleaned copies are saved separately.
* 🧠 **Cross-platform:** Works on Windows, macOS, and Linux.
* ⚙️ **Lightweight dependency:** Only requires `Pillow` (`pip install pillow`).
* 🔐 **Perfect for releases:** Remove metadata before uploading screenshots, previews, or artwork.

---

## 🧭 Notes & Best Practices

* Works great as a final “cleaning pass” before sharing images publicly or uploading product materials.
* You can safely run it on your entire Tri-Octa bundle directory — it only affects image files.
* Ideal companion to the **ChatGPT Splitter** and **Folder Generator** utilities for complete workflow hygiene.

---

### 🪶 Credits

Created by **Tri-Octa Harvest Designs (2025)**
Part of the **Productivity Tools Collection**

