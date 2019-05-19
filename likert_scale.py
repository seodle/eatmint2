#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

"""likert_question.py: create likert scale questions with the tkinter package"""

__author__ = "Sunny Avry"
__version__ = "3.6.3"

from tkinter import *
import random

class likert_question(Frame):
    def __init__(self, parent, label='', row=0):
        """
            Create a likert scale associated with a question
        """
        Frame.__init__(self, parent)
        self._parent = parent
        self.label = label
        self.row = row
        self._value = IntVar()
        self._check = IntVar()
        self._ongoing_value = StringVar()

        self._initUI()

    def _initUI(self):
        """
        	Define the scale and associate a value
        """
        self._label = Label(self._parent,text=self.label, fg="white", bg="#0B1321")
        self._label.grid(row=self.row, column=0, sticky=W)
        self._label.config(font=(None, 10, 'bold'))

        self._scale = Scale(self._parent,orient=HORIZONTAL, fg='white', bg='#0B1321',
                                      length=250, from_=1,
                                      to=7, tickinterval=1, troughcolor='white', highlightbackground='#0B1321',
                                      showvalue=0, variable=self._value, command=self._ongoing_values)
        self._scale.grid(row=self.row, column=1)
        # checkbutton whether user wants to answer the question
        self._tick = Checkbutton(self._parent,text='NOPN', bg='#0B1321', fg='gray', activebackground='#0B1321',
                                height=1, variable=self._check, command=self._tick_button)
        self._tick.grid(row=self.row, column=2)

    def _tick_button(self):
        """
        	Disable the scale when the tick is enabled
        """
        if self._check.get() == 1:
            self._scale.config(state=DISABLED, fg='gray', troughcolor='gray',label='Pas de réponse')
            self._value.set(1)
        else:
            self._scale.config(state=NORMAL, fg='white', troughcolor='white')

    def _ongoing_values(self,value):
        """
        	Specifiy the label corresponding to the scale (e.g.: 1 --> Not at all)
        """
        if self._value.get() == 1:
            self._scale.config(label='Very strongly disagree')
        if self._value.get() == 2:
            self._scale.config(label='Strongly disagree')
        if self._value.get() == 3:
            self._scale.config(label='Disagree')
        if self._value.get() == 4:
            self._scale.config(label='Neither agree nor disagree')
        if self._value.get() == 5:
            self._scale.config(label='Agree')
        if self._value.get() == 6:
            self._scale.config(label='Strongly agree')
        if self._value.get() == 7:
            self._scale.config(label='Very strongly agree')

    def getValue(self):
        """
        	Return -1 if the scale is disabled, return the value of the scale if the scale is enabled
        """
        if self._check.get() == 1:
            return -1
        else:
            return self._value.get()

list_of_questions = ['question1',
                   'question2',
                   'question3',
                   'question4',
                   'question5']

random.shuffle(list_of_questions)

list_of_instances = [None] * len(list_of_questions)

root = Tk()
root.configure(bg='#0B1321')
root.title('Likert questions example')
 
for i in range(len(list_of_questions)):
	list_of_instances[i] = likert_question(root, list_of_questions[i], i)

root.mainloop()

