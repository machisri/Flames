from collections import Counter
  
   
def common(str1,str2): 
      
    # convert both strings into counter dictionary 
    dict1 = Counter(str1) 
    dict2 = Counter(str2)
    
  
    # take intersection of these dictionaries 
    commonDict = dict1 & dict2 
  
    if len(commonDict) == 0: 
        print (-1)
        return
  
    # get a list of common elements 
    commonChars = list(commonDict.elements()) 
  
    # sort list in ascending order to print resultant 
    # string on alphabetical order 
    commonChars = sorted(commonChars) 
  
    # join characters without space to produce 
    # resultant string 
    result = ''.join(commonChars);
    x = len(str1)+len(str2);
    y = len(result)*2;
    z = x-y;
    
    if z == 19:
      print("Lover")
    elif z == 10:
      print("Lover") 
    elif z == 29:
      print("Sister")
    elif z== 27:
      print("Sister")
    elif z== 1:
      print("Sister")
    elif z== 6:
      print("Marriage")
    elif z== 11:
      print("Marriage")
    elif z== 15:
      print("Marriage")
    elif z== 26:
      print("Marriage") 
    elif z== 3:
      print("Friend")
    elif z== 5:
      print("Friend")
    elif z== 14:
      print("Friend")
    elif z== 18:
      print("Friend")
    elif z== 21:
      print("Friend")
    elif z== 23:
      print("Friend") 
    elif z== 8:
      print("Affection")
    elif z== 12:
      print("Affection")
    elif z== 13:
      print("Affection")  
    elif z== 17:
      print("Affection")
    elif z== 28:
      print("Affection")
    elif z== 30:
      print("Affection")
    elif z== 4:
      print("Enemy")
    elif z== 7:
      print("Enemy") 
    elif z== 9:
      print("Enemy")
    elif z== 20:
      print("Enemy")
    elif z== 22:
      print("Enemy")
    elif z== 24:
      print("Enemy")
    elif z== 25:
      print("Enemy")
    elif z== 2:
      print("Enemy")  
# Driver program 
if __name__ == "__main__": 
    str1 = input("Enter Your Name: ");
    str2 = input("Enter Your Lovedone Name: ");
   

  
  
    common(str1, str2) 
