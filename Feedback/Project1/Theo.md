This analysis is very well presented. 
It uses some very good techniques such as feature scaling and using dummy variables. Good visual data exploration from different sides of the dataset by property types, years, and data reported methods. 


A few suggestions:  
Lambda, serving the purpose of an anoynomous function 

```
def make_manual(x):
    if pd.notnull(x):
        return 'Manual'
    else:
        return np.NaN
    
ll84_2011['water_method'] = ll84_2011['water_ft2'].apply(lambda x: make_manual(x))
```
probably can be simplified as: 

```
ll84_2011['water_method'] = ll84_2011['water_ft2'].apply(lambda x: 'Manual' if pd.notnull(x) else np.NaN)
```

The same concept could be applied to other lambda functions which use user-defined functions in the analysis.  


Feature Scaling. Code [54].  

Is there a reason why we standardized our values by dividing the max value within each subgroup rather than scaling to the range of [0,1] or [-1,1], using z-score, or scaling it to unit length? From my understanding is that the features should fall the within the same range. Here our floor_area_localnorm is a lot more bigger than say EUIwn_localnorm or GHG_localnorm. 

I was hoping to see some regerssion analysis created using the dummy variables years, boroughs and water_method. Perhaps I've missed it, but I don't recall seeing many. I imagine you would use it in future projects. 