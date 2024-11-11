import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.dates import DateFormatter, AutoDateLocator

# Impostazioni base
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)
time_delta = timedelta(minutes=10)
battery_capacity = 500  # kWh, capacità massima della batteria
solar_peak = 15  # kW, picco dell'impianto solare
battery_charge = 0  # kWh, energia iniziale nella batteria

# Creazione del DataFrame temporale
time_index = pd.date_range(start=start_date, end=end_date, freq='10T')
data = pd.DataFrame(index=time_index)

# Funzioni per simulare consumo e produzione
def simulate_household_consumption(hour):
    base_load = 0.2  # kW, consumo base minimo
    fridge = 0.1 if hour in range(0, 24) else 0  # Il frigorifero è costante
    lights = 0.5 if hour in range(18, 23) else 0.1  # Luci attive di sera
    oven = 1.5 if hour in range(12, 14) or hour in range(18, 20) else 0  # Forno a pranzo/cena
    boiler = 1 if hour in range(6, 8) or hour in range(18, 20) else 0  # Boiler per docce
    heat_pump = 2 if hour in range(6, 9) or hour in range(17, 22) else 0  # Termopompa per riscaldamento serale
    small_devices = 0.1 * np.random.poisson(3)  # Piccoli utilizzatori variabili
    return base_load + fridge + lights + oven + boiler + heat_pump + small_devices

def simulate_solar_production(day_of_year, hour):
    # Impostiamo il picco di produzione solare intorno al giorno 173 (solstizio d'estate)
    season_factor = 1 - 0.3 * np.cos((day_of_year - 173) * 2 * np.pi / 365)
    day_factor = max(0, np.sin((hour - 6) * np.pi / 12))  # Picco a mezzogiorno
    return solar_peak * season_factor * day_factor

data['Consumption'] = [simulate_household_consumption(ts.hour) for ts in data.index]
data['SolarProduction'] = [simulate_solar_production(ts.day_of_year, ts.hour) for ts in data.index]

# Gestione energia in batteria
data['Battery'] = 0.0
data['GridExport'] = 0.0

for i in range(len(data)):
    produced = data['SolarProduction'].iloc[i]
    consumed = data['Consumption'].iloc[i]
    net_energy = produced - consumed

    # Aggiornamento batteria
    if net_energy > 0:
        if battery_charge + net_energy <= battery_capacity:
            battery_charge += net_energy
            data['Battery'].iloc[i] = battery_charge
        else:
            data['Battery'].iloc[i] = battery_capacity
            data['GridExport'].iloc[i] = battery_charge + net_energy - battery_capacity
    else:
        if battery_charge + net_energy >= 0:
            battery_charge += net_energy
            data['Battery'].iloc[i] = battery_charge
        else:
            data['Battery'].iloc[i] = 0

# Creazione dei grafici
fig, axs = plt.subplots(4, 1, figsize=(12, 10), sharex=True)
fig.suptitle('Simulazione Consumi, Produzione Solare, Energia in Batteria e Energia Rivenduta')

# Consumi
axs[0].plot(data.index, data['Consumption'], color='blue')
axs[0].set_ylabel('Consumo (kW)')
axs[0].set_title('Consumo Energetico')

# Produzione solare
axs[1].plot(data.index, data['SolarProduction'], color='orange')
axs[1].set_ylabel('Produzione (kW)')
axs[1].set_title('Produzione Solare')

# Energia in batteria
axs[2].plot(data.index, data['Battery'], color='green')
axs[2].set_ylabel('Batteria (kWh)')
axs[2].set_title('Energia Stoccata in Batteria')

# Energia rivenduta
axs[3].plot(data.index, data['GridExport'], color='red')
axs[3].set_ylabel('Rivenduta (kW)')
axs[3].set_title('Energia Rivenduta alla Rete')

# Formattazione dell'asse X per zoom dinamico
locator = AutoDateLocator()
formatter = DateFormatter('%Y-%m-%d %H:%M')
for ax in axs:
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

plt.xticks(rotation=45)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Per lasciare spazio al titolo principale
plt.show()
