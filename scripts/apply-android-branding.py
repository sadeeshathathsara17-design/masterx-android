from pathlib import Path
import xml.etree.ElementTree as ET
import shutil

base = Path("android/app/src/main")
source = Path("assets/masterx-study-icon.png")
if not source.exists():
    raise SystemExit("MasterX Study icon is missing")

# Use a drawable resource so the supplied circular artwork remains intact.
drawable = base / "res/drawable-nodpi"
drawable.mkdir(parents=True, exist_ok=True)
shutil.copy2(source, drawable / "masterx_study_icon.png")

manifest = base / "AndroidManifest.xml"
tree = ET.parse(manifest)
root = tree.getroot()
ns = "{http://schemas.android.com/apk/res/android}"
application = root.find("application")
if application is None:
    raise SystemExit("Android manifest has no application element")
application.set(ns + "icon", "@drawable/masterx_study_icon")
application.set(ns + "roundIcon", "@drawable/masterx_study_icon")
tree.write(manifest, encoding="utf-8", xml_declaration=True)
print("Applied MasterX Study app name and logo")
