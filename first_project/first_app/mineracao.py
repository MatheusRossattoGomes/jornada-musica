
from nltk.tokenize import word_tokenize
from nltk import PorterStemmer
import first_app.mineracaoConections as conections
from first_app.generosMusicaisEnum import generosMusicais
#nltk.download()
import tweepy

# Step 1 - Authenticate
def coletarDadosTweets():
    consumer_key= conections.consumer_key
    consumer_secret= conections.consumer_secret
    access_token= conections.access_token 
    access_token_secret= conections.access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    public_tweets = api.search_tweets('musica', lang="pt", count=99, include_entities=False)
    lista_tweets =[]
    for tweet in public_tweets:
        lista_tweets.append(tweet.text)

    ResultadosSertanejo = 0
    ResultadosRock = 0
    ResultadosSamba = 0
    ResultadosPagode = 0
    ResultadosFunk = 0

    for tweet in lista_tweets:
        tokenTweet = word_tokenize(tweet)
        ps = PorterStemmer()
        tweetFormaLexica = []

        for w in tokenTweet:
            tweetFormaLexica.append(ps.stem(w))
        
        qtdSertanejo = tweetFormaLexica.count(ps.stem("sertanejo"))
        qtdRock = tweetFormaLexica.count(ps.stem("rock"))
        qtdSamba = tweetFormaLexica.count(ps.stem("samba"))
        qtdPagode = tweetFormaLexica.count(ps.stem("pagode"))
        qtdFunk = tweetFormaLexica.count(ps.stem("funk"))

        listaGenero = [qtdSertanejo, qtdRock, qtdSamba, qtdPagode, qtdFunk]
        generoMaisFalado = max(listaGenero)

        if(generoMaisFalado > 0):
            tipo = None
            
            if(qtdSertanejo == generoMaisFalado):
                ResultadosSertanejo += 1
            elif(qtdRock == generoMaisFalado):
                ResultadosRock += 1
            elif(qtdSamba == generoMaisFalado):
                ResultadosSamba += 1
            elif(qtdPagode == generoMaisFalado):
                ResultadosPagode += 1
            elif(qtdFunk == generoMaisFalado):
                ResultadosFunk += 1

    resultadosFinais = [ResultadosSertanejo, ResultadosRock, ResultadosSamba, ResultadosPagode, ResultadosFunk]
    maiorResultado = max(resultadosFinais)
    menorResultado = min (resultadosFinais)
    maiorTentencia = max(resultadosFinais)
    menorTendencia = min (resultadosFinais)
    
    if(maiorResultado == ResultadosSertanejo):
                maiorTentencia = generosMusicais.Sertanejo
    elif(maiorResultado == ResultadosRock):
                maiorTentencia = generosMusicais.Rock
    elif(maiorResultado == ResultadosSamba):
                maiorTentencia = generosMusicais.Samba
    elif(maiorResultado == ResultadosPagode):
                maiorTentencia = generosMusicais.Pagode
    elif(maiorResultado == ResultadosFunk):
                maiorTentencia = generosMusicais.Funk
                
    if(menorResultado == ResultadosSertanejo):
                menorTendencia = generosMusicais.Sertanejo
    elif(menorResultado == ResultadosRock):
                menorTendencia = generosMusicais.Rock
    elif(menorResultado == ResultadosSamba):
                menorTendencia = generosMusicais.Samba
    elif(menorResultado == ResultadosPagode):
                menorTendencia = generosMusicais.Pagode
    elif(menorResultado == ResultadosFunk):
                menorTendencia = generosMusicais.Funk

    return [maiorTentencia, menorTendencia]