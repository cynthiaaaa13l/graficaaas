import pandas as pd
import matplotlib.pyplot as plt
fronteras = pd.read_csv('fronteras.csv')
fronteras['Date'] = pd.to_datetime(fronteras['Date'])
datos = (fronteras['Date'] >= '01/01/2018 00:00:00') & (fronteras['Date'] <= '12/01/2018 00:00:00')
datos1 = (fronteras['Date'] >= '01/01/2019 00:00:00') & (fronteras['Date'] <= '12/01/2019 00:00:00')
front2018 = fronteras[datos]
front2019 = fronteras[datos1]
border = front2018["Border"] == "US-Mexico Border"
front2018 = front2018[border]
border = front2019["Border"] == "US-Mexico Border"
front2019 = front2019[border]
val1 = front2018["Measure"] == "Pedestrians"
val2 = front2019["Measure"] == "Pedestrians"
front2018 = front2018[val1]
front2019 = front2019[val2]
estados = list(set(front2018["State"]))
for i in estados:
    df1 = front2018["State"] == i
    df1 = front2018[df1]
    x = df1["Port Name"]
    y = df1["Value"]
    titulo = i + " 2018"
    plt.title(titulo)
    plt.scatter(x, y)
    plt.show()
for i in estados:
    df1 = front2019["State"] == i
    df1 = front2019[df1]
    titulo = i + " 2019"
    x = df1["Port Name"]
    y = df1["Value"]
    plt.title(titulo)
    plt.scatter(x, y)
    plt.show()