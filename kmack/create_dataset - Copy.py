import pandas as pd

rev_df = pd.read_csv('./data/reviews.csv', encoding='utf8').dropna()
gp_df = pd.read_csv('./data/gpdata.csv', encoding='utf8')

app_name_ml = list(rev_df['App'])
app_name_dt = list(gp_df['App'])
ratings = list(gp_df["Rating"])

rating_hash = {}
for i in range(len(app_name_dt)):
    rating_hash.update({app_name_dt[i]: ratings[i]})

ratings = []
for i in range(len(app_name_ml)):
    try:
        ratings.append(rating_hash[app_name_ml[i]])
    except:
        ratings.append(None)
        # print(rating_hash[app_name_ml[i]])

df = pd.DataFrame({
    '1': pd.Series(app_name_ml),
    '2': pd.Series(ratings)
})


print(len(df['2']))

rev_df['Rating'] = ratings

rev_df.to_csv('./model_data.csv', index=False)