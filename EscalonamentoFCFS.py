import time

class Job:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class Printer:
    def __init__(self):
        self.queue = []

    def add_job(self, job):
        self.queue.append(job)

    def print_jobs(self):
        for job in self.queue:
            print(f"Printing job '{job.name}'...")
            time.sleep(job.duration)
            print(f"Job '{job.name}' printed.")
        
        self.queue = []

printer = Printer()

# Adiciona alguns trabalhos à fila de impressão
printer.add_job(Job("Relatório", 5))
printer.add_job(Job("Carta", 3))
printer.add_job(Job("Apresentação", 8))

# Executa a fila de impressão em ordem FCFS
printer.print_jobs()

