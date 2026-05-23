import kagglehub
import shutil
import os

# Download
path = kagglehub.competition_download('house-prices-advanced-regression-techniques')
print(f"Downloaded to: {path}")

# Copy to data/raw/
source_train = os.path.join(path, 'train.csv')
source_test = os.path.join(path, 'test.csv')

dest_dir = 'data/raw'
os.makedirs(dest_dir, exist_ok=True)

shutil.copy(source_train, os.path.join(dest_dir, 'train.csv'))
shutil.copy(source_test, os.path.join(dest_dir, 'test.csv'))

print("✓ Files copied to data/raw/")
