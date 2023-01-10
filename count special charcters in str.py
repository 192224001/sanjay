

def count_special_character(string): 
  

    special_char= 0
   
    for i in range(0, len(string)):  
    
      
        ch = string[i]
  
        

        if (string[i].isalpha()):  
            continue
        
        
        elif (string[i].isdigit()):
            continue
            
        else: 
            special_char += 1
            
            
    if special_char >= 1:    
        print("String contains {} Special Character/s ".format(special_char))  
    else:
        print("There are no Special Characters in this String.")
  

if __name__ == '__main__' : 
    string = "Code%^&*$Speedy"
    count_special_character(string)
