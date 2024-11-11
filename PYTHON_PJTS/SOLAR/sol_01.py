import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

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
    """Simula il consumo medio orario in kW per i vari dispositivi"""
    # Consumo in kW di ciascun dispositivo in base all'ora
    base_load = 0.2  # kW, consumo base minimo
    fridge = 0.1 if hour in range(0, 24) else 0  # Il frigorifero è costante
    lights = 0.5 if hour in range(18, 23) else 0.1  # Luci attive di sera
    oven = 1.5 if hour in range(12, 14) or hour in range(18, 20) else 0  # Forno a pranzo/cena
    boiler = 1 if hour in range(6, 8) or hour in range(18, 20) else 0  # Boiler per docce
    heat_pump = 2 if hour in range(6, 9) or hour in range(17, 22) else 0  # Termopompa per riscaldamento serale
    small_devices = 0.1 * np.random.poisson(3)  # Piccoli utilizzatori variabili
    return base_load + fridge + lights + oven + boiler + heat_pump + small_devices

def simulate_solar_production(day_of_year, hour):
    """Simula la produzione solare in kW"""
    # Modifica stagionale e diurna per simulare irraggiamento
    season_factor = 1 - 0.3 * np.cos((day_of_year - 173) * 2 * np.pi / 365)  # Massimo intorno a metà anno
    day_factor = max(0, np.sin((hour - 6) * np.pi / 12))  # Massimo a mezzogiorno
    return solar_peak * season_factor * day_factor

# Calcolo dei consumi e della produzione
data['Consumption'] = [simulate_household_consumption(ts.hour) for ts in data.index]
data['SolarProduction'] = [simulate_solar_production(ts.day_of_year, ts.hour) for ts in data.index]

# Gestione energia in batteria
data['Battery'] = 0.0  # Energia stoccata in kWh
data['GridExport'] = 0.0  # Energia venduta in kWh
data['GridImport'] = 0.0  # Energia acquistata in kWh

for i in range(len(data)):
    production = data['SolarProduction'].iloc[i]
    consumption = data['Consumption'].iloc[i]

    # Calcolo energia disponibile e utilizzo della batteria
    surplus = production - consumption
    if surplus > 0:
        if battery_charge + surplus <= battery_capacity:
            battery_charge += surplus
            data['Battery'].iloc[i] = battery_charge
        else:
            data['Battery'].iloc[i] = battery_capacity
            data['GridExport'].iloc[i] = battery_charge + surplus - battery_capacity
            battery_charge = battery_capacity
    else:
        deficit = -surplus
        if battery_charge >= deficit:
            battery_charge -= deficit
            data['Battery'].iloc[i] = battery_charge
        else:
            data['Battery'].iloc[i] = 0
            data['GridImport'].iloc[i] = deficit - battery_charge
            battery_charge = 0

# Creazione grafici
plt.figure(figsize=(15, 10))

plt.subplot(4, 1, 1)
plt.plot(data.index, data['SolarProduction'], color='gold', label='Produzione Solare (kW)')
plt.ylabel("kW")
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(data.index, data['Consumption'], color='red', label='Consumo (kW)')
plt.ylabel("kW")
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(data.index, data['Battery'], color='blue', label='Energia Stoccata (kWh)')
plt.ylabel("kWh")
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(data.index, data['GridExport'], color='green', label='Energia Rivenduta (kWh)')
plt.plot(data.index, data['GridImport'], color='purple', label='Energia Importata (kWh)')
plt.ylabel("kWh")
plt.legend()

plt.tight_layout()
plt.show()
