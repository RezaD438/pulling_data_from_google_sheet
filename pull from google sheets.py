import pandas as pd
import codecs

# making the yurl for your public google sheet file
# id of the google sheet file ( after /d/ and before next / is the id part of the URL )
sheet_id = "1U6BOBZUP3cJw876JHLtwIuDgt2pKcrI7-puH9vRExHs"
# the sheet name
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Read the data from the .xlsx file into a DataFrame.
df = pd.read_csv(url)

# Open a file for writing the data in persian
i = 0
with codecs.open('output.txt', 'w', "utf-8") as f:
    f.write('عدد منفی به معنای میزان پرداخت شما به بورد گیم و عدد مثبت به معنای پرداخت بورد گیم به شما است \n')
    f.write('ه=====================================\n')

    f.write('\n\n')

    # Iterate over the columns of the DataFrame.
    for col_name, col_data in df.items():
        # Get the first and second values from the current column.
        i = i + 1
        if i % 2 == 1:
            # Write the values to the file.
            value1 = col_name
            value2 = col_data.iloc[0]
            f.write(f"{value1} : {value2}\n\n=====================================\n\n")
            # print(f"{value1} : {value2}\n\n=====================================\n\n")

    f.write('\nروز خوش')

