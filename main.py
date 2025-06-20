import tkinter as tk
from core_queue_management import PrintQueue
from visualisation import PrintQueueVisualiser 

if __name__ == "__main__":
    pq = PrintQueue(5)
    root = tk.Tk()
    app = PrintQueueVisualiser(root, pq)
    root.mainloop() #Start the GUI event loop to display the print queue visualisation