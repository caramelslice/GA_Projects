All graphs are all nicely presented with labels and clear colors. I love this concept exploring 311 data and also beautiful use of the map scatter plots. Here I will just discuss on the things I might do differently. 


***Presentation***
Some sections include analysis some don't. It will be very helpful to include some section titles or # comments about purpose of a particular code block. It will make it a lot more easier for us who are doing the peer asssement.    

 
***Code***
I have a feeling that you probably come from a OOP background and that you are probably a really good Python programmer. But there are a few places where we probably could have used the powerful Pandas' split, apply or combine functions to transform the data. 

```
data_311['Hour'] = [date.strftime('%H') for date in data_311['Created Date']]
```

Also here, the Pandas sort function would be easier than the below code block. 

```
a_count={}
for row in data_311.index:
   if data_311['Agency'][row] in a_count:
        a_count[data_311['Agency'][row]] += 1
   else:
      a_count[data_311['Agency'][row]] = 1


from collections import OrderedDict
from operator import itemgetter
d = OrderedDict(sorted(a_count.items(), key=itemgetter(1), reverse = 1))
d
```

Most parts of the analysis are done using count or sum. We probably could also look at the medians or means to help us understand the data better. Another thing we can consider is probably using feature scaling to scale the all values within a similar range. For example, code [43] shows the Total and DOT as the highest on the charts, but all other lines may be somewhat hard for the audience to trace and reach a conclusion. 