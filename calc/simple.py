import math

#import pandas as pd
#import numpy as np
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import PySimpleGUI as sg
#import matplotlib

#fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
#fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

#matplotlib.use("TkAgg")

#def draw_figure(canvas, figure):
#    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
#    figure_canvas_agg.draw()
#    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
#    return figure_canvas_agg
  
# Define the window layout
#layout = [
#    [sg.Text("Plot test")],
#    [sg.Canvas(key="-CANVAS-")],
#    [sg.Button("Ok")],
#]

# Create the form and show it without the plot
#window = sg.Window(
#    "Matplotlib Single Graph",
#    layout,
#    location=(0, 0),
#    finalize=True,
#    element_justification="center",
#    font="Helvetica 18",
#)

# Add the plot to the window
#draw_figure(window["-CANVAS-"].TKCanvas, fig)

#event, values = window.read()

#window.close()  

P=float(input("Design Pressure:"))
SE=float(input("Allowable Stress:"))
D=float(input("Inside Diameter:"))
Ca=float(input("Corrosion Allowance:"))

#corrosion allowance
Di=D+2*Ca
R=Di/2

#per div1

#cir stress tmin
tc=(P*R)/(SE-0.6*P)

#long stress min
tt=(P*R)/(2*SE+0.4*P)

#greater of the two
t=max(tc,tt)
t1=t+Ca

#per div 2
t0=R*((math.exp(P/SE))-1)
t2=t0+Ca

#results

print("tmin :", t, '"')
print("tMin + CA :", t1, '"')

print("By the way Ben, it's due to licensing costs.")

#print("div1 tmin :", t, '"')
#print("div1 tmin + Ca :", t1, '"')

#print("div2 tmin :", t0, '"')
#print("div2 tmin + Ca:", t2, '"')
