# Load data into separate dataframes.
import pandas as pd


def load_dataframes():
    """

    :rtype: object
    """
    df1 = pd.DataFrame({'date': date_1,
                        'ndvi': ndvi_1,  # raw ndvi
                        'ndvic': ndvic_1,  # corrected ndvi
                        'gndvi': gndvi_1,  # gndvi (green ndvi)
                        'ndre': ndre_1,  # ndre (normative difference red-edge)
                        'psps': psps,  # lbs sugar per section
                        'treatment': treatment  # treatment type
                        })
    df2 = pd.DataFrame({'date': date_2,
                        'ndvi': ndvi_2,
                        'ndvic': ndvic_2,
                        'gndvi': gndvi_2,
                        'ndre': ndre_2,
                        'psps': psps,
                        'treatment': treatment
                        })
    df3 = pd.DataFrame({'date': date_3,
                        'ndvi': ndvi_3,
                        'ndvic': ndvic_3,
                        'gndvi': gndvi_3,
                        'ndre': ndre_3,
                        'psps': psps,
                        'treatment': treatment
                        })
    df4 = pd.DataFrame({'date': date_4,
                        'ndvi': ndvi_4,
                        'ndvic': ndvic_4,
                        'gndvi': gndvi_4,
                        'ndre': ndre_4,
                        'psps': psps,
                        'treatment': treatment
                        })
    df5 = pd.DataFrame({'date': date_5,
                        'ndvi': ndvi_5,
                        'ndvic': ndvic_5,
                        'gndvi': gndvi_5,
                        'ndre': ndre_5,
                        'psps': psps,
                        'treatment': treatment
                        })
    df6 = pd.DataFrame({'date': date_6,
                        'ndvi': ndvi_6,
                        'ndvic': ndvic_6,
                        'gndvi': gndvi_6,
                        'ndre': ndre_6,
                        'psps': psps,
                        'treatment': treatment
                        })

    return [df1, df2, df3, df4, df5, df6]


load_dataframes()
