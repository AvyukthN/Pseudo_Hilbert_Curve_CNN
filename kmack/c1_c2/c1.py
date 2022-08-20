from re import A
from tkinter import W
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('./gpdata.csv')
    # print(df.columns)

    # APPS BY CATEGORY
    print(df.value_counts(subset=["Category"]))
    # print(f"{get_cats(df)} Apps by Category")

    # APPS BY AGE RANGE
    print()
    print(df.value_counts(subset=["Rating"]))

    # APPS BY SIZE
    # s1 = get_size(df)
    # y = [ str(_[0]) + str(_[2]) for _ in s1]

    # size_hash = {}
    # set_y = list(set(y))
    # for inst in set_y:
    #     count = count_occ(y, inst)

    #     size_hash.update({inst: count})

    print(df.value_counts(subset=["Size"]))

    # APPS BY TYPE
    ct = get_paid(df)

    print()
    print(f"{len(df['Type']) - ct} Free Apps")
    print(f"{ct} Paid Apps")

    # APPS BY CATEGORY + PRICE RANGES
    print()
    print(df.value_counts(subset=["Category", "Price"]))

    # APPS BY CATEGORY + TYPE
    # catypes = get_catype(df)

    # print()
    # print(catypes)

    print()
    print(df.value_counts(subset=["Category", "Type"]))

"""
def count_occ(arr: list, instance: str) -> int:
    count = 0

    for _ in arr:
        if _ == instance:
            count += 1

    return count

def get_cats(df: pd.DataFrame) -> str:
    cats = df['Category']
    cats = set(list(cats))
    # print(cats)

    return len(list(cats))

def get_catype(df: pd.DataFrame) -> str:
    catypes = []

    cats = df['Category']
    types = df['Type']

    for i in range(len(cats)):
        cat = cats[i]
        type = types[i]

        if count_occ(catypes, (cat, type)) == 0:
            catypes.append((cat, type))
    
    return catypes

def get_age(df: pd.DataFrame) -> str: 
    age = df['Current Ver']

def get_size(df: pd.DataFrame) -> str: 
    sizes = df['Size']

    y = []
    varies = []

    for i in range(len(sizes)):
        s = sizes[i]
        if s == 'Varies with device':
            varies.append(('varies', i))
        else:
            for j in range(len(s)):
                if s[j] == '.' or s[j].isnumeric():
                    continue
                else:
                    y.append((s[:j], i, s[j]))
                    break
    
    return y

def get_paid(df: pd.DataFrame) -> int:
    type = df['Type']

    count = 0
    for _ in type:
        if _ == "Paid":
            count += 1

    return count
"""