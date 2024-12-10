import tkinter as tk
import joblib
import pandas as pd

#Create UI Application
window = tk.Tk()

frame1 = tk.Frame()
frame1.pack()

title = tk.Label(text="Iris Classification", width=30)
title.pack(pady=(0, 10))

frame2 = tk.Frame()
frame2.pack()

tk.Label(frame2, text="Sepal Length", width=12, anchor="w").grid(row=0)
input_sepal_length = tk.Entry(frame2, width=10)
input_sepal_length.grid(row=0, column=1)
tk.Label(frame2, text=" cm", width=5, anchor="w").grid(row=0, column=2)

tk.Label(frame2, text="Sepal Width", width=12, anchor="w").grid(row=1)
input_sepal_width = tk.Entry(frame2, width=10)
input_sepal_width.grid(row=1, column=1)
tk.Label(frame2, text=" cm", width=5, anchor="w").grid(row=1, column=2)

tk.Label(frame2, text="Petal Length", width=12, anchor="w").grid(row=2)
input_petal_length = tk.Entry(frame2, width=10)
input_petal_length.grid(row=2, column=1)
tk.Label(frame2, text=" cm", width=5, anchor="w").grid(row=2, column=2)

tk.Label(frame2, text="Petal Width", width=12, anchor="w").grid(row=3)
input_petal_width = tk.Entry(frame2, width=10)
input_petal_width.grid(row=3, column=1)
tk.Label(frame2, text=" cm", width=5, anchor="w").grid(row=3, column=2)

#Predict Model
model = joblib.load("model.pkl")

def predict_result():
    try:
        sepal_length = float(input_sepal_length.get())
        sepal_width = float(input_sepal_width.get())
        petal_length = float(input_petal_length.get())
        petal_width = float(input_petal_width.get())

        input_data = {"sepal.length": [sepal_length], "sepal.width": [sepal_width], 
                      "petal.length": [petal_length], "petal.width": [petal_width]}
        df = pd.DataFrame(input_data)

        predict = model.predict(df)
        output_result.config(text=f"Sepal length : {sepal_length} cm\n"
                                  f"Sepal width : {sepal_width} cm\n"
                                  f"Petal length : {petal_length} cm\n"
                                  f"Petal width : {petal_width} cm\n"
                                  f"\n"
                                  f"Predict result : Iris {predict[0]}")
    except ValueError:
        output_result.config(text="Error")

frame3 = tk.Frame()
frame3.pack(pady=10)

bt_submit = tk.Button(frame3, text="Submit", width=25, command=predict_result)
bt_submit.pack(pady=(0, 5))

output_result = tk.Label(frame3, width=25, height=6, justify="left", anchor="nw",)
output_result.pack()

window.mainloop()