import wmi
import csv


f = wmi.WMI()

#create csv with headers
with open('processes.csv', 'w', newline = '') as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames = ['Process ID', 'Process Name', 'Memory Utilization'])
  writer.writeheader()
  #iterate through all the running processes 
  for process in f.Win32_Process():
    entry = (process.ProcessId, process.Name, process.WorkingSetSize)
    writer = csv.writer(csvfile)
    writer.writerow(entry)
   

