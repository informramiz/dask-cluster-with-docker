import pandas as pd
import numpy as np
import time
import logging
import dask.dataframe as dd
from distributed import Client


logging.getLogger(__name__)\
    .info("Wating for cluster to come online")

time.sleep(30)


logging.getLogger(__name__)\
    .info("======= TESTING DASK CLUSTER ========")

c = Client('dask-scheduler:8786')

data = np.arange(10000)

df = pd.DataFrame(dict(col1=data, col2=data[::-1]))

ddf = dd.from_pandas(df, npartitions=10)

c.scatter(ddf)

logging.getLogger(__name__)\
    .info("Submitting job...")

res = dd.concat([ddf.sum(), ddf.loc[:500].sum()],
                interleave_partitions=True).compute()

logging.getLogger(__name__)\
    .info("Result:\n{}".format(str(res)))

logging.getLogger(__name__)\
    .info("======= CLUSTER OK ========")

print(res)