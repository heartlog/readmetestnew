import os


readme = root / "README.md"
readme_contents = readme.open().read()

rewritten = "Test completed !"
readme.open("w").write(rewritten * 10)
