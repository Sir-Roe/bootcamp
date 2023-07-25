def cakes(recipe, available):
    my_l =[]
    for key in recipe.keys():
        if key not in available.keys():
            return 0
    
    for key in recipe.keys():    
        for ikey in available.keys():
            print(ikey + ' vs ' + key)
            if ikey.lower() == key.lower():
                my_l.append(available[ikey] // recipe[key])
            print(my_l)
    return min(my_l)
 
  


recipes =  {'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
availables = {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}
print(cakes(recipes,availables))
#test.assert_equals(cakes(recipe, available), 2, 'example #1')
#Wrong result for recipe {'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100} and available ingredients {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}: 25 should equal 11
    