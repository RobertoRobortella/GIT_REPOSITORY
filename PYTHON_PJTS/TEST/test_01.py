import psutil
import matplotlib.pyplot as plt
import time

def stress_system():
    print("Stressando il sistema...")
    
    # Monitoraggio delle risorse
    cpu_usage = []
    mem_usage = []
    gpu_usage = []
    
    start_time = time.time()
    
    while True:
        current_cpu = psutil.cpu_percent(interval=1)
        current_mem = psutil.virtual_memory().percent
        current_gpu = 0 # Assumiamo che non abbiamo accesso diretto alla GPU

        
        cpu_usage.append(current_cpu)
        mem_usage.append(current_mem)
        
        if len(cpu_usage) > 100: # Aggiornamento ogni 100 iterazioni
            break
    
    end_time = time.time()
    duration = end_time - start_time
    
    return cpu_usage, mem_usage, gpu_usage, duration

# Esecuzione dello stress
cpu_usage, mem_usage, gpu_usage, duration = stress_system()

print(f"Durata dell'esecuzione: {duration:.2f} secondi")

# Generazione dei grafici
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(cpu_usage)
plt.title('Utilizzo CPU')
plt.xlabel('Tempo')
plt.ylabel('Percentuale')

plt.subplot(3, 1, 2)
plt.plot(mem_usage)
plt.title('Utilizzo RAM')
plt.xlabel('Tempo')
plt.ylabel('Percentuale')

plt.subplot(3, 1, 3)
plt.plot(gpu_usage)
plt.title('Utilizzo GPU')
plt.xlabel('Tempo')
plt.ylabel('Percentuale')

plt.tight_layout()
plt.show()

print("Grafici delle prestazioni generati!")
