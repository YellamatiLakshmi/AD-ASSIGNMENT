import matplotlib.pyplot as plt

#sample data
data = [5,7,7,8,9,10,10,11,12,11,11]

#create histogram
plt.hist(data, bins = 10, edgecolor = 'black')

#title and labels for the plot
plt.title("Simple histogram example")
plt.xlabel("Numbers")
plt.ylabel("Count")

#show the plot
plt.show()






import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
dataf = pd.DataFrame({"Season 1" : [7, 7, 5, 5, 6],
                   "Season 2" : [1, 2, 8, 4, 9]})
p = sns.histplot(data = dataf)
p.set(xlabel = "X Label Vale", ylabel = "Y Label Value")
plt.show()