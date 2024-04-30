from tkinter import *


class Converter:

    # convert height and weight inputs to bmi value
    def bmi_calculate(self):

        height = self.check_height()
        weight = self.weight_entry.get()
        weight = float(weight)

        if height == "amount":
            answer = "Please enter a height higher than 0cm"
        elif height == "number":
            answer = "Please make sure both entries are numbers"
        elif height == "empty":
            answer = "Please make sure neither entry is empty"
        else:
            answer = (weight / (height * height)) * 10000

        self.output_label.config(text=answer)

    def check_height(self):

        has_error = "no"

        height_response = self.height_entry.get()

        if height_response is not None:
            try:
                height_response = float(height_response)

                if height_response <= 0:
                    has_error = "amount"

            except ValueError:
                has_error = "number"
        else:
            has_error = "empty"

        if has_error == "no":
            return height_response
        else:
            return has_error

    def __init__(self):
        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # set up GUI frame
        self.bmi_frame = Frame()
        self.bmi_frame.grid()

        self.bmi_heading = Label(self.bmi_frame,
                                 text="BMI CALCULATOR",
                                 font=("Arial", "16", "bold")
                                 )
        self.bmi_heading.grid(row=0)

        instructions = "Enter your height, weight and age below in the allocated input" \
                       " boxes and then press calculate to be given your current BMI " \
                       "status."
        self.bmi_instructions = Label(self.bmi_frame,
                                      text=instructions,
                                      wrap=250, width=40,
                                      justify="left")
        self.bmi_instructions.grid(row=1, column=0)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.bmi_frame)
        self.button_frame.grid(row=4)

        self.output_label = Label(self.bmi_frame, text="",
                                  fg="#9C0000")
        self.output_label.grid(row=3)

        self.height_entry = Entry(self.button_frame,
                                  font=("Arial", "14"),
                                  width=12
                                  )
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)

        self.weight_entry = Entry(self.button_frame,
                                  font=("Arial", "14"),
                                  width=12
                                  )
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        self.age_entry = Entry(self.button_frame,
                               font=("Arial", "14"),
                               width=12
                               )
        self.age_entry.grid(row=2, column=1, padx=10, pady=10)

        self.height_label = Label(self.button_frame,
                                  text="HEIGHT:",
                                  justify="right",
                                  font=("Arial", "14"),
                                  width=12
                                  )
        self.height_label.grid(row=0, column=0, padx=5, pady=10)

        self.weight_label = Label(self.button_frame,
                                  text="WEIGHT:",
                                  justify="right",
                                  font=("Arial", "14"),
                                  width=12
                                  )
        self.weight_label.grid(row=1, column=0, padx=5, pady=10)

        self.age_label = Label(self.button_frame,
                               text="AGE:",
                               justify="right",
                               font=("Arial", "14"),
                               width=12
                               )
        self.age_label.grid(row=2, column=0, padx=5, pady=10)

        self.to_history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#004C99",
                                        fg=button_fg,
                                        font=button_font,
                                        width=12,
                                        state=DISABLED
                                        )
        self.to_history_button.grid(row=0, column=2, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg=button_fg,
                                     font=button_font,
                                     width=12
                                     )
        self.to_help_button.grid(row=1, column=2, padx=5, pady=5)

        self.to_calculate_button = Button(self.bmi_frame,
                                          text="Calculate",
                                          bg="#CC6600",
                                          fg=button_fg,
                                          font=button_font,
                                          width=36,
                                          command=lambda: self.bmi_calculate()
                                          )
        self.to_calculate_button.grid(row=5, padx=5, pady=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
