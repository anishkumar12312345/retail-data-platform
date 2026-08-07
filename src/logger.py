import logging

logging.basicConfig(
    filename="src/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Retail Data Platform Started")
print("Logging Started")