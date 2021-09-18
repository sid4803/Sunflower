#*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:38:26 2021

@author: Manoj
"""
from tkinter import *
root=Tk()
root.title("fibonacci")
root.geometry("400x400")
label_series=Label(root,text="Fibonacci series:")
label_flower=Label(root)
label_spiral=Label(root)
def fibonacci():
    num=10
    first=0
    second=1
    sum=0
    counter=1
    while(counter<=num):
        label_series['text']+=str(sum)+""
   
        counter+=1
        first=second
        second=sum
        sum=first+second
    label_flower['text']="flower is fully bloomed"
    label_spiral['text']="onright"+str(first)+"onleft"+str(second)+"totaly"+str(sum)
btn=Button(root,text="show",command=fibonacci)
btn.pack()
label_series.pack
label_flower.pack
label_spiral.pack