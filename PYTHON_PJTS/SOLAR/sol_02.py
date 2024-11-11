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
    season_factor = 1 - 0.3 * np.cos((day_of_year - 173) * 2 * np.pi / 365)
    day_factor = max(0, np.sin((hour - 6) * np.pi / 12))
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

# Grafico e formattazione dinamica
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(data.index, data['Consumption'], label='Consumo (kW)')
ax.plot(data.index, data['SolarProduction'], label='Produzione Solare (kW)')
ax.plot(data.index, data['Battery'], label='Energia Stoccata (kWh)')
ax.plot(data.index, data['GridExport'], label='Energia Rivenduta (kW)')

# Formatter e locator dinamico
date_format = DateFormatter('%Y-%m-%d %H:%M')
ax.xaxis.set_major_formatter(date_format)
ax.xaxis.set_major_locator(AutoDateLocator())

# Funzione per aggiornare il formato dell'asse X durante lo zoom
def on_zoom(event):
    scale = ax.get_xlim()[1] - ax.get_xlim()[0]
    if scale < 1/24:  # Se è inferiore a un giorno, mostra ore e minuti
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
    elif scale < 7:  # Se è inferiore a una settimana, mostra giorno e ora
        ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M'))
    else:  # Oltre una settimana, mostra solo giorno
        ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.canvas.draw_idle()

# Collegamento dell'evento di zoom
fig.canvas.mpl_connect('button_release_event', on_zoom)

# Configurazioni finali del grafico
ax.set_title('Simulazione dei Consumi e della Produzione Solare con Zoom Dettagliato')
ax.set_xlabel('Data')
ax.set_ylabel('Energia (kW/kWh)')
ax.legend()
plt.show()

