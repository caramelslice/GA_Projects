Clear analysis, very easy to read with titles and explanation of each section, good application of pretty much all kind of data visualization plots we learnt in class. I love how you use scatter matrix to see the relationship among different features. I also like that you showed all the subsetted dataframes so the audience could understand your analysis faster. 

Here are some of the things I probably would have done differently. 


```
beer_df['cnt'] = df.groupby(df.index)['beer_name'].count()
print beer_df.cnt.describe()
beer_df.cnt.plot(kind='box')
```

Here in beer_df.cnt.plot(kind='box'), we are plotting a column, so the box plot is probably going to plot all the data in one line. To use box plots, we might want to pass different columns, like this: 

```
df = DataFrame(rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot(kind='box')
```

I could not find the original pickle file in the data directory. So I can't be 100% sure the below code will work. But I would imagine it's something like this below. Also, we might want to convert beer_name to dummy variables first so you can plot them by their names. 
```
df['beer_name', 'cnt'].boxplot(by='beer_name')
```
P.S. I found this [Beer Data](http://www.craftbeeranalytics.com/beer-data.html) while I was doing my project. I thought you'd be interested. 
I look forward to reading your prediction about what people like and your recommendation about the new beer. 
