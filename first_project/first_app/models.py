from django.db import models

class Usuario(models.Model):
    TiposUsuarios= (
    (-1, 'Banda/Artista'),
    (-2, 'Empresa'))    
    abstract=True
    nome = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    idTipoUsuario = models.IntegerField(choices=TiposUsuarios)

############ BANDA ####################################################################################

class BandaArtista(Usuario):
    numeroIntegrantes = models.IntegerField()
    cpfOuCnpj = models.CharField(max_length=14, unique=True)
    valorDataHora = models.DecimalField(max_digits=10, decimal_places=2)

class BandaArtistaGeneroDeApresentacao(models.Model):
    generosDeApresentacao= (
    (-1, 'Rock'),
    (-2, 'Sertanejo'),
    (-3, 'Pop'),
    (-4, 'Casamento'),
    (-5, 'Samba'),
    (-6, 'Pagode'))
    idBandaArtista = models.ForeignKey(BandaArtista, on_delete=models.CASCADE)
    idGeneroMusical = models.IntegerField(choices=generosDeApresentacao)

class Instrumento(models.Model):
    tipoInstrumento= (
    (-1, 'Corda'),
    (-2, 'Sopro'),
    (-3, 'Percussão'),
    (-4, 'Vocal'))
    nome = models.CharField(max_length=45, unique=True)
    idTipoInstrumento = models.IntegerField(choices=tipoInstrumento)

class BandaArtistaInstrumentos(models.Model):
    idBandaArtista = models.ForeignKey(BandaArtista, on_delete=models.CASCADE)
    idInstrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)

class BandaArtistaArquivo(models.Model):
    idBandaArtista = models.ForeignKey(BandaArtista, on_delete=models.CASCADE)
    pathArquivo = models.CharField(max_length=300, unique=True)

################################################################################################
############ EMPRESA ####################################################################################

class Empresa(Usuario):
    cnpj = models.CharField(max_length=14, unique=True)

class Evento(models.Model):
    status = (
    (-1, 'Encerrado'),
    (-2, 'Cancelado'),
    (-3, 'Agendado'),
    (-4, 'Em vigor'))
    porteEvento = (
    (-1, 'Grande'),
    (-2, 'Médio'),
    (-3, 'Pequeno'))
    idStatus = models.IntegerField(choices=status)
    idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    idPorteEvento = models.IntegerField(choices=porteEvento)
    duracao = models.DecimalField(max_digits=20, decimal_places=2)
    data = models.DateTimeField()
    nome = models.CharField(max_length=200, unique=True)
    local = models.CharField(max_length=200, unique=True)

################################################################################################
############ CONTRATO ####################################################################################

class Contrato(models.Model):
    status = (
    (-1, 'Encerrado'),
    (-2, 'Cancelado'),
    (-3, 'Aguandando aprovação'),
    (-4, 'Em vigor'))
    idStatus = models.IntegerField(choices=status)
    idEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    idBandaArtista = models.ForeignKey(BandaArtista, on_delete=models.CASCADE)
    valorTotal = models.DecimalField(max_digits=20, decimal_places=2)
    empresaAceitou = models.BooleanField()
    bandaArtistaAceitou = models.BooleanField()

################################################################################################
############ CUMPOM ####################################################################################

class ResultadoMineracao(models.Model):
    maiorTendencia =  models.IntegerField()
    menorTendencia =  models.IntegerField()
    valorDataHora = models.DateTimeField()

class Cupom(models.Model):
    tipoGeneroMusical= (
    (-1, 'Rock'),
    (-2, 'Sertanejo'),
    (-3, 'Pop'),
    (-4, 'Samba'),
    (-5, 'Pagode'),
    (-6, 'Funk'))
    porcentagem =  models.IntegerField()
    generoMusical = models.IntegerField(choices=tipoGeneroMusical)
    valorDataHora = models.DateTimeField()

################################################################################################