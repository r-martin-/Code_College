__author__ = 'mark'

import httplib2

def return_web_csv(url, delimiter=",", encoding="utf-8"):

    row_list = []

    try:
        # get data file, open it and split on delimiter,

        h = httplib2.Http(".cache")
        headers, fh = h.request(url)
        fh = fh.decode(encoding).split("\n")

        for row in fh:
            try:
                row = row.strip()
                row = row.split(delimiter)

            except ValueError as e:
                print(e +": "+ row)
                continue
            except TypeError as e:
                print(e +": "+ row)
                continue
            except IndexError as e:
                print(e +": "+ row)
                continue

            row_list.append(row)

    except httplib2.HttpLib2Error as e:
        print(e)

    return row_list