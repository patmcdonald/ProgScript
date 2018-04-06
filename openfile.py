#Pat McDonald
#Exercise 5: Programming and Scripting
#Working with Fishers Iris dataset. Source: https://archive.ics.uci.edu/ml/datasets/iris

with open("data/iris.csv") as f:
  contents = f.read() 
  print(contents)