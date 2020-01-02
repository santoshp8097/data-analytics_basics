# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 18:35:36 2020

@author: Santosh
"""

#list to pandas conversion
import pandas as pd
import numpy as np
np_array=np.array([1,2,3,4,5])
print(np_array)
new=pd.series(np_array)
print(new)


## pandas to list 

import pandas as pd
import numpy as np
new=pd.series([1,2,3,4])
print(new)
print(new.tolist())


##dictonory to pandas and list 

import pandas as pd
import numpy as np
ds={'a':1,'b':2,'c':6,'d':7}
print(ds)
print(pd.series(ds))
print(ds.tolist())
ds=list(data.values())
print(ds)
