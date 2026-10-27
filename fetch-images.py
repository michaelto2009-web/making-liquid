#!/usr/bin/env python3
"""Downloads the 7 background images for the liquid glass demo.
Run once inside the liquid-glass-site folder:  python3 fetch-images.py
Files land in ./images/  (delete old ones first if re-running after an update)
"""
import urllib.request, os

IMAGES = [
    ("https://images.pexels.com/photos/17186345/pexels-photo-17186345.jpeg?auto=compress&cs=tinysrgb&w=3840", "images/bg-1.jpg"),
    ("https://images.unsplash.com/photo-1504707748692-419802cf939d?w=3840&q=85&auto=format&fit=crop", "images/bg-2.jpg"),
    ("https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=3840&q=85&auto=format&fit=crop", "images/bg-3.jpg"),
    ("https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=3840&q=85&auto=format&fit=crop", "images/bg-4.jpg"),
    ("https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=3840&q=85&auto=format&fit=crop", "images/bg-5.jpg"),
    ("https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=3840&q=85&auto=format&fit=crop", "images/bg-6.jpg"),
    ("https://images.unsplash.com/photo-1552053831-71594a27632d?w=3840&q=85&auto=format&fit=crop", "images/bg-7.jpg"),
    ("https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=3840&q=85&auto=format&fit=crop", "images/bg-8.jpg"),
]
FALLBACK = "https://picsum.photos/id/10/3840/2160"

os.makedirs("images", exist_ok=True)
ok = True
for url, path in IMAGES:
    try:
        print("downloading:", path)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=120).read()
        if len(data) < 10000: raise IOError("too small (%d bytes)" % len(data))
        open(path, "wb").write(data)
        print("  -> %d KB" % (len(data)//1024))
    except Exception as e:
        print("  FAILED (%s), trying fallback..." % e)
        try:
            data = urllib.request.urlopen(FALLBACK, timeout=60).read()
            open(path, "wb").write(data)
        except Exception as e2:
            print("  fallback also failed:", e2); ok = False
print("DONE" if ok else "Some images failed - re-run to retry.")
