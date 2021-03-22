import pandas as pd
import matplotlib.pyplot as plt
fronteras = pd.read_csv("fronteras.csv")
fronteras["Date"] = pd.to_datetime(fronteras["Date"])
dates = (fronteras["Date"] >= "01/01/2018 00:00:00") & (fronteras["Date"] <= "12/01/2018 00:00:00")
dates2 = (fronteras["Date"] >= "01/01/2019 00:00:00") & (fronteras["Date"] <= "12/01/2019 00:00:00")
front2018 = fronteras[dates]
front2019 = fronteras[dates2]

border = front2018["Border"] == "US-Mexico Border"
front2018 = front2018[border]
border = front2019["Border"] == "US-Mexico Border"
front2019 = front2019[border]

pasajeros = front2018["Measure"] == "Personal Vehicles"
front2018 = front2018[pasajeros]
pasajeros2 = front2019["Measure"] == "Personal Vehicles"
front2019 = front2019[pasajeros2]
estados = list(set(front2018["State"]))
for i in estados:
    suma1= front2018.groupby("State")[["Value"]].sum()
    suma2= front2019.groupby("State")[["Value"]].sum()
    df3 = pd.merge(suma1, suma2,on="State")
    df4 = pd.DataFrame(df3)
    print(df4)
    df5 = df4.rename(columns ={'Value_x':'2018', 'Value_y':'2019'},inplace=False)
    if df5.empty == False:
        grafica = df5[["2018", '2019']]
        grafica.plot(kind="line")
        plt.title(i)
        plt.show()
