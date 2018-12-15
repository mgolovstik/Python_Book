import pickle
aaaaaaaaa = {'Еда','Сон','Родители','И т.д.'}
diavol = open('save.dat','wb')
pickle.dump(aaaaaaaaa, diavol)
diavol.close()
pop = open('save.dat','rb')
did = pickle.load(pop)
print(did)
