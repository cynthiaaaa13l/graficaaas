import pandas as pd
import matplotlib.pyplot as plt
fronteras = pd.read_csv("fronteras.csv")
fronteras["Date"] = pd.to_datetime(fronteras["Date"])
fechas = (fronteras["Date"] >= "01/01/2018 00:00:00") & (fronteras["Date"] <= "12/01/2019 00:00:00")
fronteras = fronteras[fechas]
tipo_bus = fronteras["Measure"] == "Bus Passengers"
fronteras = fronteras[tipo_bus]
border = fronteras["Border"] == "US-Mexico Border"
fronteras = fronteras[border]
estados = list(set(fronteras["State"]))
for i in estados:
    is_estado = fronteras["State"] == i
    df1 = fronteras[is_estado]
    df1["Value"].plot(kind="hist", title = i, color="red")
plt.show()
