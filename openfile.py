#Pat McDonald
#Exercise 5: Programming and Scripting
#Working with Fishers Iris dataset. Source: https://archive.ics.uci.edu/ml/datasets/iris

#Open the iris dataset
with open("data/iris.csv") as f:
  #Loop through each line
  for line in f:
    #Split and print each line of string values
    #Code by Mohamed Noor;https://learnonline.gmit.ie/mod/forum/discuss.php?d=14986#p29763 
        line = line.replace(',', ' ')
        line = line.rstrip()
        print(line[:11], line[12:16].strip())