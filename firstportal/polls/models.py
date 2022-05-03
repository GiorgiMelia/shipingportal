from locale import currency
import mailbox
from django.db import models
from django.contrib.auth.models import User

 

class stock(models.Model):    
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class account(models.Model) :
    currency = models.CharField(max_length=3)
    balance=models.DecimalField
    user =  models.ForeignKey(User, on_delete=models.CASCADE )
    #transfer_history = transfer_history(user_id)




'''
#iuseri
# eqaunti
#amanatis gadatanis istoria
class traffing_history(models.model) :
        def __init__(self):
            self.user_id

#gadaricxvis istoria
class transfer_history(user_id=0) :
    def __init__(self):
        self.user_id = user_id
        self.transfer_id
        self.cut
        self.before_cut
        self.after_cut

 



class account(models.Model) :
    currency
    balance
    user_id = user.id
    transfer_history = transfer_history(user_id)


#sawyobi
class warehouse(models.Model) :
    adress 

#amanati
class parcel(models.Model) :
    id
    traffing_history = traffing_history(id)
'''
