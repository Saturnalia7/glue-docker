import logging
from typing import Union

# Set logging base properties
# If spark logger, set properties


def get_logger():
    try:
        from pyspark.context import SparkContext
        from awsglue.context import GlueContext

        sc = SparkContext.getOrCreate()
        # This is a py4j.java_gateway.JavaObject
        logger = GlueContext(sc).get_logger()
    except:
        # This is a logging.logger
        logger = logging.getLogger(__name__)

    return logger
