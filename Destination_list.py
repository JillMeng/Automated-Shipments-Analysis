def destination_region():

    desto_fil = input('What are the destination province you would like to filter? (0 for Exit)\n').upper()
    desto_pro = ["AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FM", "FL", "GA", "GU", "HI",
             "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MH", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
             "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH", "OK", "OR", "PW", "PA", "PR", "RI",
             "SC", "SD", "TN", "TX", "UT", "VT", "VI", "VA", "WA", "WV", "WI", "WY", "AE", "AA", "AE", "AE",
             "AE", "AP", "AB", "BC", "MB", "NB", "NF", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT", ]
    desto_lst = []
    while desto_fil != '0':
        if desto_fil in desto_pro:
            desto_lst += [desto_fil]
        else:
            print('Invalid input! ')
        desto_fil = input('What are the destination province you would like to filter? (0 for Exit)\n').upper()

    return desto_lst