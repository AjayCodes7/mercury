from breezypythongui import EasyFrame


class Calculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Calculator",
                           width=450, height=350, background="black")
        self.name = self.addLabel(text="Calculator", row=0, column=0,
                                  font="consolas", background="Black", foreground="white")
        self.result = self.addLabel(
            text="", row=0, column=2, background="black", foreground="white", font="calibri")
        self.op1 = 0
        self.op2 = 0
        self.pop = ""
        self.flag = 0
        self.addButton(text="\n\t1\t\n", row=2, column=0, command=self.one)
        self.addButton(text="\n\t2\t\n", row=2, column=1, command=self.two)
        self.addButton(text="\n\t3\t\n", row=2, column=2, command=self.three)
        self.addButton(text="\n\t-\t\n", row=5, column=2, command=self.minus)
        self.addButton(text="\n\t4\t\n", row=3, column=0, command=self.four)
        self.addButton(text="\n\t5\t\n", row=3, column=1, command=self.five)
        self.addButton(text="\n\t6\t\n", row=3, column=2, command=self.six)
        self.addButton(text="\n\tX\t\n", row=3,
                       column=3, command=self.multiply)
        self.addButton(text="\n\t7\t\n", row=4, column=0, command=self.seven)
        self.addButton(text="\n\t8\t\n", row=4, column=1, command=self.eight)
        self.addButton(text="\n\t9\t\n", row=4, column=2, command=self.nine)
        self.addButton(text="\n\t/\t\n", row=4, column=3, command=self.devide)
        self.addButton(text="\n\t0\t\n", row=5, column=0, command=self.zero)
        self.addButton(text="\n\t+\t\n", row=5, column=1, command=self.plus)
        self.addButton(text="\n\tCE\t\n", row=2, column=3, command=self.clear)
        self.addButton(text="\n\t=\t\n", row=5, column=3, command=self.equalto)

    def one(self):
        if self.flag == 1:
            self.op2 = self.op2*10 + 1
            #   self.result["text"] = str(self.op2)
            self.result["text"] = str(self.op2)
        else:
            self.op1 = self.op1*10 + 1
            # self.result["text"] = str(self.op1)
            self.result["text"] = str(self.op1)

    def two(self):
        if self.flag == 1:
            self.op2 = self.op2*10 + 2
            self.result["text"] = str(self.op2)
        else:
            self.op1 = self.op1*10 + 2
            self.result["text"] = str(self.op1)

    def three(self):
        if self.flag == 1:
            self.op2 = self.op2*10 + 3
            self.result["text"] = str(self.op2)
        else:
            self.op1 = self.op1*10 + 3
            self.result["text"] = str(self.op1)

    def four(self):
        if self.flag == 1:
            self.op2 = self.op2*10 + 4
            self.result["text"] = str(self.op2)
        else:
            self.op1 = self.op1*10 + 4
            self.result["text"] = str(self.op1)

    def five(self):
        if self.flag == 1:
            self.op2 = self.op2*10 + 5
            self.result["text"] = str(self.op2)
        else:
            self.op1 = self.op1*10 + 5
            self.result["text"] = str(self.op1)

    def six(self):
        if self.flag == 1:
            self.op2 = self.op2*10 + 6
            self.result["text"] = str(self.op2)
        else:
            self.op1 = self.op1*10 + 6
            self.result["text"] = str(self.op1)

    def seven(self):
        if self.flag == 1:
            self.op2 = self.op2*10 + 7
            self.result["text"] = str(self.op2)
        else:
            self.op1 = self.op1*10 + 7
            self.result["text"] = str(self.op1)

    def eight(self):
        if self.flag == 1:
            self.op2 = self.op2*10 + 8
            self.result["text"] = str(self.op2)
        else:
            self.op1 = self.op1*10 + 8
            self.result["text"] = str(self.op1)

    def nine(self):
        if self.flag == 1:
            self.op2 = self.op2*10 + 9
            self.result["text"] = str(self.op2)
        else:
            self.op1 = self.op1*10 + 9
            self.result["text"] = str(self.op1)

    def zero(self):
        if self.flag == 1:
            self.op2 = self.op2*10 + 0
            self.result["text"] = str(self.op2)
        else:
            self.op1 = self.op1*10 + 0
            self.result["text"] = str(self.op1)

    def plus(self):
        self.flag = 1
        self.pop = "+"
        self.result["text"] = "+"

    def minus(self):
        self.flag = 1
        self.pop = "-"
        self.result["text"] = "-"

    def multiply(self):
        self.flag = 1
        self.pop = "*"
        self.result["text"] = "*"

    def devide(self):
        self.flag = 1
        self.pop = "/"
        self.result["text"] = "/"

    def equalto(self):
        if self.pop == "+":
            self.op1 = self.op1 + self.op2
        if self.pop == "-":
            self.op1 = self.op1 - self.op2
        if self.pop == "*":
            self.op1 = self.op1 * self.op2
        if self.pop == "/":
            self.op1 = self.op1 / self.op2
        self.result["text"] = str(self.op1)
        self.op2 = 0

    def clear(self):
        self.op1 = 0
        self.op2 = 0
        self.flag = 0
        self.result["text"] = ""
        self.pop = ""


def main():
    Calculator().mainloop()


if __name__ == "__main__":
    main()
