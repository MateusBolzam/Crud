from django.db import models

# Create your models here.


Status = (
    ("FORÇA", "Força"),
    ("DESTREZA", "Destreza"),
    ("CONSTITUIÇÃO", "Constituição"),
    ("CARISMA", "Carisma"),
    ("INTELIGÊNCIA", "Inteligência"),
    ("SABEDORIA", "Sabedoria")
)

class classe(models.Model):
    
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=128,
                                choices=Status,
                                default="Força")
    intStatus = models.IntegerField() 
    
    def __str__(self):
        return str(self.name)
    

class personagem(models.Model):
    
    name = models.CharField(max_length=255)
    classes = models.ForeignKey(classe, on_delete=models.CASCADE)


