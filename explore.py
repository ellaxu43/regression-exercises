def plot_variable_pairs(df: pd.core.frame.DataFrame):

    

    sns.pairplot(train, corner = True, kind = 'reg')
    plt.show()


def months_to_years():

    train['tenure_years'] = round(train['tenure'] / 12).astype('int')
    return train

def plot_cate_cont_vars(train, cat_cols, con_cols):

    for con in con_cols:
        for cat in cat_cols:
            fig = plt.figure(figsize = (14, 4))
            fig.suptitle(f'{con} v. {cat}')

            plt.subplot(1, 3, 1)
            sns.boxplot(data = df, x = cat, y = con)
            plt.axhline(df[con].mean())

            plt.subplot(1, 3, 2)
            sns.barplot(data = df, x = cat, y = con)
            plt.axhline(df[con].mean())

            plt.subplot(1, 3, 3)
            sns.histplot(data = df, x = con, bins = 10, hue = cat)
            plt.show()
