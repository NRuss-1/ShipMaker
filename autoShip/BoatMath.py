import Composition
from functools import lru_cache
from Instance import InstanceData

    
def getMaxCP(num_people):  
    cp = 40 * (num_people/15)  
    return cp  

def deepcopy(choice):  
    ret_value = []  
    for ch in choice:  
        ret_value.append(ch)  
    return ret_value  


def combsUtil(choice, arr, index, r, start, end, people):  
    instanceData = InstanceData.getInstance() 
    if index == r:  
        copy = deepcopy(choice)  
        comp = Composition.Composition(copy, instanceData)  
        if comp.validate(getMaxCP(people), people):  
            instanceData.comb_append(comp)  
        return   
    
    if start > end:  
        return   
    
    choice[index] = arr[start]  
    
    combsUtil(choice, arr, index+1, r, start, end, people)  
    combsUtil(choice, arr, index, r, start+1, end, people)  

def combs(arr, n, r, people):  
    choice = [0] * r  
    combsUtil(choice, arr, 0, r, 0, n-1, people)        

def sortKey(e):    
    return e.getRelativePower()    

def setPageMax(arr):      
    if (len(arr) <= 30):        
        return len(arr) - 1    
    else:        
        return 30    

def formatComps():    
    total = []    
    total.append(["#", "Ship", "Ship", "Ship", "Ship", "Ship", "HP", "CP", "Manning"])        
    instanceData = InstanceData.getInstance()  
    combs = instanceData.all_combs    
    combs.sort(key = sortKey, reverse = True)    
    for i in range(instanceData.page, instanceData.page + setPageMax(combs)):        
        temp = [0,"","","","","",0,0,0]        
        temp[0] = i        
        names = combs[i].getNames()          
        for j in range(len(names)):            
            temp[j+1] = names[j]        
        temp[6] = combs[i].getHP()        
        temp[7] = combs[i].getCP()        
        temp[8] = combs[i].getManning()        
        total.append(temp)    
    return total    

def adjustCompRange(num):    
    ran = 5    
    if num > 25:        
        ran = 6    
    return ran    

def createCompositions():  
    instanceData = InstanceData.getInstance()       
    boats = instanceData.ships
    num_people = instanceData.num_people    
    upper_range = adjustCompRange(num_people)    
    
    instanceData.initCombArr() 
    instanceData.setNumPeople(num_people) 
    instanceData.getMaxCP()
    
    for i in range(2, upper_range):        
        combs(boats, len(boats), i, num_people)  
 
    instanceData.initPage()
