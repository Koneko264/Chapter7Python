def outputTable(title, header1, header2, strList, intList):
   """
       Function that prints the contents in tabular format
   """
  
   # Printing title
   print("\n\n %33s \n" %(title));
  
   # Printing header
   print("\n %-20s %-10s %-23s \n" %(header1, "|", header2));
  
   print("\n -------------------------------------------- \n");
  
   # Printing formatted output
   for i in range(0, len(strList)):
       print("\n %-20s %-10s %-23d " %(strList[i], "|", intList[i]));
      
   print("\n");

  
def outputHistogram(strList, intList):
   """
       Function that prints the contents in tabular format
   """
  
   print("\n\n");
  
   # Printing names
   for i in range(0, len(strList)):
       print("\n %20s %-5s " %(strList[i], " "), end = "");
      
       # Printing *'s
       for j in range(0, intList[i]):
           print("*", end="");
      
   print("\n");
  
  
def chkCommas(dataPoint):
   """
       Function that validates commas error checking
   """
  
   # Checking for non-existence of comma
   if ',' not in dataPoint:
       print('\n Error: No comma in string. \n');
       return False;
  
   # Checking for more than comma  
   elif dataPoint.count(",") > 1:
       print('\n Error: Too many commas in input. \n');
       return False;
  
   # Checking for integer after comma
   else:
      
       # Fetching integer after comma
       index = dataPoint.find(",");
       name = dataPoint.split(",")[0];
       integer = (dataPoint.split(",")[1]).strip();
      
       # Validating integer
       if not (integer.isdigit()):
           print('\n Comma not followed by an integer. \n');
           return False;  
       else:
           return True;

def main():
   """
       Main function
   """
  
   # List's to hold data
   strList = [];
   intList = [];
  
   # Reading title from user
   title = input('\n Enter a title for the data: ');
   print("\n You entered: " + title);
  
   # Reading header1 from user
   header1 = input('\n\n Enter the column 1 header: ');
   print("\n You entered: " + header1);
  
   # Reading header2 from user
   header2 = input('\n Enter the column 2 header: ');
   print("\n You entered: " + header2);
  
   # Reading dataPoints
   dataPoint = input("\n\n Enter a data point (-1 to stop input): ");
  
   # Reading data points
   while dataPoint != "-1":
       # Validating commas
       commas = chkCommas(dataPoint);
      
       # If there commas are OK
       if commas:
           # Splitting data point to name and integer
           name = dataPoint.split(",")[0];
           integer = int((dataPoint.split(",")[1]).strip());
          
           # Printing to console
           print("\n Data string: " + name);
           print("\n Data integer: " + str(integer));
          
           # Storing in list
           strList.append(name);
           intList.append(integer);
          
       # Reading dataPoints
       dataPoint = input("\n\n Enter a data point (-1 to stop input): ");
  
   # Printing result in tabular format
   outputTable(title, header1, header2, strList, intList);
  
   # Printing result in histogram
   outputHistogram(strList, intList);
  
# Calling main function  
main();
