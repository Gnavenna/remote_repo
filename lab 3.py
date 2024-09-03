 # req -1 :create repository
emp = {'ename':['hari','thomas','raj','laksh','subha'],'age':[21,23,22,35,20],'salary':[15000,18000,26000,30000,10000]}
print ("the employee dataset is:",emp)
print ("the employee salaries are:")
print (emp['salary'])
print("the salaries are:")
for v in emp['salary']:
    print(v)
L1=emp['salary']
print("The listed salaries:",L1)
print("The sorted salaries are:",sorted(L1))
print("The reversed salaries:",L1[::-1])
print("The minimum salary is:",min(L1))
print("The maximum salary is:",max(L1))
print("The total salary is:",sum(L1))