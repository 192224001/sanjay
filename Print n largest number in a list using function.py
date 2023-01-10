def N_max_elements(list, N):
    result_list = []
  
    for i in range(0, N): 
        maximum = 0
          
        for j in range(len(list)):     
            if list[j] > maximum:
                maximum = list[j]
                  
        list.remove(maximum)
        result_list.append(maximum)
          
    return result_list
  

list1 = [4, 8, 12, 15, 20, 29, 45, 32]
N=1
print(N, "max elements in ",list1)
print(N_max_elements(list1,N))
