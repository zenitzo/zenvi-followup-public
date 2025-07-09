import sys
import os
import importlib

# Fix sys.path to include root
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

if len(sys.argv) < 3 or sys.argv[1] != "--product":
    print("Usage: python run.py --product <product_name>")
    sys.exit(1)

product = sys.argv[2]
module_path = f"zens_engine.products.{product}.main"
print(f"🧪 Importing: {module_path}")  # Debug line

try:
    importlib.import_module(module_path)
except ModuleNotFoundError as e:
    print(f"❌ Could not find main.py for product: {product}")
    print("Error detail:", e)