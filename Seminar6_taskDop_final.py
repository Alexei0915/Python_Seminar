# user = ["user1","user2","user3","user4","user5"]
# ids= [4,5,9,14,7]
# salary=[111,222,333]

# res=list(zip(user,ids,salary))
# print(res,"\n")

# new_users = [i[0] for i in res]
# new_ids = [i[1] for i in res]
# new_salary = [i[2] for i in res]
# print(new_users,"\n",new_ids,"\n", new_salary,"\n")


user = ["user1","user2","user3","user4","user5"]
ids= [4,5,9,14,7]
salary=[111,222,333]
a,b,c = map(list,zip(user,ids,salary))
print(a,b,c,sep="\n")
a,b,c = map(list,zip(a,b,c))

print(a,b,c, sep="\n")