
expense = [ 2200, 2350, 2600, 2130, 2190 ]
print( expense[1] - expense[0] )
print( expense[0] + expense[1] + expense[2] )

print( 2000 in expense )

expense.append(1980) 
expense[3] = expense[3] - 200

#excesise 2
heros=['spider man','thor','hulk','iron man','captain america']
print( len(heros) )
heros.append('black panther')
heros.pop(5)
heros.insert( 3, 'black panther' )
heros[1:3] = ['docter strange']
heros.sort()
print( heros ) 

#excesise 3

limit = int( input( 'Enter max: ') )
# arr=[]
# for i in range(limit):
#     if i % 2 != 0:
#         arr.append(i) 

# another method for above code
arr=[ x for x in range(limit) if x%2 != 0 ]

print(arr)

#---
txt = f'hello {10}'
print(txt)



