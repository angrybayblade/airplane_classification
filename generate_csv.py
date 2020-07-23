import numpy as np
import pandas as pd

from glob import glob
from tqdm.cli import tqdm

train_dir = glob("./train/*/*.jpg")
val_dir = glob("./val/*/*.jpg")

families = open("./families.txt","r").read().split("\n")[:-1]
variants = open("./variants.txt","r").read().split("\n")[:-1]

train_fam = pd.DataFrame([
    [i.split(" ")[0]," ".join(i.split(" ")[1:])]
    for 
        i
    in 
        open("./images_family_train.txt","r").read().split("\n")[:-1]
],columns=['id','family'])

train_var = pd.DataFrame([
    [i.split(" ")[0]," ".join(i.split(" ")[1:])]
    for 
        i
    in 
        open("./images_variant_train.txt","r").read().split("\n")[:-1]
],columns=['id','variant'])


family_var_mapping = train_fam.merge(train_var)
mappings = family_var_mapping.groupby('variant')



train = [[int(i.split("/")[2]),i] for i in train_dir]
train = [[variants[i-1],j] for i,j in train]
train = pd.DataFrame(train,columns=['variant','image'])

train['family'] = train.variant.apply(lambda x:mappings.get_group(x).family.values[0])

val = [[int(i.split("/")[2]),i] for i in val_dir]
val = [[variants[i-1],j] for i,j in val]
val = pd.DataFrame(val,columns=['variant','image'])

val['family'] = val.variant.apply(lambda x:mappings.get_group(x).family.values[0])

train.to_csv("./train.csv",index=False)
val.to_csv("./validation.csv",index=False)