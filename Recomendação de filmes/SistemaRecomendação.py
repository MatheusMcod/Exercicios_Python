def getMoviesOp():
    mov = 1
    movies = []
    while mov <= 10:
        operatorMovie = input('Digite um filme: ')
        if(operatorMovie in movies):
            print('Esse filme ja está na lista! Tente novament.')
        else:
            movies.append(operatorMovie)
            mov = mov + 1
        
    return movies    
    
def addMoviesUser(quant, movies):
    moviesUser = []
    cont = 0
    while cont < quant:
        selector = input('Filme: ')
        if selector in movies:
            moviesUser.append(selector) 
            cont = cont + 1       
        else:
            print('Filme invalido! Tente novamente')
    
    return moviesUser
        
def compareList(list1,list2):
    moviesRecommendation = list2.copy()
    for i in list2:
        if i in list1:
            moviesRecommendation.remove(i)
            
    return moviesRecommendation
            
moviesUser1 = []
moviesUser2 = []  
print('----------------Operador----------------')
moviesOperator = getMoviesOp()
for i in range(2):
    print('----------------User{}----------------' .format(i+1))
    print('Quantos desses filmes você ja assistiu')
    for c in moviesOperator:
        print(c, end='   ')
    cont = 0
    while cont < 1:
        movieNumber = int(input('\nQuantidade?: '))
        if (movieNumber >= 0 and movieNumber <= 10):
            cont = cont + 1
    print('E Quais desses filmes você ja assistiu')
    print('Digite o Nome')
    if(i == 0):
        moviesUser1 = addMoviesUser(movieNumber, moviesOperator)
    else:
        moviesUser2 = addMoviesUser(movieNumber, moviesOperator)
                
Recommendation = compareList(moviesUser1,moviesUser2)
print('----------------User1----------------')
if(Recommendation == []):
    print("Sinto muito! não temos filmes para recomendar.")
else:
    print('Recomendamos esses filmes para você')
    for i in Recommendation:
        print(i, end='   ')

Recommendation = compareList(moviesUser2,moviesUser1)                            
print('\n----------------User2----------------')
if(Recommendation == []):
    print("Sinto muito! não temos filmes para recomendar.")
else:
    print('Recomendamos esses filmes para você')
    for i in Recommendation:
        print(i, end='   ')

