def get_param():
    param = {'legend.fontsize' : 'Large',
              'figure.figsize'  : figsize,
              'axes.labelsize'  : 'x-large',
              'axes.titlesize'  : 'xx-large',
              'xtick.labelsize' : 'Large',
              'ytick.labelsize' : 'Large'}
    return param

def count_plt(x, y, df=movies, figsize=(18, 6)):
    # sns.set(style="ticks")
    sns.set(style="whitegrid")

    param = {'legend.fontsize': 'large',
              'figure.figsize' : figsize,
              'axes.labelsize' : 'x-large',
              'axes.titlesize' : 'xx-large',
              'xtick.labelsize': 'large',
              'ytick.labelsize': 'large'}
    plt.rcParams.update(param)


    ax = sns.countplot(x=x, y=y, data=df)
    if y: plt.title(y)
    else: plt.title(x)
    plt.xticks(rotation=90)

    plt.show()