import shutil
import os

src = r"C:\Users\charl\learning-narrative-kit\scratch\comic_card_mockup.html"
dst = r"C:\Users\charl\learning-narrative-kit\docs\comic_card_mockup.html"

shutil.copy2(src, dst)
print("Copied mockup to docs/comic_card_mockup.html for GitHub Pages / browser preview.")
