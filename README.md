# Brand-Colored Website (Flask)

This is a complete Flask website styled **entirely** in your company logo colors (Blue & Green), with animations, CSS, vendor-style structure, JS, assets, and Jinja templates.

## Run Locally

```bash
cd pragnaware_site
pip install -r requirements.txt
python app.py
# visit http://127.0.0.1:5000
```

## Structure

```
pragnaware_site/
 ├─ app.py
 ├─ requirements.txt
 ├─ templates/
 │   ├─ base.html
 │   ├─ index.html
 │   ├─ about.html
 │   ├─ services.html
 │   └─ contact.html
 └─ static/
     ├─ css/style.css
     ├─ js/main.js
     ├─ vendor/        # place any external libs here if you want
     └─ assets/
         ├─ images/slide1.jpg
         └─ images/slide2.jpg
```

## Change Brand Colors

Open `app.py` -> `inject_globals()` and change `BRAND_PRIMARY` and `BRAND_ACCENT` hex values to your exact logo colors.

## Notes

- The "vendor" folder is included for organization. You can drop third-party libs there if needed.
- The site includes:
  - Animated hero slider
  - Reveal-on-scroll animations
  - Smooth navigation
  - Cards, badges, buttons styled in brand colors
```
