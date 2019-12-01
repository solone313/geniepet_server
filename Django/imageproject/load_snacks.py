import sys, os 
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imageproject.settings')

import django
django.setup()

from reco.models import Snack


def save_snack_from_row(snack_row):
    snack = Snack()
    snack.id = snack_row[0]
    snack.name = snack_row[1]
    snack.price = snack_row[2]
    snack.text = snack_row[3]
    snack.image = snack_row[4]
    snack.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:

        print ("Reading from file " + str(sys.argv[1]))
        snacks_df = pd.read_csv(sys.argv[1], encoding='CP949')
        print (snacks_df)

        snacks_df.apply(
            save_snack_from_row,
            axis=1
        )

        print ("There are {} Snacks".format(Snack.objects.count()))
        
    else:
        print ("Please, provide feed file path")
