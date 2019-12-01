import sys, os 
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imageproject.settings')

import django
django.setup()

from reco.models import Shampoo


def save_Shampoo_from_row(shampoo_row):
    shampoo = Shampoo()
    shampoo.id = shampoo_row[0]
    shampoo.name = shampoo_row[1]
    shampoo.price = shampoo_row[2]
    shampoo.text = shampoo_row[3]
    shampoo.image = shampoo_row[4]
    shampoo.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:

        print ("Reading from file " + str(sys.argv[1]))
        shampoos_df = pd.read_csv(sys.argv[1], encoding='CP949')
        print (shampoos_df)

        shampoos_df.apply(
            save_Shampoo_from_row,
            axis=1
        )

        print ("There are {} Shampoos".format(Shampoo.objects.count()))
        
    else:
        print ("Please, provide feed file path")
