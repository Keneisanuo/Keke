Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas
>>> import pandas as pd
>>> url="http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

>>> df=pd.read_csv(url)
>>> df
     3    ?  alfa-romero     gas    std   two  convertible  rwd  front  88.60  \
0    3    ?  alfa-romero     gas    std   two  convertible  rwd  front   88.6   
1    1    ?  alfa-romero     gas    std   two    hatchback  rwd  front   94.5   
2    2  164         audi     gas    std  four        sedan  fwd  front   99.8   
3    2  164         audi     gas    std  four        sedan  4wd  front   99.4   
4    2    ?         audi     gas    std   two        sedan  fwd  front   99.8   
5    1  158         audi     gas    std  four        sedan  fwd  front  105.8   
6    1    ?         audi     gas    std  four        wagon  fwd  front  105.8   
7    1  158         audi     gas  turbo  four        sedan  fwd  front  105.8   
8    0    ?         audi     gas  turbo   two    hatchback  4wd  front   99.5   
9    2  192          bmw     gas    std   two        sedan  rwd  front  101.2   
10   0  192          bmw     gas    std  four        sedan  rwd  front  101.2   
11   0  188          bmw     gas    std   two        sedan  rwd  front  101.2   
12   0  188          bmw     gas    std  four        sedan  rwd  front  101.2   
13   1    ?          bmw     gas    std  four        sedan  rwd  front  103.5   
14   0    ?          bmw     gas    std  four        sedan  rwd  front  103.5   
15   0    ?          bmw     gas    std   two        sedan  rwd  front  103.5   
16   0    ?          bmw     gas    std  four        sedan  rwd  front  110.0   
17   2  121    chevrolet     gas    std   two    hatchback  fwd  front   88.4   
18   1   98    chevrolet     gas    std   two    hatchback  fwd  front   94.5   
19   0   81    chevrolet     gas    std  four        sedan  fwd  front   94.5   
20   1  118        dodge     gas    std   two    hatchback  fwd  front   93.7   
21   1  118        dodge     gas    std   two    hatchback  fwd  front   93.7   
22   1  118        dodge     gas  turbo   two    hatchback  fwd  front   93.7   
23   1  148        dodge     gas    std  four    hatchback  fwd  front   93.7   
24   1  148        dodge     gas    std  four        sedan  fwd  front   93.7   
25   1  148        dodge     gas    std  four        sedan  fwd  front   93.7   
26   1  148        dodge     gas  turbo     ?        sedan  fwd  front   93.7   
27  -1  110        dodge     gas    std  four        wagon  fwd  front  103.3   
28   3  145        dodge     gas  turbo   two    hatchback  fwd  front   95.9   
29   2  137        honda     gas    std   two    hatchback  fwd  front   86.6   
..  ..  ...          ...     ...    ...   ...          ...  ...    ...    ...   
174 -1   65       toyota     gas    std  four    hatchback  fwd  front  102.4   
175 -1   65       toyota     gas    std  four        sedan  fwd  front  102.4   
176 -1   65       toyota     gas    std  four    hatchback  fwd  front  102.4   
177  3  197       toyota     gas    std   two    hatchback  rwd  front  102.9   
178  3  197       toyota     gas    std   two    hatchback  rwd  front  102.9   
179 -1   90       toyota     gas    std  four        sedan  rwd  front  104.5   
180 -1    ?       toyota     gas    std  four        wagon  rwd  front  104.5   
181  2  122   volkswagen  diesel    std   two        sedan  fwd  front   97.3   
182  2  122   volkswagen     gas    std   two        sedan  fwd  front   97.3   
183  2   94   volkswagen  diesel    std  four        sedan  fwd  front   97.3   
184  2   94   volkswagen     gas    std  four        sedan  fwd  front   97.3   
185  2   94   volkswagen     gas    std  four        sedan  fwd  front   97.3   
186  2   94   volkswagen  diesel  turbo  four        sedan  fwd  front   97.3   
187  2   94   volkswagen     gas    std  four        sedan  fwd  front   97.3   
188  3    ?   volkswagen     gas    std   two  convertible  fwd  front   94.5   
189  3  256   volkswagen     gas    std   two    hatchback  fwd  front   94.5   
190  0    ?   volkswagen     gas    std  four        sedan  fwd  front  100.4   
191  0    ?   volkswagen  diesel  turbo  four        sedan  fwd  front  100.4   
192  0    ?   volkswagen     gas    std  four        wagon  fwd  front  100.4   
193 -2  103        volvo     gas    std  four        sedan  rwd  front  104.3   
194 -1   74        volvo     gas    std  four        wagon  rwd  front  104.3   
195 -2  103        volvo     gas    std  four        sedan  rwd  front  104.3   
196 -1   74        volvo     gas    std  four        wagon  rwd  front  104.3   
197 -2  103        volvo     gas  turbo  four        sedan  rwd  front  104.3   
198 -1   74        volvo     gas  turbo  four        wagon  rwd  front  104.3   
199 -1   95        volvo     gas    std  four        sedan  rwd  front  109.1   
200 -1   95        volvo     gas  turbo  four        sedan  rwd  front  109.1   
201 -1   95        volvo     gas    std  four        sedan  rwd  front  109.1   
202 -1   95        volvo  diesel  turbo  four        sedan  rwd  front  109.1   
203 -1   95        volvo     gas  turbo  four        sedan  rwd  front  109.1   

     ...    130  mpfi  3.47  2.68   9.00  111  5000  21  27  13495  
0    ...    130  mpfi  3.47  2.68   9.00  111  5000  21  27  16500  
1    ...    152  mpfi  2.68  3.47   9.00  154  5000  19  26  16500  
2    ...    109  mpfi  3.19  3.40  10.00  102  5500  24  30  13950  
3    ...    136  mpfi  3.19  3.40   8.00  115  5500  18  22  17450  
4    ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  15250  
5    ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  17710  
6    ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  18920  
7    ...    131  mpfi  3.13  3.40   8.30  140  5500  17  20  23875  
8    ...    131  mpfi  3.13  3.40   7.00  160  5500  16  22      ?  
9    ...    108  mpfi  3.50  2.80   8.80  101  5800  23  29  16430  
10   ...    108  mpfi  3.50  2.80   8.80  101  5800  23  29  16925  
11   ...    164  mpfi  3.31  3.19   9.00  121  4250  21  28  20970  
12   ...    164  mpfi  3.31  3.19   9.00  121  4250  21  28  21105  
13   ...    164  mpfi  3.31  3.19   9.00  121  4250  20  25  24565  
14   ...    209  mpfi  3.62  3.39   8.00  182  5400  16  22  30760  
15   ...    209  mpfi  3.62  3.39   8.00  182  5400  16  22  41315  
16   ...    209  mpfi  3.62  3.39   8.00  182  5400  15  20  36880  
17   ...     61  2bbl  2.91  3.03   9.50   48  5100  47  53   5151  
18   ...     90  2bbl  3.03  3.11   9.60   70  5400  38  43   6295  
19   ...     90  2bbl  3.03  3.11   9.60   70  5400  38  43   6575  
20   ...     90  2bbl  2.97  3.23   9.41   68  5500  37  41   5572  
21   ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6377  
22   ...     98  mpfi  3.03  3.39   7.60  102  5500  24  30   7957  
23   ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6229  
24   ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6692  
25   ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   7609  
26   ...     98  mpfi  3.03  3.39   7.60  102  5500  24  30   8558  
27   ...    122  2bbl  3.34  3.46   8.50   88  5000  24  30   8921  
28   ...    156   mfi  3.60  3.90   7.00  145  5000  19  24  12964  
29   ...     92  1bbl  2.91  3.41   9.60   58  4800  49  54   6479  
..   ...    ...   ...   ...   ...    ...  ...   ...  ..  ..    ...  
174  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32   9988  
175  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32  10898  
176  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32  11248  
177  ...    171  mpfi  3.27  3.35   9.30  161  5200  20  24  16558  
178  ...    171  mpfi  3.27  3.35   9.30  161  5200  19  24  15998  
179  ...    171  mpfi  3.27  3.35   9.20  156  5200  20  24  15690  
180  ...    161  mpfi  3.27  3.35   9.20  156  5200  19  24  15750  
181  ...     97   idi  3.01  3.40  23.00   52  4800  37  46   7775  
182  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   7975  
183  ...     97   idi  3.01  3.40  23.00   52  4800  37  46   7995  
184  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   8195  
185  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   8495  
186  ...     97   idi  3.01  3.40  23.00   68  4500  37  42   9495  
187  ...    109  mpfi  3.19  3.40  10.00  100  5500  26  32   9995  
188  ...    109  mpfi  3.19  3.40   8.50   90  5500  24  29  11595  
189  ...    109  mpfi  3.19  3.40   8.50   90  5500  24  29   9980  
190  ...    136  mpfi  3.19  3.40   8.50  110  5500  19  24  13295  
191  ...     97   idi  3.01  3.40  23.00   68  4500  33  38  13845  
192  ...    109  mpfi  3.19  3.40   9.00   88  5500  25  31  12290  
193  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  12940  
194  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  13415  
195  ...    141  mpfi  3.78  3.15   9.50  114  5400  24  28  15985  
196  ...    141  mpfi  3.78  3.15   9.50  114  5400  24  28  16515  
197  ...    130  mpfi  3.62  3.15   7.50  162  5100  17  22  18420  
198  ...    130  mpfi  3.62  3.15   7.50  162  5100  17  22  18950  
199  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  16845  
200  ...    141  mpfi  3.78  3.15   8.70  160  5300  19  25  19045  
201  ...    173  mpfi  3.58  2.87   8.80  134  5500  18  23  21485  
202  ...    145   idi  3.01  3.40  23.00  106  4800  26  27  22470  
203  ...    141  mpfi  3.78  3.15   9.50  114  5400  19  25  22625  

[204 rows x 26 columns]
>>> df=pd.read_csv(url,header=None)
>>> df
     0    1            2       3      4     5            6    7      8   \
0     3    ?  alfa-romero     gas    std   two  convertible  rwd  front   
1     3    ?  alfa-romero     gas    std   two  convertible  rwd  front   
2     1    ?  alfa-romero     gas    std   two    hatchback  rwd  front   
3     2  164         audi     gas    std  four        sedan  fwd  front   
4     2  164         audi     gas    std  four        sedan  4wd  front   
5     2    ?         audi     gas    std   two        sedan  fwd  front   
6     1  158         audi     gas    std  four        sedan  fwd  front   
7     1    ?         audi     gas    std  four        wagon  fwd  front   
8     1  158         audi     gas  turbo  four        sedan  fwd  front   
9     0    ?         audi     gas  turbo   two    hatchback  4wd  front   
10    2  192          bmw     gas    std   two        sedan  rwd  front   
11    0  192          bmw     gas    std  four        sedan  rwd  front   
12    0  188          bmw     gas    std   two        sedan  rwd  front   
13    0  188          bmw     gas    std  four        sedan  rwd  front   
14    1    ?          bmw     gas    std  four        sedan  rwd  front   
15    0    ?          bmw     gas    std  four        sedan  rwd  front   
16    0    ?          bmw     gas    std   two        sedan  rwd  front   
17    0    ?          bmw     gas    std  four        sedan  rwd  front   
18    2  121    chevrolet     gas    std   two    hatchback  fwd  front   
19    1   98    chevrolet     gas    std   two    hatchback  fwd  front   
20    0   81    chevrolet     gas    std  four        sedan  fwd  front   
21    1  118        dodge     gas    std   two    hatchback  fwd  front   
22    1  118        dodge     gas    std   two    hatchback  fwd  front   
23    1  118        dodge     gas  turbo   two    hatchback  fwd  front   
24    1  148        dodge     gas    std  four    hatchback  fwd  front   
25    1  148        dodge     gas    std  four        sedan  fwd  front   
26    1  148        dodge     gas    std  four        sedan  fwd  front   
27    1  148        dodge     gas  turbo     ?        sedan  fwd  front   
28   -1  110        dodge     gas    std  four        wagon  fwd  front   
29    3  145        dodge     gas  turbo   two    hatchback  fwd  front   
..   ..  ...          ...     ...    ...   ...          ...  ...    ...   
175  -1   65       toyota     gas    std  four    hatchback  fwd  front   
176  -1   65       toyota     gas    std  four        sedan  fwd  front   
177  -1   65       toyota     gas    std  four    hatchback  fwd  front   
178   3  197       toyota     gas    std   two    hatchback  rwd  front   
179   3  197       toyota     gas    std   two    hatchback  rwd  front   
180  -1   90       toyota     gas    std  four        sedan  rwd  front   
181  -1    ?       toyota     gas    std  four        wagon  rwd  front   
182   2  122   volkswagen  diesel    std   two        sedan  fwd  front   
183   2  122   volkswagen     gas    std   two        sedan  fwd  front   
184   2   94   volkswagen  diesel    std  four        sedan  fwd  front   
185   2   94   volkswagen     gas    std  four        sedan  fwd  front   
186   2   94   volkswagen     gas    std  four        sedan  fwd  front   
187   2   94   volkswagen  diesel  turbo  four        sedan  fwd  front   
188   2   94   volkswagen     gas    std  four        sedan  fwd  front   
189   3    ?   volkswagen     gas    std   two  convertible  fwd  front   
190   3  256   volkswagen     gas    std   two    hatchback  fwd  front   
191   0    ?   volkswagen     gas    std  four        sedan  fwd  front   
192   0    ?   volkswagen  diesel  turbo  four        sedan  fwd  front   
193   0    ?   volkswagen     gas    std  four        wagon  fwd  front   
194  -2  103        volvo     gas    std  four        sedan  rwd  front   
195  -1   74        volvo     gas    std  four        wagon  rwd  front   
196  -2  103        volvo     gas    std  four        sedan  rwd  front   
197  -1   74        volvo     gas    std  four        wagon  rwd  front   
198  -2  103        volvo     gas  turbo  four        sedan  rwd  front   
199  -1   74        volvo     gas  turbo  four        wagon  rwd  front   
200  -1   95        volvo     gas    std  four        sedan  rwd  front   
201  -1   95        volvo     gas  turbo  four        sedan  rwd  front   
202  -1   95        volvo     gas    std  four        sedan  rwd  front   
203  -1   95        volvo  diesel  turbo  four        sedan  rwd  front   
204  -1   95        volvo     gas  turbo  four        sedan  rwd  front   

        9   ...     16    17    18    19     20   21    22  23  24     25  
0     88.6  ...    130  mpfi  3.47  2.68   9.00  111  5000  21  27  13495  
1     88.6  ...    130  mpfi  3.47  2.68   9.00  111  5000  21  27  16500  
2     94.5  ...    152  mpfi  2.68  3.47   9.00  154  5000  19  26  16500  
3     99.8  ...    109  mpfi  3.19  3.40  10.00  102  5500  24  30  13950  
4     99.4  ...    136  mpfi  3.19  3.40   8.00  115  5500  18  22  17450  
5     99.8  ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  15250  
6    105.8  ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  17710  
7    105.8  ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  18920  
8    105.8  ...    131  mpfi  3.13  3.40   8.30  140  5500  17  20  23875  
9     99.5  ...    131  mpfi  3.13  3.40   7.00  160  5500  16  22      ?  
10   101.2  ...    108  mpfi  3.50  2.80   8.80  101  5800  23  29  16430  
11   101.2  ...    108  mpfi  3.50  2.80   8.80  101  5800  23  29  16925  
12   101.2  ...    164  mpfi  3.31  3.19   9.00  121  4250  21  28  20970  
13   101.2  ...    164  mpfi  3.31  3.19   9.00  121  4250  21  28  21105  
14   103.5  ...    164  mpfi  3.31  3.19   9.00  121  4250  20  25  24565  
15   103.5  ...    209  mpfi  3.62  3.39   8.00  182  5400  16  22  30760  
16   103.5  ...    209  mpfi  3.62  3.39   8.00  182  5400  16  22  41315  
17   110.0  ...    209  mpfi  3.62  3.39   8.00  182  5400  15  20  36880  
18    88.4  ...     61  2bbl  2.91  3.03   9.50   48  5100  47  53   5151  
19    94.5  ...     90  2bbl  3.03  3.11   9.60   70  5400  38  43   6295  
20    94.5  ...     90  2bbl  3.03  3.11   9.60   70  5400  38  43   6575  
21    93.7  ...     90  2bbl  2.97  3.23   9.41   68  5500  37  41   5572  
22    93.7  ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6377  
23    93.7  ...     98  mpfi  3.03  3.39   7.60  102  5500  24  30   7957  
24    93.7  ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6229  
25    93.7  ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6692  
26    93.7  ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   7609  
27    93.7  ...     98  mpfi  3.03  3.39   7.60  102  5500  24  30   8558  
28   103.3  ...    122  2bbl  3.34  3.46   8.50   88  5000  24  30   8921  
29    95.9  ...    156   mfi  3.60  3.90   7.00  145  5000  19  24  12964  
..     ...  ...    ...   ...   ...   ...    ...  ...   ...  ..  ..    ...  
175  102.4  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32   9988  
176  102.4  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32  10898  
177  102.4  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32  11248  
178  102.9  ...    171  mpfi  3.27  3.35   9.30  161  5200  20  24  16558  
179  102.9  ...    171  mpfi  3.27  3.35   9.30  161  5200  19  24  15998  
180  104.5  ...    171  mpfi  3.27  3.35   9.20  156  5200  20  24  15690  
181  104.5  ...    161  mpfi  3.27  3.35   9.20  156  5200  19  24  15750  
182   97.3  ...     97   idi  3.01  3.40  23.00   52  4800  37  46   7775  
183   97.3  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   7975  
184   97.3  ...     97   idi  3.01  3.40  23.00   52  4800  37  46   7995  
185   97.3  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   8195  
186   97.3  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   8495  
187   97.3  ...     97   idi  3.01  3.40  23.00   68  4500  37  42   9495  
188   97.3  ...    109  mpfi  3.19  3.40  10.00  100  5500  26  32   9995  
189   94.5  ...    109  mpfi  3.19  3.40   8.50   90  5500  24  29  11595  
190   94.5  ...    109  mpfi  3.19  3.40   8.50   90  5500  24  29   9980  
191  100.4  ...    136  mpfi  3.19  3.40   8.50  110  5500  19  24  13295  
192  100.4  ...     97   idi  3.01  3.40  23.00   68  4500  33  38  13845  
193  100.4  ...    109  mpfi  3.19  3.40   9.00   88  5500  25  31  12290  
194  104.3  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  12940  
195  104.3  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  13415  
196  104.3  ...    141  mpfi  3.78  3.15   9.50  114  5400  24  28  15985  
197  104.3  ...    141  mpfi  3.78  3.15   9.50  114  5400  24  28  16515  
198  104.3  ...    130  mpfi  3.62  3.15   7.50  162  5100  17  22  18420  
199  104.3  ...    130  mpfi  3.62  3.15   7.50  162  5100  17  22  18950  
200  109.1  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  16845  
201  109.1  ...    141  mpfi  3.78  3.15   8.70  160  5300  19  25  19045  
202  109.1  ...    173  mpfi  3.58  2.87   8.80  134  5500  18  23  21485  
203  109.1  ...    145   idi  3.01  3.40  23.00  106  4800  26  27  22470  
204  109.1  ...    141  mpfi  3.78  3.15   9.50  114  5400  19  25  22625  

[205 rows x 26 columns]
>>> df.columns=headers
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    df.columns=headers
NameError: name 'headers' is not defined
>>>  headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rmp","city-mpg","highway-mpg","price"]
SyntaxError: unexpected indent
>>> headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rmp","city-mpg","highway-mpg","price"]
>>> df.columns=headers
>>> df.head(10)
   symboling normalized-losses         make fuel-type aspiration num-of-doors  \
0          3                 ?  alfa-romero       gas        std          two   
1          3                 ?  alfa-romero       gas        std          two   
2          1                 ?  alfa-romero       gas        std          two   
3          2               164         audi       gas        std         four   
4          2               164         audi       gas        std         four   
5          2                 ?         audi       gas        std          two   
6          1               158         audi       gas        std         four   
7          1                 ?         audi       gas        std         four   
8          1               158         audi       gas      turbo         four   
9          0                 ?         audi       gas      turbo          two   

    body-style drive-wheels engine-location  wheel-base  ...    engine-size  \
0  convertible          rwd           front        88.6  ...            130   
1  convertible          rwd           front        88.6  ...            130   
2    hatchback          rwd           front        94.5  ...            152   
3        sedan          fwd           front        99.8  ...            109   
4        sedan          4wd           front        99.4  ...            136   
5        sedan          fwd           front        99.8  ...            136   
6        sedan          fwd           front       105.8  ...            136   
7        wagon          fwd           front       105.8  ...            136   
8        sedan          fwd           front       105.8  ...            131   
9    hatchback          4wd           front        99.5  ...            131   

   fuel-system  bore  stroke compression-ratio horsepower  peak-rmp city-mpg  \
0         mpfi  3.47    2.68               9.0        111      5000       21   
1         mpfi  3.47    2.68               9.0        111      5000       21   
2         mpfi  2.68    3.47               9.0        154      5000       19   
3         mpfi  3.19    3.40              10.0        102      5500       24   
4         mpfi  3.19    3.40               8.0        115      5500       18   
5         mpfi  3.19    3.40               8.5        110      5500       19   
6         mpfi  3.19    3.40               8.5        110      5500       19   
7         mpfi  3.19    3.40               8.5        110      5500       19   
8         mpfi  3.13    3.40               8.3        140      5500       17   
9         mpfi  3.13    3.40               7.0        160      5500       16   

  highway-mpg  price  
0          27  13495  
1          27  16500  
2          26  16500  
3          30  13950  
4          22  17450  
5          25  15250  
6          25  17710  
7          25  18920  
8          20  23875  
9          22      ?  

[10 rows x 26 columns]
>>> df.head(5)
   symboling normalized-losses         make fuel-type aspiration num-of-doors  \
0          3                 ?  alfa-romero       gas        std          two   
1          3                 ?  alfa-romero       gas        std          two   
2          1                 ?  alfa-romero       gas        std          two   
3          2               164         audi       gas        std         four   
4          2               164         audi       gas        std         four   

    body-style drive-wheels engine-location  wheel-base  ...    engine-size  \
0  convertible          rwd           front        88.6  ...            130   
1  convertible          rwd           front        88.6  ...            130   
2    hatchback          rwd           front        94.5  ...            152   
3        sedan          fwd           front        99.8  ...            109   
4        sedan          4wd           front        99.4  ...            136   

   fuel-system  bore  stroke compression-ratio horsepower  peak-rmp city-mpg  \
0         mpfi  3.47    2.68               9.0        111      5000       21   
1         mpfi  3.47    2.68               9.0        111      5000       21   
2         mpfi  2.68    3.47               9.0        154      5000       19   
3         mpfi  3.19    3.40              10.0        102      5500       24   
4         mpfi  3.19    3.40               8.0        115      5500       18   

  highway-mpg  price  
0          27  13495  
1          27  16500  
2          26  16500  
3          30  13950  
4          22  17450  

[5 rows x 26 columns]
>>> df.describe()
        symboling  wheel-base      length       width      height  \
count  205.000000  205.000000  205.000000  205.000000  205.000000   
mean     0.834146   98.756585  174.049268   65.907805   53.724878   
std      1.245307    6.021776   12.337289    2.145204    2.443522   
min     -2.000000   86.600000  141.100000   60.300000   47.800000   
25%      0.000000   94.500000  166.300000   64.100000   52.000000   
50%      1.000000   97.000000  173.200000   65.500000   54.100000   
75%      2.000000  102.400000  183.100000   66.900000   55.500000   
max      3.000000  120.900000  208.100000   72.300000   59.800000   

       curb-weight  engine-size  compression-ratio    city-mpg  highway-mpg  
count   205.000000   205.000000         205.000000  205.000000   205.000000  
mean   2555.565854   126.907317          10.142537   25.219512    30.751220  
std     520.680204    41.642693           3.972040    6.542142     6.886443  
min    1488.000000    61.000000           7.000000   13.000000    16.000000  
25%    2145.000000    97.000000           8.600000   19.000000    25.000000  
50%    2414.000000   120.000000           9.000000   24.000000    30.000000  
75%    2935.000000   141.000000           9.400000   30.000000    34.000000  
max    4066.000000   326.000000          23.000000   49.000000    54.000000  
>>> df.dtypes()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    df.dtypes()
TypeError: 'Series' object is not callable
>>> df["symboling"]
0      3
1      3
2      1
3      2
4      2
5      2
6      1
7      1
8      1
9      0
10     2
11     0
12     0
13     0
14     1
15     0
16     0
17     0
18     2
19     1
20     0
21     1
22     1
23     1
24     1
25     1
26     1
27     1
28    -1
29     3
      ..
175   -1
176   -1
177   -1
178    3
179    3
180   -1
181   -1
182    2
183    2
184    2
185    2
186    2
187    2
188    2
189    3
190    3
191    0
192    0
193    0
194   -2
195   -1
196   -2
197   -1
198   -2
199   -1
200   -1
201   -1
202   -1
203   -1
204   -1
Name: symboling, Length: 205, dtype: int64
>>> df["symboling"=df["symboling"]+1
       
SyntaxError: invalid syntax
>>> df["symboling"]=df["symboling"]+1
       
>>> df
       
     symboling normalized-losses         make fuel-type aspiration  \
0            4                 ?  alfa-romero       gas        std   
1            4                 ?  alfa-romero       gas        std   
2            2                 ?  alfa-romero       gas        std   
3            3               164         audi       gas        std   
4            3               164         audi       gas        std   
5            3                 ?         audi       gas        std   
6            2               158         audi       gas        std   
7            2                 ?         audi       gas        std   
8            2               158         audi       gas      turbo   
9            1                 ?         audi       gas      turbo   
10           3               192          bmw       gas        std   
11           1               192          bmw       gas        std   
12           1               188          bmw       gas        std   
13           1               188          bmw       gas        std   
14           2                 ?          bmw       gas        std   
15           1                 ?          bmw       gas        std   
16           1                 ?          bmw       gas        std   
17           1                 ?          bmw       gas        std   
18           3               121    chevrolet       gas        std   
19           2                98    chevrolet       gas        std   
20           1                81    chevrolet       gas        std   
21           2               118        dodge       gas        std   
22           2               118        dodge       gas        std   
23           2               118        dodge       gas      turbo   
24           2               148        dodge       gas        std   
25           2               148        dodge       gas        std   
26           2               148        dodge       gas        std   
27           2               148        dodge       gas      turbo   
28           0               110        dodge       gas        std   
29           4               145        dodge       gas      turbo   
..         ...               ...          ...       ...        ...   
175          0                65       toyota       gas        std   
176          0                65       toyota       gas        std   
177          0                65       toyota       gas        std   
178          4               197       toyota       gas        std   
179          4               197       toyota       gas        std   
180          0                90       toyota       gas        std   
181          0                 ?       toyota       gas        std   
182          3               122   volkswagen    diesel        std   
183          3               122   volkswagen       gas        std   
184          3                94   volkswagen    diesel        std   
185          3                94   volkswagen       gas        std   
186          3                94   volkswagen       gas        std   
187          3                94   volkswagen    diesel      turbo   
188          3                94   volkswagen       gas        std   
189          4                 ?   volkswagen       gas        std   
190          4               256   volkswagen       gas        std   
191          1                 ?   volkswagen       gas        std   
192          1                 ?   volkswagen    diesel      turbo   
193          1                 ?   volkswagen       gas        std   
194         -1               103        volvo       gas        std   
195          0                74        volvo       gas        std   
196         -1               103        volvo       gas        std   
197          0                74        volvo       gas        std   
198         -1               103        volvo       gas      turbo   
199          0                74        volvo       gas      turbo   
200          0                95        volvo       gas        std   
201          0                95        volvo       gas      turbo   
202          0                95        volvo       gas        std   
203          0                95        volvo    diesel      turbo   
204          0                95        volvo       gas      turbo   

    num-of-doors   body-style drive-wheels engine-location  wheel-base  ...    \
0            two  convertible          rwd           front        88.6  ...     
1            two  convertible          rwd           front        88.6  ...     
2            two    hatchback          rwd           front        94.5  ...     
3           four        sedan          fwd           front        99.8  ...     
4           four        sedan          4wd           front        99.4  ...     
5            two        sedan          fwd           front        99.8  ...     
6           four        sedan          fwd           front       105.8  ...     
7           four        wagon          fwd           front       105.8  ...     
8           four        sedan          fwd           front       105.8  ...     
9            two    hatchback          4wd           front        99.5  ...     
10           two        sedan          rwd           front       101.2  ...     
11          four        sedan          rwd           front       101.2  ...     
12           two        sedan          rwd           front       101.2  ...     
13          four        sedan          rwd           front       101.2  ...     
14          four        sedan          rwd           front       103.5  ...     
15          four        sedan          rwd           front       103.5  ...     
16           two        sedan          rwd           front       103.5  ...     
17          four        sedan          rwd           front       110.0  ...     
18           two    hatchback          fwd           front        88.4  ...     
19           two    hatchback          fwd           front        94.5  ...     
20          four        sedan          fwd           front        94.5  ...     
21           two    hatchback          fwd           front        93.7  ...     
22           two    hatchback          fwd           front        93.7  ...     
23           two    hatchback          fwd           front        93.7  ...     
24          four    hatchback          fwd           front        93.7  ...     
25          four        sedan          fwd           front        93.7  ...     
26          four        sedan          fwd           front        93.7  ...     
27             ?        sedan          fwd           front        93.7  ...     
28          four        wagon          fwd           front       103.3  ...     
29           two    hatchback          fwd           front        95.9  ...     
..           ...          ...          ...             ...         ...  ...     
175         four    hatchback          fwd           front       102.4  ...     
176         four        sedan          fwd           front       102.4  ...     
177         four    hatchback          fwd           front       102.4  ...     
178          two    hatchback          rwd           front       102.9  ...     
179          two    hatchback          rwd           front       102.9  ...     
180         four        sedan          rwd           front       104.5  ...     
181         four        wagon          rwd           front       104.5  ...     
182          two        sedan          fwd           front        97.3  ...     
183          two        sedan          fwd           front        97.3  ...     
184         four        sedan          fwd           front        97.3  ...     
185         four        sedan          fwd           front        97.3  ...     
186         four        sedan          fwd           front        97.3  ...     
187         four        sedan          fwd           front        97.3  ...     
188         four        sedan          fwd           front        97.3  ...     
189          two  convertible          fwd           front        94.5  ...     
190          two    hatchback          fwd           front        94.5  ...     
191         four        sedan          fwd           front       100.4  ...     
192         four        sedan          fwd           front       100.4  ...     
193         four        wagon          fwd           front       100.4  ...     
194         four        sedan          rwd           front       104.3  ...     
195         four        wagon          rwd           front       104.3  ...     
196         four        sedan          rwd           front       104.3  ...     
197         four        wagon          rwd           front       104.3  ...     
198         four        sedan          rwd           front       104.3  ...     
199         four        wagon          rwd           front       104.3  ...     
200         four        sedan          rwd           front       109.1  ...     
201         four        sedan          rwd           front       109.1  ...     
202         four        sedan          rwd           front       109.1  ...     
203         four        sedan          rwd           front       109.1  ...     
204         four        sedan          rwd           front       109.1  ...     

     engine-size  fuel-system  bore  stroke compression-ratio horsepower  \
0            130         mpfi  3.47    2.68              9.00        111   
1            130         mpfi  3.47    2.68              9.00        111   
2            152         mpfi  2.68    3.47              9.00        154   
3            109         mpfi  3.19    3.40             10.00        102   
4            136         mpfi  3.19    3.40              8.00        115   
5            136         mpfi  3.19    3.40              8.50        110   
6            136         mpfi  3.19    3.40              8.50        110   
7            136         mpfi  3.19    3.40              8.50        110   
8            131         mpfi  3.13    3.40              8.30        140   
9            131         mpfi  3.13    3.40              7.00        160   
10           108         mpfi  3.50    2.80              8.80        101   
11           108         mpfi  3.50    2.80              8.80        101   
12           164         mpfi  3.31    3.19              9.00        121   
13           164         mpfi  3.31    3.19              9.00        121   
14           164         mpfi  3.31    3.19              9.00        121   
15           209         mpfi  3.62    3.39              8.00        182   
16           209         mpfi  3.62    3.39              8.00        182   
17           209         mpfi  3.62    3.39              8.00        182   
18            61         2bbl  2.91    3.03              9.50         48   
19            90         2bbl  3.03    3.11              9.60         70   
20            90         2bbl  3.03    3.11              9.60         70   
21            90         2bbl  2.97    3.23              9.41         68   
22            90         2bbl  2.97    3.23              9.40         68   
23            98         mpfi  3.03    3.39              7.60        102   
24            90         2bbl  2.97    3.23              9.40         68   
25            90         2bbl  2.97    3.23              9.40         68   
26            90         2bbl  2.97    3.23              9.40         68   
27            98         mpfi  3.03    3.39              7.60        102   
28           122         2bbl  3.34    3.46              8.50         88   
29           156          mfi  3.60    3.90              7.00        145   
..           ...          ...   ...     ...               ...        ...   
175          122         mpfi  3.31    3.54              8.70         92   
176          122         mpfi  3.31    3.54              8.70         92   
177          122         mpfi  3.31    3.54              8.70         92   
178          171         mpfi  3.27    3.35              9.30        161   
179          171         mpfi  3.27    3.35              9.30        161   
180          171         mpfi  3.27    3.35              9.20        156   
181          161         mpfi  3.27    3.35              9.20        156   
182           97          idi  3.01    3.40             23.00         52   
183          109         mpfi  3.19    3.40              9.00         85   
184           97          idi  3.01    3.40             23.00         52   
185          109         mpfi  3.19    3.40              9.00         85   
186          109         mpfi  3.19    3.40              9.00         85   
187           97          idi  3.01    3.40             23.00         68   
188          109         mpfi  3.19    3.40             10.00        100   
189          109         mpfi  3.19    3.40              8.50         90   
190          109         mpfi  3.19    3.40              8.50         90   
191          136         mpfi  3.19    3.40              8.50        110   
192           97          idi  3.01    3.40             23.00         68   
193          109         mpfi  3.19    3.40              9.00         88   
194          141         mpfi  3.78    3.15              9.50        114   
195          141         mpfi  3.78    3.15              9.50        114   
196          141         mpfi  3.78    3.15              9.50        114   
197          141         mpfi  3.78    3.15              9.50        114   
198          130         mpfi  3.62    3.15              7.50        162   
199          130         mpfi  3.62    3.15              7.50        162   
200          141         mpfi  3.78    3.15              9.50        114   
201          141         mpfi  3.78    3.15              8.70        160   
202          173         mpfi  3.58    2.87              8.80        134   
203          145          idi  3.01    3.40             23.00        106   
204          141         mpfi  3.78    3.15              9.50        114   

     peak-rmp city-mpg highway-mpg  price  
0        5000       21          27  13495  
1        5000       21          27  16500  
2        5000       19          26  16500  
3        5500       24          30  13950  
4        5500       18          22  17450  
5        5500       19          25  15250  
6        5500       19          25  17710  
7        5500       19          25  18920  
8        5500       17          20  23875  
9        5500       16          22      ?  
10       5800       23          29  16430  
11       5800       23          29  16925  
12       4250       21          28  20970  
13       4250       21          28  21105  
14       4250       20          25  24565  
15       5400       16          22  30760  
16       5400       16          22  41315  
17       5400       15          20  36880  
18       5100       47          53   5151  
19       5400       38          43   6295  
20       5400       38          43   6575  
21       5500       37          41   5572  
22       5500       31          38   6377  
23       5500       24          30   7957  
24       5500       31          38   6229  
25       5500       31          38   6692  
26       5500       31          38   7609  
27       5500       24          30   8558  
28       5000       24          30   8921  
29       5000       19          24  12964  
..        ...      ...         ...    ...  
175      4200       27          32   9988  
176      4200       27          32  10898  
177      4200       27          32  11248  
178      5200       20          24  16558  
179      5200       19          24  15998  
180      5200       20          24  15690  
181      5200       19          24  15750  
182      4800       37          46   7775  
183      5250       27          34   7975  
184      4800       37          46   7995  
185      5250       27          34   8195  
186      5250       27          34   8495  
187      4500       37          42   9495  
188      5500       26          32   9995  
189      5500       24          29  11595  
190      5500       24          29   9980  
191      5500       19          24  13295  
192      4500       33          38  13845  
193      5500       25          31  12290  
194      5400       23          28  12940  
195      5400       23          28  13415  
196      5400       24          28  15985  
197      5400       24          28  16515  
198      5100       17          22  18420  
199      5100       17          22  18950  
200      5400       23          28  16845  
201      5300       19          25  19045  
202      5500       18          23  21485  
203      4800       26          27  22470  
204      5400       19          25  22625  

[205 rows x 26 columns]
>>> df["symboling"]=df["symboling"]-1
       
>>> df
       
     symboling normalized-losses         make fuel-type aspiration  \
0            3                 ?  alfa-romero       gas        std   
1            3                 ?  alfa-romero       gas        std   
2            1                 ?  alfa-romero       gas        std   
3            2               164         audi       gas        std   
4            2               164         audi       gas        std   
5            2                 ?         audi       gas        std   
6            1               158         audi       gas        std   
7            1                 ?         audi       gas        std   
8            1               158         audi       gas      turbo   
9            0                 ?         audi       gas      turbo   
10           2               192          bmw       gas        std   
11           0               192          bmw       gas        std   
12           0               188          bmw       gas        std   
13           0               188          bmw       gas        std   
14           1                 ?          bmw       gas        std   
15           0                 ?          bmw       gas        std   
16           0                 ?          bmw       gas        std   
17           0                 ?          bmw       gas        std   
18           2               121    chevrolet       gas        std   
19           1                98    chevrolet       gas        std   
20           0                81    chevrolet       gas        std   
21           1               118        dodge       gas        std   
22           1               118        dodge       gas        std   
23           1               118        dodge       gas      turbo   
24           1               148        dodge       gas        std   
25           1               148        dodge       gas        std   
26           1               148        dodge       gas        std   
27           1               148        dodge       gas      turbo   
28          -1               110        dodge       gas        std   
29           3               145        dodge       gas      turbo   
..         ...               ...          ...       ...        ...   
175         -1                65       toyota       gas        std   
176         -1                65       toyota       gas        std   
177         -1                65       toyota       gas        std   
178          3               197       toyota       gas        std   
179          3               197       toyota       gas        std   
180         -1                90       toyota       gas        std   
181         -1                 ?       toyota       gas        std   
182          2               122   volkswagen    diesel        std   
183          2               122   volkswagen       gas        std   
184          2                94   volkswagen    diesel        std   
185          2                94   volkswagen       gas        std   
186          2                94   volkswagen       gas        std   
187          2                94   volkswagen    diesel      turbo   
188          2                94   volkswagen       gas        std   
189          3                 ?   volkswagen       gas        std   
190          3               256   volkswagen       gas        std   
191          0                 ?   volkswagen       gas        std   
192          0                 ?   volkswagen    diesel      turbo   
193          0                 ?   volkswagen       gas        std   
194         -2               103        volvo       gas        std   
195         -1                74        volvo       gas        std   
196         -2               103        volvo       gas        std   
197         -1                74        volvo       gas        std   
198         -2               103        volvo       gas      turbo   
199         -1                74        volvo       gas      turbo   
200         -1                95        volvo       gas        std   
201         -1                95        volvo       gas      turbo   
202         -1                95        volvo       gas        std   
203         -1                95        volvo    diesel      turbo   
204         -1                95        volvo       gas      turbo   

    num-of-doors   body-style drive-wheels engine-location  wheel-base  ...    \
0            two  convertible          rwd           front        88.6  ...     
1            two  convertible          rwd           front        88.6  ...     
2            two    hatchback          rwd           front        94.5  ...     
3           four        sedan          fwd           front        99.8  ...     
4           four        sedan          4wd           front        99.4  ...     
5            two        sedan          fwd           front        99.8  ...     
6           four        sedan          fwd           front       105.8  ...     
7           four        wagon          fwd           front       105.8  ...     
8           four        sedan          fwd           front       105.8  ...     
9            two    hatchback          4wd           front        99.5  ...     
10           two        sedan          rwd           front       101.2  ...     
11          four        sedan          rwd           front       101.2  ...     
12           two        sedan          rwd           front       101.2  ...     
13          four        sedan          rwd           front       101.2  ...     
14          four        sedan          rwd           front       103.5  ...     
15          four        sedan          rwd           front       103.5  ...     
16           two        sedan          rwd           front       103.5  ...     
17          four        sedan          rwd           front       110.0  ...     
18           two    hatchback          fwd           front        88.4  ...     
19           two    hatchback          fwd           front        94.5  ...     
20          four        sedan          fwd           front        94.5  ...     
21           two    hatchback          fwd           front        93.7  ...     
22           two    hatchback          fwd           front        93.7  ...     
23           two    hatchback          fwd           front        93.7  ...     
24          four    hatchback          fwd           front        93.7  ...     
25          four        sedan          fwd           front        93.7  ...     
26          four        sedan          fwd           front        93.7  ...     
27             ?        sedan          fwd           front        93.7  ...     
28          four        wagon          fwd           front       103.3  ...     
29           two    hatchback          fwd           front        95.9  ...     
..           ...          ...          ...             ...         ...  ...     
175         four    hatchback          fwd           front       102.4  ...     
176         four        sedan          fwd           front       102.4  ...     
177         four    hatchback          fwd           front       102.4  ...     
178          two    hatchback          rwd           front       102.9  ...     
179          two    hatchback          rwd           front       102.9  ...     
180         four        sedan          rwd           front       104.5  ...     
181         four        wagon          rwd           front       104.5  ...     
182          two        sedan          fwd           front        97.3  ...     
183          two        sedan          fwd           front        97.3  ...     
184         four        sedan          fwd           front        97.3  ...     
185         four        sedan          fwd           front        97.3  ...     
186         four        sedan          fwd           front        97.3  ...     
187         four        sedan          fwd           front        97.3  ...     
188         four        sedan          fwd           front        97.3  ...     
189          two  convertible          fwd           front        94.5  ...     
190          two    hatchback          fwd           front        94.5  ...     
191         four        sedan          fwd           front       100.4  ...     
192         four        sedan          fwd           front       100.4  ...     
193         four        wagon          fwd           front       100.4  ...     
194         four        sedan          rwd           front       104.3  ...     
195         four        wagon          rwd           front       104.3  ...     
196         four        sedan          rwd           front       104.3  ...     
197         four        wagon          rwd           front       104.3  ...     
198         four        sedan          rwd           front       104.3  ...     
199         four        wagon          rwd           front       104.3  ...     
200         four        sedan          rwd           front       109.1  ...     
201         four        sedan          rwd           front       109.1  ...     
202         four        sedan          rwd           front       109.1  ...     
203         four        sedan          rwd           front       109.1  ...     
204         four        sedan          rwd           front       109.1  ...     

     engine-size  fuel-system  bore  stroke compression-ratio horsepower  \
0            130         mpfi  3.47    2.68              9.00        111   
1            130         mpfi  3.47    2.68              9.00        111   
2            152         mpfi  2.68    3.47              9.00        154   
3            109         mpfi  3.19    3.40             10.00        102   
4            136         mpfi  3.19    3.40              8.00        115   
5            136         mpfi  3.19    3.40              8.50        110   
6            136         mpfi  3.19    3.40              8.50        110   
7            136         mpfi  3.19    3.40              8.50        110   
8            131         mpfi  3.13    3.40              8.30        140   
9            131         mpfi  3.13    3.40              7.00        160   
10           108         mpfi  3.50    2.80              8.80        101   
11           108         mpfi  3.50    2.80              8.80        101   
12           164         mpfi  3.31    3.19              9.00        121   
13           164         mpfi  3.31    3.19              9.00        121   
14           164         mpfi  3.31    3.19              9.00        121   
15           209         mpfi  3.62    3.39              8.00        182   
16           209         mpfi  3.62    3.39              8.00        182   
17           209         mpfi  3.62    3.39              8.00        182   
18            61         2bbl  2.91    3.03              9.50         48   
19            90         2bbl  3.03    3.11              9.60         70   
20            90         2bbl  3.03    3.11              9.60         70   
21            90         2bbl  2.97    3.23              9.41         68   
22            90         2bbl  2.97    3.23              9.40         68   
23            98         mpfi  3.03    3.39              7.60        102   
24            90         2bbl  2.97    3.23              9.40         68   
25            90         2bbl  2.97    3.23              9.40         68   
26            90         2bbl  2.97    3.23              9.40         68   
27            98         mpfi  3.03    3.39              7.60        102   
28           122         2bbl  3.34    3.46              8.50         88   
29           156          mfi  3.60    3.90              7.00        145   
..           ...          ...   ...     ...               ...        ...   
175          122         mpfi  3.31    3.54              8.70         92   
176          122         mpfi  3.31    3.54              8.70         92   
177          122         mpfi  3.31    3.54              8.70         92   
178          171         mpfi  3.27    3.35              9.30        161   
179          171         mpfi  3.27    3.35              9.30        161   
180          171         mpfi  3.27    3.35              9.20        156   
181          161         mpfi  3.27    3.35              9.20        156   
182           97          idi  3.01    3.40             23.00         52   
183          109         mpfi  3.19    3.40              9.00         85   
184           97          idi  3.01    3.40             23.00         52   
185          109         mpfi  3.19    3.40              9.00         85   
186          109         mpfi  3.19    3.40              9.00         85   
187           97          idi  3.01    3.40             23.00         68   
188          109         mpfi  3.19    3.40             10.00        100   
189          109         mpfi  3.19    3.40              8.50         90   
190          109         mpfi  3.19    3.40              8.50         90   
191          136         mpfi  3.19    3.40              8.50        110   
192           97          idi  3.01    3.40             23.00         68   
193          109         mpfi  3.19    3.40              9.00         88   
194          141         mpfi  3.78    3.15              9.50        114   
195          141         mpfi  3.78    3.15              9.50        114   
196          141         mpfi  3.78    3.15              9.50        114   
197          141         mpfi  3.78    3.15              9.50        114   
198          130         mpfi  3.62    3.15              7.50        162   
199          130         mpfi  3.62    3.15              7.50        162   
200          141         mpfi  3.78    3.15              9.50        114   
201          141         mpfi  3.78    3.15              8.70        160   
202          173         mpfi  3.58    2.87              8.80        134   
203          145          idi  3.01    3.40             23.00        106   
204          141         mpfi  3.78    3.15              9.50        114   

     peak-rmp city-mpg highway-mpg  price  
0        5000       21          27  13495  
1        5000       21          27  16500  
2        5000       19          26  16500  
3        5500       24          30  13950  
4        5500       18          22  17450  
5        5500       19          25  15250  
6        5500       19          25  17710  
7        5500       19          25  18920  
8        5500       17          20  23875  
9        5500       16          22      ?  
10       5800       23          29  16430  
11       5800       23          29  16925  
12       4250       21          28  20970  
13       4250       21          28  21105  
14       4250       20          25  24565  
15       5400       16          22  30760  
16       5400       16          22  41315  
17       5400       15          20  36880  
18       5100       47          53   5151  
19       5400       38          43   6295  
20       5400       38          43   6575  
21       5500       37          41   5572  
22       5500       31          38   6377  
23       5500       24          30   7957  
24       5500       31          38   6229  
25       5500       31          38   6692  
26       5500       31          38   7609  
27       5500       24          30   8558  
28       5000       24          30   8921  
29       5000       19          24  12964  
..        ...      ...         ...    ...  
175      4200       27          32   9988  
176      4200       27          32  10898  
177      4200       27          32  11248  
178      5200       20          24  16558  
179      5200       19          24  15998  
180      5200       20          24  15690  
181      5200       19          24  15750  
182      4800       37          46   7775  
183      5250       27          34   7975  
184      4800       37          46   7995  
185      5250       27          34   8195  
186      5250       27          34   8495  
187      4500       37          42   9495  
188      5500       26          32   9995  
189      5500       24          29  11595  
190      5500       24          29   9980  
191      5500       19          24  13295  
192      4500       33          38  13845  
193      5500       25          31  12290  
194      5400       23          28  12940  
195      5400       23          28  13415  
196      5400       24          28  15985  
197      5400       24          28  16515  
198      5100       17          22  18420  
199      5100       17          22  18950  
200      5400       23          28  16845  
201      5300       19          25  19045  
202      5500       18          23  21485  
203      4800       26          27  22470  
204      5400       19          25  22625  

[205 rows x 26 columns]
>>> use dataframes.drop() :
       
SyntaxError: invalid syntax
>>> dataframes.dropna() :
       
SyntaxError: invalid syntax
>>> use dataframes.dropna():
       
SyntaxError: invalid syntax
>>> use df.dropna()
       
SyntaxError: invalid syntax
>>> df.dropna()
       
     symboling normalized-losses         make fuel-type aspiration  \
0            3                 ?  alfa-romero       gas        std   
1            3                 ?  alfa-romero       gas        std   
2            1                 ?  alfa-romero       gas        std   
3            2               164         audi       gas        std   
4            2               164         audi       gas        std   
5            2                 ?         audi       gas        std   
6            1               158         audi       gas        std   
7            1                 ?         audi       gas        std   
8            1               158         audi       gas      turbo   
9            0                 ?         audi       gas      turbo   
10           2               192          bmw       gas        std   
11           0               192          bmw       gas        std   
12           0               188          bmw       gas        std   
13           0               188          bmw       gas        std   
14           1                 ?          bmw       gas        std   
15           0                 ?          bmw       gas        std   
16           0                 ?          bmw       gas        std   
17           0                 ?          bmw       gas        std   
18           2               121    chevrolet       gas        std   
19           1                98    chevrolet       gas        std   
20           0                81    chevrolet       gas        std   
21           1               118        dodge       gas        std   
22           1               118        dodge       gas        std   
23           1               118        dodge       gas      turbo   
24           1               148        dodge       gas        std   
25           1               148        dodge       gas        std   
26           1               148        dodge       gas        std   
27           1               148        dodge       gas      turbo   
28          -1               110        dodge       gas        std   
29           3               145        dodge       gas      turbo   
..         ...               ...          ...       ...        ...   
175         -1                65       toyota       gas        std   
176         -1                65       toyota       gas        std   
177         -1                65       toyota       gas        std   
178          3               197       toyota       gas        std   
179          3               197       toyota       gas        std   
180         -1                90       toyota       gas        std   
181         -1                 ?       toyota       gas        std   
182          2               122   volkswagen    diesel        std   
183          2               122   volkswagen       gas        std   
184          2                94   volkswagen    diesel        std   
185          2                94   volkswagen       gas        std   
186          2                94   volkswagen       gas        std   
187          2                94   volkswagen    diesel      turbo   
188          2                94   volkswagen       gas        std   
189          3                 ?   volkswagen       gas        std   
190          3               256   volkswagen       gas        std   
191          0                 ?   volkswagen       gas        std   
192          0                 ?   volkswagen    diesel      turbo   
193          0                 ?   volkswagen       gas        std   
194         -2               103        volvo       gas        std   
195         -1                74        volvo       gas        std   
196         -2               103        volvo       gas        std   
197         -1                74        volvo       gas        std   
198         -2               103        volvo       gas      turbo   
199         -1                74        volvo       gas      turbo   
200         -1                95        volvo       gas        std   
201         -1                95        volvo       gas      turbo   
202         -1                95        volvo       gas        std   
203         -1                95        volvo    diesel      turbo   
204         -1                95        volvo       gas      turbo   

    num-of-doors   body-style drive-wheels engine-location  wheel-base  ...    \
0            two  convertible          rwd           front        88.6  ...     
1            two  convertible          rwd           front        88.6  ...     
2            two    hatchback          rwd           front        94.5  ...     
3           four        sedan          fwd           front        99.8  ...     
4           four        sedan          4wd           front        99.4  ...     
5            two        sedan          fwd           front        99.8  ...     
6           four        sedan          fwd           front       105.8  ...     
7           four        wagon          fwd           front       105.8  ...     
8           four        sedan          fwd           front       105.8  ...     
9            two    hatchback          4wd           front        99.5  ...     
10           two        sedan          rwd           front       101.2  ...     
11          four        sedan          rwd           front       101.2  ...     
12           two        sedan          rwd           front       101.2  ...     
13          four        sedan          rwd           front       101.2  ...     
14          four        sedan          rwd           front       103.5  ...     
15          four        sedan          rwd           front       103.5  ...     
16           two        sedan          rwd           front       103.5  ...     
17          four        sedan          rwd           front       110.0  ...     
18           two    hatchback          fwd           front        88.4  ...     
19           two    hatchback          fwd           front        94.5  ...     
20          four        sedan          fwd           front        94.5  ...     
21           two    hatchback          fwd           front        93.7  ...     
22           two    hatchback          fwd           front        93.7  ...     
23           two    hatchback          fwd           front        93.7  ...     
24          four    hatchback          fwd           front        93.7  ...     
25          four        sedan          fwd           front        93.7  ...     
26          four        sedan          fwd           front        93.7  ...     
27             ?        sedan          fwd           front        93.7  ...     
28          four        wagon          fwd           front       103.3  ...     
29           two    hatchback          fwd           front        95.9  ...     
..           ...          ...          ...             ...         ...  ...     
175         four    hatchback          fwd           front       102.4  ...     
176         four        sedan          fwd           front       102.4  ...     
177         four    hatchback          fwd           front       102.4  ...     
178          two    hatchback          rwd           front       102.9  ...     
179          two    hatchback          rwd           front       102.9  ...     
180         four        sedan          rwd           front       104.5  ...     
181         four        wagon          rwd           front       104.5  ...     
182          two        sedan          fwd           front        97.3  ...     
183          two        sedan          fwd           front        97.3  ...     
184         four        sedan          fwd           front        97.3  ...     
185         four        sedan          fwd           front        97.3  ...     
186         four        sedan          fwd           front        97.3  ...     
187         four        sedan          fwd           front        97.3  ...     
188         four        sedan          fwd           front        97.3  ...     
189          two  convertible          fwd           front        94.5  ...     
190          two    hatchback          fwd           front        94.5  ...     
191         four        sedan          fwd           front       100.4  ...     
192         four        sedan          fwd           front       100.4  ...     
193         four        wagon          fwd           front       100.4  ...     
194         four        sedan          rwd           front       104.3  ...     
195         four        wagon          rwd           front       104.3  ...     
196         four        sedan          rwd           front       104.3  ...     
197         four        wagon          rwd           front       104.3  ...     
198         four        sedan          rwd           front       104.3  ...     
199         four        wagon          rwd           front       104.3  ...     
200         four        sedan          rwd           front       109.1  ...     
201         four        sedan          rwd           front       109.1  ...     
202         four        sedan          rwd           front       109.1  ...     
203         four        sedan          rwd           front       109.1  ...     
204         four        sedan          rwd           front       109.1  ...     

     engine-size  fuel-system  bore  stroke compression-ratio horsepower  \
0            130         mpfi  3.47    2.68              9.00        111   
1            130         mpfi  3.47    2.68              9.00        111   
2            152         mpfi  2.68    3.47              9.00        154   
3            109         mpfi  3.19    3.40             10.00        102   
4            136         mpfi  3.19    3.40              8.00        115   
5            136         mpfi  3.19    3.40              8.50        110   
6            136         mpfi  3.19    3.40              8.50        110   
7            136         mpfi  3.19    3.40              8.50        110   
8            131         mpfi  3.13    3.40              8.30        140   
9            131         mpfi  3.13    3.40              7.00        160   
10           108         mpfi  3.50    2.80              8.80        101   
11           108         mpfi  3.50    2.80              8.80        101   
12           164         mpfi  3.31    3.19              9.00        121   
13           164         mpfi  3.31    3.19              9.00        121   
14           164         mpfi  3.31    3.19              9.00        121   
15           209         mpfi  3.62    3.39              8.00        182   
16           209         mpfi  3.62    3.39              8.00        182   
17           209         mpfi  3.62    3.39              8.00        182   
18            61         2bbl  2.91    3.03              9.50         48   
19            90         2bbl  3.03    3.11              9.60         70   
20            90         2bbl  3.03    3.11              9.60         70   
21            90         2bbl  2.97    3.23              9.41         68   
22            90         2bbl  2.97    3.23              9.40         68   
23            98         mpfi  3.03    3.39              7.60        102   
24            90         2bbl  2.97    3.23              9.40         68   
25            90         2bbl  2.97    3.23              9.40         68   
26            90         2bbl  2.97    3.23              9.40         68   
27            98         mpfi  3.03    3.39              7.60        102   
28           122         2bbl  3.34    3.46              8.50         88   
29           156          mfi  3.60    3.90              7.00        145   
..           ...          ...   ...     ...               ...        ...   
175          122         mpfi  3.31    3.54              8.70         92   
176          122         mpfi  3.31    3.54              8.70         92   
177          122         mpfi  3.31    3.54              8.70         92   
178          171         mpfi  3.27    3.35              9.30        161   
179          171         mpfi  3.27    3.35              9.30        161   
180          171         mpfi  3.27    3.35              9.20        156   
181          161         mpfi  3.27    3.35              9.20        156   
182           97          idi  3.01    3.40             23.00         52   
183          109         mpfi  3.19    3.40              9.00         85   
184           97          idi  3.01    3.40             23.00         52   
185          109         mpfi  3.19    3.40              9.00         85   
186          109         mpfi  3.19    3.40              9.00         85   
187           97          idi  3.01    3.40             23.00         68   
188          109         mpfi  3.19    3.40             10.00        100   
189          109         mpfi  3.19    3.40              8.50         90   
190          109         mpfi  3.19    3.40              8.50         90   
191          136         mpfi  3.19    3.40              8.50        110   
192           97          idi  3.01    3.40             23.00         68   
193          109         mpfi  3.19    3.40              9.00         88   
194          141         mpfi  3.78    3.15              9.50        114   
195          141         mpfi  3.78    3.15              9.50        114   
196          141         mpfi  3.78    3.15              9.50        114   
197          141         mpfi  3.78    3.15              9.50        114   
198          130         mpfi  3.62    3.15              7.50        162   
199          130         mpfi  3.62    3.15              7.50        162   
200          141         mpfi  3.78    3.15              9.50        114   
201          141         mpfi  3.78    3.15              8.70        160   
202          173         mpfi  3.58    2.87              8.80        134   
203          145          idi  3.01    3.40             23.00        106   
204          141         mpfi  3.78    3.15              9.50        114   

     peak-rmp city-mpg highway-mpg  price  
0        5000       21          27  13495  
1        5000       21          27  16500  
2        5000       19          26  16500  
3        5500       24          30  13950  
4        5500       18          22  17450  
5        5500       19          25  15250  
6        5500       19          25  17710  
7        5500       19          25  18920  
8        5500       17          20  23875  
9        5500       16          22      ?  
10       5800       23          29  16430  
11       5800       23          29  16925  
12       4250       21          28  20970  
13       4250       21          28  21105  
14       4250       20          25  24565  
15       5400       16          22  30760  
16       5400       16          22  41315  
17       5400       15          20  36880  
18       5100       47          53   5151  
19       5400       38          43   6295  
20       5400       38          43   6575  
21       5500       37          41   5572  
22       5500       31          38   6377  
23       5500       24          30   7957  
24       5500       31          38   6229  
25       5500       31          38   6692  
26       5500       31          38   7609  
27       5500       24          30   8558  
28       5000       24          30   8921  
29       5000       19          24  12964  
..        ...      ...         ...    ...  
175      4200       27          32   9988  
176      4200       27          32  10898  
177      4200       27          32  11248  
178      5200       20          24  16558  
179      5200       19          24  15998  
180      5200       20          24  15690  
181      5200       19          24  15750  
182      4800       37          46   7775  
183      5250       27          34   7975  
184      4800       37          46   7995  
185      5250       27          34   8195  
186      5250       27          34   8495  
187      4500       37          42   9495  
188      5500       26          32   9995  
189      5500       24          29  11595  
190      5500       24          29   9980  
191      5500       19          24  13295  
192      4500       33          38  13845  
193      5500       25          31  12290  
194      5400       23          28  12940  
195      5400       23          28  13415  
196      5400       24          28  15985  
197      5400       24          28  16515  
198      5100       17          22  18420  
199      5100       17          22  18950  
200      5400       23          28  16845  
201      5300       19          25  19045  
202      5500       18          23  21485  
203      4800       26          27  22470  
204      5400       19          25  22625  

[205 rows x 26 columns]
>>> df.dropna(subset=["price"],axis=0,inplaceTrue)
       
SyntaxError: positional argument follows keyword argument
>>> df.dropna(subset=["price"], axis=0, inplace =True)
       
>>> df
       
     symboling normalized-losses         make fuel-type aspiration  \
0            3                 ?  alfa-romero       gas        std   
1            3                 ?  alfa-romero       gas        std   
2            1                 ?  alfa-romero       gas        std   
3            2               164         audi       gas        std   
4            2               164         audi       gas        std   
5            2                 ?         audi       gas        std   
6            1               158         audi       gas        std   
7            1                 ?         audi       gas        std   
8            1               158         audi       gas      turbo   
9            0                 ?         audi       gas      turbo   
10           2               192          bmw       gas        std   
11           0               192          bmw       gas        std   
12           0               188          bmw       gas        std   
13           0               188          bmw       gas        std   
14           1                 ?          bmw       gas        std   
15           0                 ?          bmw       gas        std   
16           0                 ?          bmw       gas        std   
17           0                 ?          bmw       gas        std   
18           2               121    chevrolet       gas        std   
19           1                98    chevrolet       gas        std   
20           0                81    chevrolet       gas        std   
21           1               118        dodge       gas        std   
22           1               118        dodge       gas        std   
23           1               118        dodge       gas      turbo   
24           1               148        dodge       gas        std   
25           1               148        dodge       gas        std   
26           1               148        dodge       gas        std   
27           1               148        dodge       gas      turbo   
28          -1               110        dodge       gas        std   
29           3               145        dodge       gas      turbo   
..         ...               ...          ...       ...        ...   
175         -1                65       toyota       gas        std   
176         -1                65       toyota       gas        std   
177         -1                65       toyota       gas        std   
178          3               197       toyota       gas        std   
179          3               197       toyota       gas        std   
180         -1                90       toyota       gas        std   
181         -1                 ?       toyota       gas        std   
182          2               122   volkswagen    diesel        std   
183          2               122   volkswagen       gas        std   
184          2                94   volkswagen    diesel        std   
185          2                94   volkswagen       gas        std   
186          2                94   volkswagen       gas        std   
187          2                94   volkswagen    diesel      turbo   
188          2                94   volkswagen       gas        std   
189          3                 ?   volkswagen       gas        std   
190          3               256   volkswagen       gas        std   
191          0                 ?   volkswagen       gas        std   
192          0                 ?   volkswagen    diesel      turbo   
193          0                 ?   volkswagen       gas        std   
194         -2               103        volvo       gas        std   
195         -1                74        volvo       gas        std   
196         -2               103        volvo       gas        std   
197         -1                74        volvo       gas        std   
198         -2               103        volvo       gas      turbo   
199         -1                74        volvo       gas      turbo   
200         -1                95        volvo       gas        std   
201         -1                95        volvo       gas      turbo   
202         -1                95        volvo       gas        std   
203         -1                95        volvo    diesel      turbo   
204         -1                95        volvo       gas      turbo   

    num-of-doors   body-style drive-wheels engine-location  wheel-base  ...    \
0            two  convertible          rwd           front        88.6  ...     
1            two  convertible          rwd           front        88.6  ...     
2            two    hatchback          rwd           front        94.5  ...     
3           four        sedan          fwd           front        99.8  ...     
4           four        sedan          4wd           front        99.4  ...     
5            two        sedan          fwd           front        99.8  ...     
6           four        sedan          fwd           front       105.8  ...     
7           four        wagon          fwd           front       105.8  ...     
8           four        sedan          fwd           front       105.8  ...     
9            two    hatchback          4wd           front        99.5  ...     
10           two        sedan          rwd           front       101.2  ...     
11          four        sedan          rwd           front       101.2  ...     
12           two        sedan          rwd           front       101.2  ...     
13          four        sedan          rwd           front       101.2  ...     
14          four        sedan          rwd           front       103.5  ...     
15          four        sedan          rwd           front       103.5  ...     
16           two        sedan          rwd           front       103.5  ...     
17          four        sedan          rwd           front       110.0  ...     
18           two    hatchback          fwd           front        88.4  ...     
19           two    hatchback          fwd           front        94.5  ...     
20          four        sedan          fwd           front        94.5  ...     
21           two    hatchback          fwd           front        93.7  ...     
22           two    hatchback          fwd           front        93.7  ...     
23           two    hatchback          fwd           front        93.7  ...     
24          four    hatchback          fwd           front        93.7  ...     
25          four        sedan          fwd           front        93.7  ...     
26          four        sedan          fwd           front        93.7  ...     
27             ?        sedan          fwd           front        93.7  ...     
28          four        wagon          fwd           front       103.3  ...     
29           two    hatchback          fwd           front        95.9  ...     
..           ...          ...          ...             ...         ...  ...     
175         four    hatchback          fwd           front       102.4  ...     
176         four        sedan          fwd           front       102.4  ...     
177         four    hatchback          fwd           front       102.4  ...     
178          two    hatchback          rwd           front       102.9  ...     
179          two    hatchback          rwd           front       102.9  ...     
180         four        sedan          rwd           front       104.5  ...     
181         four        wagon          rwd           front       104.5  ...     
182          two        sedan          fwd           front        97.3  ...     
183          two        sedan          fwd           front        97.3  ...     
184         four        sedan          fwd           front        97.3  ...     
185         four        sedan          fwd           front        97.3  ...     
186         four        sedan          fwd           front        97.3  ...     
187         four        sedan          fwd           front        97.3  ...     
188         four        sedan          fwd           front        97.3  ...     
189          two  convertible          fwd           front        94.5  ...     
190          two    hatchback          fwd           front        94.5  ...     
191         four        sedan          fwd           front       100.4  ...     
192         four        sedan          fwd           front       100.4  ...     
193         four        wagon          fwd           front       100.4  ...     
194         four        sedan          rwd           front       104.3  ...     
195         four        wagon          rwd           front       104.3  ...     
196         four        sedan          rwd           front       104.3  ...     
197         four        wagon          rwd           front       104.3  ...     
198         four        sedan          rwd           front       104.3  ...     
199         four        wagon          rwd           front       104.3  ...     
200         four        sedan          rwd           front       109.1  ...     
201         four        sedan          rwd           front       109.1  ...     
202         four        sedan          rwd           front       109.1  ...     
203         four        sedan          rwd           front       109.1  ...     
204         four        sedan          rwd           front       109.1  ...     

     engine-size  fuel-system  bore  stroke compression-ratio horsepower  \
0            130         mpfi  3.47    2.68              9.00        111   
1            130         mpfi  3.47    2.68              9.00        111   
2            152         mpfi  2.68    3.47              9.00        154   
3            109         mpfi  3.19    3.40             10.00        102   
4            136         mpfi  3.19    3.40              8.00        115   
5            136         mpfi  3.19    3.40              8.50        110   
6            136         mpfi  3.19    3.40              8.50        110   
7            136         mpfi  3.19    3.40              8.50        110   
8            131         mpfi  3.13    3.40              8.30        140   
9            131         mpfi  3.13    3.40              7.00        160   
10           108         mpfi  3.50    2.80              8.80        101   
11           108         mpfi  3.50    2.80              8.80        101   
12           164         mpfi  3.31    3.19              9.00        121   
13           164         mpfi  3.31    3.19              9.00        121   
14           164         mpfi  3.31    3.19              9.00        121   
15           209         mpfi  3.62    3.39              8.00        182   
16           209         mpfi  3.62    3.39              8.00        182   
17           209         mpfi  3.62    3.39              8.00        182   
18            61         2bbl  2.91    3.03              9.50         48   
19            90         2bbl  3.03    3.11              9.60         70   
20            90         2bbl  3.03    3.11              9.60         70   
21            90         2bbl  2.97    3.23              9.41         68   
22            90         2bbl  2.97    3.23              9.40         68   
23            98         mpfi  3.03    3.39              7.60        102   
24            90         2bbl  2.97    3.23              9.40         68   
25            90         2bbl  2.97    3.23              9.40         68   
26            90         2bbl  2.97    3.23              9.40         68   
27            98         mpfi  3.03    3.39              7.60        102   
28           122         2bbl  3.34    3.46              8.50         88   
29           156          mfi  3.60    3.90              7.00        145   
..           ...          ...   ...     ...               ...        ...   
175          122         mpfi  3.31    3.54              8.70         92   
176          122         mpfi  3.31    3.54              8.70         92   
177          122         mpfi  3.31    3.54              8.70         92   
178          171         mpfi  3.27    3.35              9.30        161   
179          171         mpfi  3.27    3.35              9.30        161   
180          171         mpfi  3.27    3.35              9.20        156   
181          161         mpfi  3.27    3.35              9.20        156   
182           97          idi  3.01    3.40             23.00         52   
183          109         mpfi  3.19    3.40              9.00         85   
184           97          idi  3.01    3.40             23.00         52   
185          109         mpfi  3.19    3.40              9.00         85   
186          109         mpfi  3.19    3.40              9.00         85   
187           97          idi  3.01    3.40             23.00         68   
188          109         mpfi  3.19    3.40             10.00        100   
189          109         mpfi  3.19    3.40              8.50         90   
190          109         mpfi  3.19    3.40              8.50         90   
191          136         mpfi  3.19    3.40              8.50        110   
192           97          idi  3.01    3.40             23.00         68   
193          109         mpfi  3.19    3.40              9.00         88   
194          141         mpfi  3.78    3.15              9.50        114   
195          141         mpfi  3.78    3.15              9.50        114   
196          141         mpfi  3.78    3.15              9.50        114   
197          141         mpfi  3.78    3.15              9.50        114   
198          130         mpfi  3.62    3.15              7.50        162   
199          130         mpfi  3.62    3.15              7.50        162   
200          141         mpfi  3.78    3.15              9.50        114   
201          141         mpfi  3.78    3.15              8.70        160   
202          173         mpfi  3.58    2.87              8.80        134   
203          145          idi  3.01    3.40             23.00        106   
204          141         mpfi  3.78    3.15              9.50        114   

     peak-rmp city-mpg highway-mpg  price  
0        5000       21          27  13495  
1        5000       21          27  16500  
2        5000       19          26  16500  
3        5500       24          30  13950  
4        5500       18          22  17450  
5        5500       19          25  15250  
6        5500       19          25  17710  
7        5500       19          25  18920  
8        5500       17          20  23875  
9        5500       16          22      ?  
10       5800       23          29  16430  
11       5800       23          29  16925  
12       4250       21          28  20970  
13       4250       21          28  21105  
14       4250       20          25  24565  
15       5400       16          22  30760  
16       5400       16          22  41315  
17       5400       15          20  36880  
18       5100       47          53   5151  
19       5400       38          43   6295  
20       5400       38          43   6575  
21       5500       37          41   5572  
22       5500       31          38   6377  
23       5500       24          30   7957  
24       5500       31          38   6229  
25       5500       31          38   6692  
26       5500       31          38   7609  
27       5500       24          30   8558  
28       5000       24          30   8921  
29       5000       19          24  12964  
..        ...      ...         ...    ...  
175      4200       27          32   9988  
176      4200       27          32  10898  
177      4200       27          32  11248  
178      5200       20          24  16558  
179      5200       19          24  15998  
180      5200       20          24  15690  
181      5200       19          24  15750  
182      4800       37          46   7775  
183      5250       27          34   7975  
184      4800       37          46   7995  
185      5250       27          34   8195  
186      5250       27          34   8495  
187      4500       37          42   9495  
188      5500       26          32   9995  
189      5500       24          29  11595  
190      5500       24          29   9980  
191      5500       19          24  13295  
192      4500       33          38  13845  
193      5500       25          31  12290  
194      5400       23          28  12940  
195      5400       23          28  13415  
196      5400       24          28  15985  
197      5400       24          28  16515  
198      5100       17          22  18420  
199      5100       17          22  18950  
200      5400       23          28  16845  
201      5300       19          25  19045  
202      5500       18          23  21485  
203      4800       26          27  22470  
204      5400       19          25  22625  

[205 rows x 26 columns]
>>> df=df.dropna(subset=["price"],axis=0)
       
>>> df
       
     symboling normalized-losses         make fuel-type aspiration  \
0            3                 ?  alfa-romero       gas        std   
1            3                 ?  alfa-romero       gas        std   
2            1                 ?  alfa-romero       gas        std   
3            2               164         audi       gas        std   
4            2               164         audi       gas        std   
5            2                 ?         audi       gas        std   
6            1               158         audi       gas        std   
7            1                 ?         audi       gas        std   
8            1               158         audi       gas      turbo   
9            0                 ?         audi       gas      turbo   
10           2               192          bmw       gas        std   
11           0               192          bmw       gas        std   
12           0               188          bmw       gas        std   
13           0               188          bmw       gas        std   
14           1                 ?          bmw       gas        std   
15           0                 ?          bmw       gas        std   
16           0                 ?          bmw       gas        std   
17           0                 ?          bmw       gas        std   
18           2               121    chevrolet       gas        std   
19           1                98    chevrolet       gas        std   
20           0                81    chevrolet       gas        std   
21           1               118        dodge       gas        std   
22           1               118        dodge       gas        std   
23           1               118        dodge       gas      turbo   
24           1               148        dodge       gas        std   
25           1               148        dodge       gas        std   
26           1               148        dodge       gas        std   
27           1               148        dodge       gas      turbo   
28          -1               110        dodge       gas        std   
29           3               145        dodge       gas      turbo   
..         ...               ...          ...       ...        ...   
175         -1                65       toyota       gas        std   
176         -1                65       toyota       gas        std   
177         -1                65       toyota       gas        std   
178          3               197       toyota       gas        std   
179          3               197       toyota       gas        std   
180         -1                90       toyota       gas        std   
181         -1                 ?       toyota       gas        std   
182          2               122   volkswagen    diesel        std   
183          2               122   volkswagen       gas        std   
184          2                94   volkswagen    diesel        std   
185          2                94   volkswagen       gas        std   
186          2                94   volkswagen       gas        std   
187          2                94   volkswagen    diesel      turbo   
188          2                94   volkswagen       gas        std   
189          3                 ?   volkswagen       gas        std   
190          3               256   volkswagen       gas        std   
191          0                 ?   volkswagen       gas        std   
192          0                 ?   volkswagen    diesel      turbo   
193          0                 ?   volkswagen       gas        std   
194         -2               103        volvo       gas        std   
195         -1                74        volvo       gas        std   
196         -2               103        volvo       gas        std   
197         -1                74        volvo       gas        std   
198         -2               103        volvo       gas      turbo   
199         -1                74        volvo       gas      turbo   
200         -1                95        volvo       gas        std   
201         -1                95        volvo       gas      turbo   
202         -1                95        volvo       gas        std   
203         -1                95        volvo    diesel      turbo   
204         -1                95        volvo       gas      turbo   

    num-of-doors   body-style drive-wheels engine-location  wheel-base  ...    \
0            two  convertible          rwd           front        88.6  ...     
1            two  convertible          rwd           front        88.6  ...     
2            two    hatchback          rwd           front        94.5  ...     
3           four        sedan          fwd           front        99.8  ...     
4           four        sedan          4wd           front        99.4  ...     
5            two        sedan          fwd           front        99.8  ...     
6           four        sedan          fwd           front       105.8  ...     
7           four        wagon          fwd           front       105.8  ...     
8           four        sedan          fwd           front       105.8  ...     
9            two    hatchback          4wd           front        99.5  ...     
10           two        sedan          rwd           front       101.2  ...     
11          four        sedan          rwd           front       101.2  ...     
12           two        sedan          rwd           front       101.2  ...     
13          four        sedan          rwd           front       101.2  ...     
14          four        sedan          rwd           front       103.5  ...     
15          four        sedan          rwd           front       103.5  ...     
16           two        sedan          rwd           front       103.5  ...     
17          four        sedan          rwd           front       110.0  ...     
18           two    hatchback          fwd           front        88.4  ...     
19           two    hatchback          fwd           front        94.5  ...     
20          four        sedan          fwd           front        94.5  ...     
21           two    hatchback          fwd           front        93.7  ...     
22           two    hatchback          fwd           front        93.7  ...     
23           two    hatchback          fwd           front        93.7  ...     
24          four    hatchback          fwd           front        93.7  ...     
25          four        sedan          fwd           front        93.7  ...     
26          four        sedan          fwd           front        93.7  ...     
27             ?        sedan          fwd           front        93.7  ...     
28          four        wagon          fwd           front       103.3  ...     
29           two    hatchback          fwd           front        95.9  ...     
..           ...          ...          ...             ...         ...  ...     
175         four    hatchback          fwd           front       102.4  ...     
176         four        sedan          fwd           front       102.4  ...     
177         four    hatchback          fwd           front       102.4  ...     
178          two    hatchback          rwd           front       102.9  ...     
179          two    hatchback          rwd           front       102.9  ...     
180         four        sedan          rwd           front       104.5  ...     
181         four        wagon          rwd           front       104.5  ...     
182          two        sedan          fwd           front        97.3  ...     
183          two        sedan          fwd           front        97.3  ...     
184         four        sedan          fwd           front        97.3  ...     
185         four        sedan          fwd           front        97.3  ...     
186         four        sedan          fwd           front        97.3  ...     
187         four        sedan          fwd           front        97.3  ...     
188         four        sedan          fwd           front        97.3  ...     
189          two  convertible          fwd           front        94.5  ...     
190          two    hatchback          fwd           front        94.5  ...     
191         four        sedan          fwd           front       100.4  ...     
192         four        sedan          fwd           front       100.4  ...     
193         four        wagon          fwd           front       100.4  ...     
194         four        sedan          rwd           front       104.3  ...     
195         four        wagon          rwd           front       104.3  ...     
196         four        sedan          rwd           front       104.3  ...     
197         four        wagon          rwd           front       104.3  ...     
198         four        sedan          rwd           front       104.3  ...     
199         four        wagon          rwd           front       104.3  ...     
200         four        sedan          rwd           front       109.1  ...     
201         four        sedan          rwd           front       109.1  ...     
202         four        sedan          rwd           front       109.1  ...     
203         four        sedan          rwd           front       109.1  ...     
204         four        sedan          rwd           front       109.1  ...     

     engine-size  fuel-system  bore  stroke compression-ratio horsepower  \
0            130         mpfi  3.47    2.68              9.00        111   
1            130         mpfi  3.47    2.68              9.00        111   
2            152         mpfi  2.68    3.47              9.00        154   
3            109         mpfi  3.19    3.40             10.00        102   
4            136         mpfi  3.19    3.40              8.00        115   
5            136         mpfi  3.19    3.40              8.50        110   
6            136         mpfi  3.19    3.40              8.50        110   
7            136         mpfi  3.19    3.40              8.50        110   
8            131         mpfi  3.13    3.40              8.30        140   
9            131         mpfi  3.13    3.40              7.00        160   
10           108         mpfi  3.50    2.80              8.80        101   
11           108         mpfi  3.50    2.80              8.80        101   
12           164         mpfi  3.31    3.19              9.00        121   
13           164         mpfi  3.31    3.19              9.00        121   
14           164         mpfi  3.31    3.19              9.00        121   
15           209         mpfi  3.62    3.39              8.00        182   
16           209         mpfi  3.62    3.39              8.00        182   
17           209         mpfi  3.62    3.39              8.00        182   
18            61         2bbl  2.91    3.03              9.50         48   
19            90         2bbl  3.03    3.11              9.60         70   
20            90         2bbl  3.03    3.11              9.60         70   
21            90         2bbl  2.97    3.23              9.41         68   
22            90         2bbl  2.97    3.23              9.40         68   
23            98         mpfi  3.03    3.39              7.60        102   
24            90         2bbl  2.97    3.23              9.40         68   
25            90         2bbl  2.97    3.23              9.40         68   
26            90         2bbl  2.97    3.23              9.40         68   
27            98         mpfi  3.03    3.39              7.60        102   
28           122         2bbl  3.34    3.46              8.50         88   
29           156          mfi  3.60    3.90              7.00        145   
..           ...          ...   ...     ...               ...        ...   
175          122         mpfi  3.31    3.54              8.70         92   
176          122         mpfi  3.31    3.54              8.70         92   
177          122         mpfi  3.31    3.54              8.70         92   
178          171         mpfi  3.27    3.35              9.30        161   
179          171         mpfi  3.27    3.35              9.30        161   
180          171         mpfi  3.27    3.35              9.20        156   
181          161         mpfi  3.27    3.35              9.20        156   
182           97          idi  3.01    3.40             23.00         52   
183          109         mpfi  3.19    3.40              9.00         85   
184           97          idi  3.01    3.40             23.00         52   
185          109         mpfi  3.19    3.40              9.00         85   
186          109         mpfi  3.19    3.40              9.00         85   
187           97          idi  3.01    3.40             23.00         68   
188          109         mpfi  3.19    3.40             10.00        100   
189          109         mpfi  3.19    3.40              8.50         90   
190          109         mpfi  3.19    3.40              8.50         90   
191          136         mpfi  3.19    3.40              8.50        110   
192           97          idi  3.01    3.40             23.00         68   
193          109         mpfi  3.19    3.40              9.00         88   
194          141         mpfi  3.78    3.15              9.50        114   
195          141         mpfi  3.78    3.15              9.50        114   
196          141         mpfi  3.78    3.15              9.50        114   
197          141         mpfi  3.78    3.15              9.50        114   
198          130         mpfi  3.62    3.15              7.50        162   
199          130         mpfi  3.62    3.15              7.50        162   
200          141         mpfi  3.78    3.15              9.50        114   
201          141         mpfi  3.78    3.15              8.70        160   
202          173         mpfi  3.58    2.87              8.80        134   
203          145          idi  3.01    3.40             23.00        106   
204          141         mpfi  3.78    3.15              9.50        114   

     peak-rmp city-mpg highway-mpg  price  
0        5000       21          27  13495  
1        5000       21          27  16500  
2        5000       19          26  16500  
3        5500       24          30  13950  
4        5500       18          22  17450  
5        5500       19          25  15250  
6        5500       19          25  17710  
7        5500       19          25  18920  
8        5500       17          20  23875  
9        5500       16          22      ?  
10       5800       23          29  16430  
11       5800       23          29  16925  
12       4250       21          28  20970  
13       4250       21          28  21105  
14       4250       20          25  24565  
15       5400       16          22  30760  
16       5400       16          22  41315  
17       5400       15          20  36880  
18       5100       47          53   5151  
19       5400       38          43   6295  
20       5400       38          43   6575  
21       5500       37          41   5572  
22       5500       31          38   6377  
23       5500       24          30   7957  
24       5500       31          38   6229  
25       5500       31          38   6692  
26       5500       31          38   7609  
27       5500       24          30   8558  
28       5000       24          30   8921  
29       5000       19          24  12964  
..        ...      ...         ...    ...  
175      4200       27          32   9988  
176      4200       27          32  10898  
177      4200       27          32  11248  
178      5200       20          24  16558  
179      5200       19          24  15998  
180      5200       20          24  15690  
181      5200       19          24  15750  
182      4800       37          46   7775  
183      5250       27          34   7975  
184      4800       37          46   7995  
185      5250       27          34   8195  
186      5250       27          34   8495  
187      4500       37          42   9495  
188      5500       26          32   9995  
189      5500       24          29  11595  
190      5500       24          29   9980  
191      5500       19          24  13295  
192      4500       33          38  13845  
193      5500       25          31  12290  
194      5400       23          28  12940  
195      5400       23          28  13415  
196      5400       24          28  15985  
197      5400       24          28  16515  
198      5100       17          22  18420  
199      5100       17          22  18950  
200      5400       23          28  16845  
201      5300       19          25  19045  
202      5500       18          23  21485  
203      4800       26          27  22470  
204      5400       19          25  22625  

[205 rows x 26 columns]
>>> 
