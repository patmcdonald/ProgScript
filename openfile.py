#Pat McDonald
#Exercise 5: Programming and Scripting
#Working with Fishers Iris dataset. Source: https://archive.ics.uci.edu/ml/datasets/iris

#Open the iris dataset
with open("data/iris.csv") as f:
  #Loop through each line
  for line in f:
    #Split and print each line of string values
    print(line.split(',' [:4]))
