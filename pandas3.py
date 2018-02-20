import matplotlib.pyplot as plt
>>> import numpy as np
>>> import pandas as pd
>>> s=pd.Series([1,3,5,np.nan,6,8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> dates=pd.date_range('20130101', periods=6)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> dates=pd.date_range('20130101',periods=10)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06', '2013-01-07', '2013-01-08',
               '2013-01-09', '2013-01-10'],
              dtype='datetime64[ns]', freq='D')
>>> df2=pd.dataframe({'A':1.,
		      'b' : pd.Timestamp('20180101'),
		      'c' :np.array([3]*4,dtypes='int32'),
		      'd' :pd.Series(1,index=lisst(range(4)),dtype='float32'),
		      'e' : pd.Categorical(["test","train","test","train"]),
		      'f' : 'foo' })
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    df2=pd.dataframe({'A':1.,
AttributeError: module 'pandas' has no attribute 'dataframe'
>>> df2=pd.DataFrame({'A':1.,
		      'B' : pd.Timestamp('20180101'),
		      'C' :np.array([3]*4,dtypes='int32'),
		      'D' :pd.Series(1,index=lisst(range(4)),dtype='float32'),
		      'E' : pd.Categorical(["test","train","test","train"]),
		      'F' : 'foo' })
		      
Traceback (most recent call last):
  File "<pyshell#15>", line 3, in <module>
    'C' :np.array([3]*4,dtypes='int32'),
TypeError: 'dtypes' is an invalid keyword argument for this function
>>> df2=pd.DataFrame({'A':1.,
		      'B' : pd.Timestamp('20180101'),
		      'C' :np.array([3]*4,dtype='int32'),
		      'D' :pd.Series(1,index=lisst(range(4)),dtype='float32'),
		      'E' : pd.Categorical(["test","train","test","train"]),
		      'F' : 'foo' })
		      
Traceback (most recent call last):
  File "<pyshell#16>", line 4, in <module>
    'D' :pd.Series(1,index=lisst(range(4)),dtype='float32'),
NameError: name 'lisst' is not defined
>>> df2=pd.DataFrame({'A':1.,
		      'B' : pd.Timestamp('20180101'),
		      'C' :np.array([3]*4,dtype='int32'),
		      'D' :pd.Series(1,index=list(range(4)),dtype='float32'),
		      'E' : pd.Categorical(["test","train","test","train"]),
		      'F' : 'foo' })
		      
>>> df2
		      
     A          B  C    D      E    F
0  1.0 2018-01-01  3  1.0   test  foo
1  1.0 2018-01-01  3  1.0  train  foo
2  1.0 2018-01-01  3  1.0   test  foo
3  1.0 2018-01-01  3  1.0  train  foo
>>> x=pd.Timestamp('20180907')
		      
>>> x
		      
Timestamp('2018-09-07 00:00:00')
>>> df2.head(10)
		      
     A          B  C    D      E    F
0  1.0 2018-01-01  3  1.0   test  foo
1  1.0 2018-01-01  3  1.0  train  foo
2  1.0 2018-01-01  3  1.0   test  foo
3  1.0 2018-01-01  3  1.0  train  foo
>>> df2.tail(2)
		      
     A          B  C    D      E    F
2  1.0 2018-01-01  3  1.0   test  foo
3  1.0 2018-01-01  3  1.0  train  foo
>>> df2.index
		      
Int64Index([0, 1, 2, 3], dtype='int64')
>>> df2.columns
		      
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
>>> df2.T
		      
                     0                    1                    2  \
A                    1                    1                    1   
B  2018-01-01 00:00:00  2018-01-01 00:00:00  2018-01-01 00:00:00   
C                    3                    3                    3   
D                    1                    1                    1   
E                 test                train                 test   
F                  foo                  foo                  foo   

                     3  
A                    1  
B  2018-01-01 00:00:00  
C                    3  
D                    1  
E                train  
F                  foo  
>>> df2
		      
     A          B  C    D      E    F
0  1.0 2018-01-01  3  1.0   test  foo
1  1.0 2018-01-01  3  1.0  train  foo
2  1.0 2018-01-01  3  1.0   test  foo
3  1.0 2018-01-01  3  1.0  train  foo
>>> df=pd.DataFrame(np.random.randn(6,4),index=dates,column=list('ABCD'))
		      
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    df=pd.DataFrame(np.random.randn(6,4),index=dates,column=list('ABCD'))
TypeError: __init__() got an unexpected keyword argument 'column'
>>> df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
		      
Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 4624, in create_block_manager_from_blocks
    mgr = BlockManager(blocks, axes)
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 3033, in __init__
    self._verify_integrity()
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 3244, in _verify_integrity
    construction_error(tot_items, block.shape[1:], self.axes)
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 4608, in construction_error
    passed, implied))
ValueError: Shape of passed values is (4, 6), indices imply (4, 10)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 361, in __init__
    copy=copy)
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 533, in _init_ndarray
    return create_block_manager_from_blocks([values], [columns, index])
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 4631, in create_block_manager_from_blocks
    construction_error(tot_items, blocks[0].shape[1:], axes, e)
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 4608, in construction_error
    passed, implied))
ValueError: Shape of passed values is (4, 6), indices imply (4, 10)
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 4624, in create_block_manager_from_blocks
    mgr = BlockManager(blocks, axes)
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 3033, in __init__
    self._verify_integrity()
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 3244, in _verify_integrity
    construction_error(tot_items, block.shape[1:], self.axes)
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 4608, in construction_error
    passed, implied))
ValueError: Shape of passed values is (4, 6), indices imply (4, 10)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 361, in __init__
    copy=copy)
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 533, in _init_ndarray
    return create_block_manager_from_blocks([values], [columns, index])
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 4631, in create_block_manager_from_blocks
    construction_error(tot_items, blocks[0].shape[1:], axes, e)
  File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 4608, in construction_error
    passed, implied))
ValueError: Shape of passed values is (4, 6), indices imply (4, 10)
>>> df = pd.DataFrame(np.random.randn(10,4), index=dates, columns=list('ABCD'))
>>> df
                   A         B         C         D
2013-01-01 -0.584097 -0.672626  0.871800  0.009349
2013-01-02 -0.528538 -0.214885  0.191734 -0.486818
2013-01-03 -0.709967 -0.074022 -0.684967 -0.938910
2013-01-04 -1.532617  0.259219 -0.660099  0.990723
2013-01-05 -0.127941 -1.037672 -0.466913  0.859080
2013-01-06 -0.742694  1.599758  0.001832  0.152040
2013-01-07  0.587661  1.696389  1.367631  1.039936
2013-01-08 -0.626946  1.084674  0.851653 -1.087033
2013-01-09 -0.418993 -0.943578 -0.583818  1.286449
2013-01-10  1.887318 -0.984025 -1.201518 -1.223087
>>> df.sort_index(axis=1,ascending=False)
                   D         C         B         A
2013-01-01  0.009349  0.871800 -0.672626 -0.584097
2013-01-02 -0.486818  0.191734 -0.214885 -0.528538
2013-01-03 -0.938910 -0.684967 -0.074022 -0.709967
2013-01-04  0.990723 -0.660099  0.259219 -1.532617
2013-01-05  0.859080 -0.466913 -1.037672 -0.127941
2013-01-06  0.152040  0.001832  1.599758 -0.742694
2013-01-07  1.039936  1.367631  1.696389  0.587661
2013-01-08 -1.087033  0.851653  1.084674 -0.626946
2013-01-09  1.286449 -0.583818 -0.943578 -0.418993
2013-01-10 -1.223087 -1.201518 -0.984025  1.887318
>>> df.T
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06  \
A   -0.584097   -0.528538   -0.709967   -1.532617   -0.127941   -0.742694   
B   -0.672626   -0.214885   -0.074022    0.259219   -1.037672    1.599758   
C    0.871800    0.191734   -0.684967   -0.660099   -0.466913    0.001832   
D    0.009349   -0.486818   -0.938910    0.990723    0.859080    0.152040   

   2013-01-07  2013-01-08  2013-01-09  2013-01-10  
A    0.587661   -0.626946   -0.418993    1.887318  
B    1.696389    1.084674   -0.943578   -0.984025  
C    1.367631    0.851653   -0.583818   -1.201518  
D    1.039936   -1.087033    1.286449   -1.223087  
>>> df.sort_values(by='A')
                   A         B         C         D
2013-01-04 -1.532617  0.259219 -0.660099  0.990723
2013-01-06 -0.742694  1.599758  0.001832  0.152040
2013-01-03 -0.709967 -0.074022 -0.684967 -0.938910
2013-01-08 -0.626946  1.084674  0.851653 -1.087033
2013-01-01 -0.584097 -0.672626  0.871800  0.009349
2013-01-02 -0.528538 -0.214885  0.191734 -0.486818
2013-01-09 -0.418993 -0.943578 -0.583818  1.286449
2013-01-05 -0.127941 -1.037672 -0.466913  0.859080
2013-01-07  0.587661  1.696389  1.367631  1.039936
2013-01-10  1.887318 -0.984025 -1.201518 -1.223087
>>> df[0:3]
                   A         B         C         D
2013-01-01 -0.584097 -0.672626  0.871800  0.009349
2013-01-02 -0.528538 -0.214885  0.191734 -0.486818
2013-01-03 -0.709967 -0.074022 -0.684967 -0.938910
>>> df.loc[dates[0]]
A   -0.584097
B   -0.672626
C    0.871800
D    0.009349
Name: 2013-01-01 00:00:00, dtype: float64
>>> 
