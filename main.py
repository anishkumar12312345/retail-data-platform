from src.extract.extract import *
from src.transform.transform import *
from src.load.load import *
from src.quality.validate import validate

orders = validate(orders)

print("Validation Completed")
print("Pipeline Completed")