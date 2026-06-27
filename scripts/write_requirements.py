"""requirements.txt: Python dependencies for GFP Design Project"""
packages = """openpyxl>=3.1.0
requests>=2.31.0
biopython>=1.81
pandas>=2.0.0
numpy>=1.24.0
"""
with open('D:\\openclaw_work\\GFP-Design-SynBio2026\\requirements.txt', 'w') as f:
    f.write(packages.strip())
print("requirements.txt written")
