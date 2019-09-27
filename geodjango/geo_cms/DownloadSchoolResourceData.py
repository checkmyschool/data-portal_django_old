import pandas as pd
from geo_cms.models import cms2017


def DownloadData(columns):

    ## Prefered Method however the raw raw query returns a weird type 
    ## of query set not compatible with rendering the downloadable CSV ##
    # length = len(columns) - 2
    # print(length)
    # counter = 0
    # string = 'SELECT school_nam, '
    # for i in columns:
    #     string += columns[counter]
    #     string += ', '
    #     counter += 1
    # string += columns[len(columns) - 1]
    # string += ' FROM cms2017'
    # print(string)
    # qs = cms2017.objects.raw(string)[0:20]

    ## Pandas Method ##
    df = pd.DataFrame(list(cms2017.objects.all()))
    print(df)
    print("DF COLUMNS: ", df.columns)
    print("CHOSEN COLUMNS: ", columns)

    df = df[columns]

    return df