#!/usr/bin/env python3
"""Download all anecdote images from Squarespace CDN."""
import urllib.request
import os
import ssl

# Disable SSL verification for squarespace CDN
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "assets", "images")

def dl(url, path):
    full = os.path.join(IMG, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    if os.path.exists(full) and os.path.getsize(full) > 100:
        print(f"  SKIP (exists): {path}")
        return
    print(f"  Downloading: {path}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = resp.read()
        with open(full, "wb") as f:
            f.write(data)
        print(f"    OK ({len(data)} bytes)")
    except Exception as e:
        print(f"    ERROR: {e}")

# === THUMBNAILS ===
print("=== Thumbnails ===")
thumbnails = [
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1616191738735-CK11CKKPFID8MW5XMMDA/Screen+Shot+2021-03-19+at+6.08.29+PM.png", "anecdotes-thumbnails/mycelium.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613623020686-AOAHK721V9ZYWS0P1XX2/Frame+12+%282%29.png", "anecdotes-thumbnails/thegoodmeal.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613624462915-H9T3Y4J0OCIF7WLVM4GW/0329BE5B-8C21-45D9-933C-740A10103565.JPG", "anecdotes-thumbnails/plastic-world.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613694007922-HEMOWVOBOVYEEPJBKS6E/Screen+Recording+2020-02-19+at+11.13+AM.gif", "anecdotes-thumbnails/physical-design.gif"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613624219957-M2NQHLDFBMCX7P6ACELO/Edited+IMG_3249.png", "anecdotes-thumbnails/laundry-machine.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613695502375-AMDS879WG7XQBHNTX81F/Binder3_Page_4.jpg", "anecdotes-thumbnails/mckinsey.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613623981619-YMO7KSBXC323GY9X03ER/Screen+Shot+2021-02-17+at+11.51.02+PM.png", "anecdotes-thumbnails/metaphor-animation.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613624053487-26GQ5MSR28CFRIRTY25W/Screen+Shot+2021-02-17+at+11.53.59+PM.png", "anecdotes-thumbnails/post-series.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613623073311-5JXQ50IN09U576C61I7S/IMG_3592.JPG", "anecdotes-thumbnails/magic-thinking.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613623462198-1LCN6RSPAZAW209UG1AG/Mind+Map+%283%29.jpg", "anecdotes-thumbnails/fake-news.jpg"),
]
for url, path in thumbnails:
    dl(url, path)

# === MYCELIUM ===
print("\n=== Mycelium ===")
mycelium = [
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1616188578295-DG61TCL0L4QJOSNACWRL/Screen+Shot+2020-10-29+at+4.32.23+PM.png", "anecdotes-mycelium/hero.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1616188624092-QCAX0000253BUA5J464J/Screen+Shot+2021-03-19+at+5.15.52+PM.png", "anecdotes-mycelium/screenshot-2.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1616187814020-8HVNUG91LV02AXTCP81O/Screen+Recording+2020-10-21+at+08.34+PM.gif", "anecdotes-mycelium/animation.gif"),
]
for url, path in mycelium:
    dl(url, path)

# === THEGOODMEAL ===
print("\n=== TheGoodMeal ===")
thegoodmeal = [
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/6e2b56bd-59ff-4233-b3b0-b64da91a498a/Asset+1%402x+copy.png", "anecdotes-thegoodmeal/hero.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/3619a7ba-2473-4ddf-8565-b73bc40eaf48/IMG_3110.JPG", "anecdotes-thegoodmeal/img-3110.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/8609e76c-a405-4107-9c26-7b2a83d783d0/IMG_1887+copy.JPG", "anecdotes-thegoodmeal/img-1887.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/0015e90f-34bd-4bab-b9ea-d45938756460/Screen+Shot+2020-01-15+at+10.53.28+PM.png", "anecdotes-thegoodmeal/screenshot.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/9b8d0fd7-e64c-4206-a0c7-83608ef8c3f1/Garfield2.JPG", "anecdotes-thegoodmeal/garfield.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/09e30f48-da9a-407a-8794-814a03010886/Meal2.JPG", "anecdotes-thegoodmeal/meal.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1730dd70-56b2-4dbd-b0db-99c3b3d1bcb2/IMG_3505+2.JPG", "anecdotes-thegoodmeal/img-3505.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/82ad311a-b09d-4cdd-8006-57bfb1ad176d/IMG_3498.JPG", "anecdotes-thegoodmeal/img-3498.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/6246ca85-8fbb-4fa5-bbaf-952ae36d7b27/IMG_1872.JPG", "anecdotes-thegoodmeal/img-1872.jpg"),
]
for url, path in thegoodmeal:
    dl(url, path)

# === PLASTIC WORLD ===
print("\n=== Plastic World ===")
plastic = [
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613693352833-EWADXVJPN0SYCIQ4FB58/Screen+Shot+2020-04-18+at+1.44.31+PM.png", "anecdotes-plastic-world/hero.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1616187313204-LZS8FBSO2KTXSZUH5AO0/0329BE5B-8C21-45D9-933C-740A10103565.JPG", "anecdotes-plastic-world/artifact.jpg"),
]
for url, path in plastic:
    dl(url, path)

# === PHYSICAL DESIGN ===
print("\n=== Physical Design ===")
physical = [
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613694438050-YITOA0A46YVQS65RZXS8/Screen+Recording+2020-02-19+at+11.13+AM.gif", "anecdotes-physical-design/3d-printing.gif"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613694253434-0N7EEZLLZ7WFO7AD6V8G/6799F5DA-AA83-4AD4-863A-C90E985F141F.JPG", "anecdotes-physical-design/fusion360.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613694809354-1GISSLPNSMJA3JXNY6NM/IMG_4028.JPG", "anecdotes-physical-design/cnc-1.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613694831783-NA89DCED3GDT3QRIZGCO/IMG_4038.JPG", "anecdotes-physical-design/cnc-2.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613694917340-HY7YR9W9Z2HKXDELJXPP/IMG_4043.JPG", "anecdotes-physical-design/laser-1.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613694945122-67C92T0Y5R51RWVEQ4OH/IMG_4074.JPG", "anecdotes-physical-design/laser-2.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613695028948-3YJN19F0HY1ACNZ6HTN5/IMG_3994.JPG", "anecdotes-physical-design/arduino-1.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613695210129-A29X2HGGKDJC0ASHPDE4/IMG_4089.JPG", "anecdotes-physical-design/arduino-2.jpg"),
]
for url, path in physical:
    dl(url, path)

# === LAUNDRY MACHINE (no content images found on live site, only logo) ===
# Use the thumbnail as the hero image
print("\n=== Laundry Machine ===")
laundry = [
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613624219957-M2NQHLDFBMCX7P6ACELO/Edited+IMG_3249.png", "anecdotes-laundry-machine/hero.png"),
]
for url, path in laundry:
    dl(url, path)

# === MCKINSEY ===
print("\n=== McKinsey ===")
mckinsey = [
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613677929234-CYC3WULL7NMBQJ6KB5R9/Attemp+3_Page_4.jpg", "anecdotes-mckinsey/hero.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613677881008-I1BBAMD68QX6MYAP568U/Smor+Gif.gif", "anecdotes-mckinsey/smor.gif"),
]
for url, path in mckinsey:
    dl(url, path)

# === METAPHOR ANIMATION (no content images found, only logo) ===
# Use the thumbnail as hero
print("\n=== Metaphor Animation ===")
metaphor = [
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613623981619-YMO7KSBXC323GY9X03ER/Screen+Shot+2021-02-17+at+11.51.02+PM.png", "anecdotes-metaphor-animation/hero.png"),
]
for url, path in metaphor:
    dl(url, path)

# === POST SERIES ===
print("\n=== Post Series ===")
post_series = [
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/d97c3281-7e2c-4d05-b91c-ffb61856fde6/Artboard+16.png", "anecdotes-post-series/artboard-16.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/6fcfa79f-2420-4fcf-a07b-149acc5a9511/F1A80169-B743-4529-9BB4-3A5B99DAE13F.JPG", "anecdotes-post-series/photo.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/e386ea0f-b7ac-468f-bb94-56e725f15dc7/Artboard+16+copy.png", "anecdotes-post-series/artboard-16-copy.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/112915e6-ef78-4298-a08b-fea24e08688c/Screen+Shot+2020-01-15+at+9.40.34+PM.png", "anecdotes-post-series/screenshot-1.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/8e620144-9525-4737-802b-49121ca0a3af/Artboard+3+copy+2.png", "anecdotes-post-series/artboard-3-copy-2.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/14bd515d-55dd-4e87-80fb-5b3d135b14b3/Artboard+20.png", "anecdotes-post-series/artboard-20.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/c3216a35-db40-4314-afa8-f25a15772060/Artboard+3+copy.png", "anecdotes-post-series/artboard-3-copy.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/e06e96e3-12bd-4554-997d-b42b771e6eec/Screen+Shot+2020-01-15+at+9.40.52+PM.png", "anecdotes-post-series/screenshot-2.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/f686da7d-4f4d-487b-9722-c0be4144718e/Artboard+10.png", "anecdotes-post-series/artboard-10.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/a5398331-e6a1-4436-9847-7f8c93b5a3d3/Screen+Shot+2020-01-15+at+9.41.24+PM.png", "anecdotes-post-series/screenshot-3.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/fa9e7151-1d21-4617-a183-58b52c8ceeaf/Screen+Shot+2020-01-15+at+9.46.11+PM.png", "anecdotes-post-series/screenshot-4.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/fbde5630-05c8-4816-afa5-bc76f3b85d3e/Artboard+1+copy.png", "anecdotes-post-series/artboard-1-copy.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/546d76b9-06f3-42d9-b8e3-4aacc5dcf62c/Artboard+8+copy.png", "anecdotes-post-series/artboard-8-copy.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/c4a982c8-7b77-4c33-b8ef-11545aa71109/Artboard+1.png", "anecdotes-post-series/artboard-1.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/a2665310-9e1c-42b9-9e65-5ac7d38358a5/Artboard+8+copy+2.png", "anecdotes-post-series/artboard-8-copy-2.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/50e0ca5c-173c-4f93-ba25-13a359131e4b/Artboard+8.png", "anecdotes-post-series/artboard-8.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/71d9fa6c-8b6a-4055-972a-a7585d0ed8d7/Artboard+10+copy.png", "anecdotes-post-series/artboard-10-copy.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/33c672a2-1038-4511-9147-ae03490a2ca1/Artboard+14+copy.png", "anecdotes-post-series/artboard-14-copy.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/f0977a1d-737a-4dd5-9a9c-63a0a0c2fcad/Artboard+14.png", "anecdotes-post-series/artboard-14.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/19f61efb-c5fa-48a6-9f5c-7c444ca82714/Artboard+16+copy+2.png", "anecdotes-post-series/artboard-16-copy-2.png"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/e26a8dbc-ec2b-4654-9b89-180fe021d10a/Artboard+3.png", "anecdotes-post-series/artboard-3.png"),
]
for url, path in post_series:
    dl(url, path)

# === MAGIC THINKING ===
print("\n=== Magic Thinking ===")
magic = [
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1615853800207-AW6SE0TTXGGUDZ8JDX2D/IMG_3592.JPG", "anecdotes-magic-thinking/hero.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/04bc1927-e295-4801-9912-11234a73ab01/IMG_3592.JPG", "anecdotes-magic-thinking/img-3592.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/b9161bc6-f8f7-4957-88cd-338c55873e0d/IMG_3596.JPG", "anecdotes-magic-thinking/img-3596.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/cd4c7443-d51d-499f-bb6c-2ae906af2ae1/IMG_3590.JPG", "anecdotes-magic-thinking/img-3590.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/dccbb1ab-5d0c-4519-8aa1-0f47ccf80872/IMG_3586.JPG", "anecdotes-magic-thinking/img-3586.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/60b16832-55d2-4f65-8689-adffad975377/IMG_3588.JPG", "anecdotes-magic-thinking/img-3588.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/c65223d8-e444-4a55-8833-acfb09ccda59/IMG_3589.JPG", "anecdotes-magic-thinking/img-3589.jpg"),
]
for url, path in magic:
    dl(url, path)

# === FAKE NEWS ===
print("\n=== Fake News ===")
fakenews = [
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613674556656-RO08A7O411SAZR2FIDFU/Mind+Map.jpg", "anecdotes-fake-news/mind-map.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5fffe215879bf154c30dd438/1613674371502-KAYLQM0SA7YD4FICZ94H/Mind+Map+%282%29.jpg", "anecdotes-fake-news/mind-map-2.jpg"),
]
for url, path in fakenews:
    dl(url, path)

print("\n=== DONE ===")
