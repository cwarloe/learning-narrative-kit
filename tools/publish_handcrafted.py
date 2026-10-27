import shutil

src = r"C:\Users\charl\learning-narrative-kit\scratch\handcrafted_cards_mockup.html"
dst = r"C:\Users\charl\learning-narrative-kit\docs\handcrafted_cards_mockup.html"

shutil.copy2(src, dst)
print("Copied handcrafted cards mockup to docs/handcrafted_cards_mockup.html.")
