# glue-docker
Testing AWS Glue in local docker container

## Logger solution

```python
from pyspark.context import SparkContext
from awsglue.context import GlueContext
sc = SparkContext.getOrCreate()
logger = GlueContext(sc).get_logger()
```

