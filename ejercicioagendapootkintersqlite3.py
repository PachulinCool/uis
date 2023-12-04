import numpy as np
from tkinter import *
import sqlite3 as sql

class algebra():
    def __init__(self, inter):
        self.interfaz = inter
        self.interfaz.geometry("300x300")
        self.interfaz.title(" algebra")
        self.num1 = StringVar()

        self.dibujarVentana()
        self.createDB()

    def dibujarVentana(self):
        Label(self.interfaz, text="digite el vector delimitado por comas").place(x=10, y=10)
        Entry(self.interfaz, textvariable=self.num1).place(x=20, y=30)

        Button(self.interfaz, command=self.octener, text="Subir ya").place(x=170, y=250)

    def octener(self):
        self.resp1 = self.num1.get()
        print(self.resp1)
        numeros_str = self.resp1.split(',')
        numeros_float = [float(numero) for numero in numeros_str]
        self.vector_numpy = np.array([numeros_float])
        print("Vector NumPy resultante:", self.vector_numpy)
        self.vec()

    def vec(self):
        self.vectors=self.vector_numpy
        self.orthonormal_basis = self.gram_schmidt()
        self.result()

    def gram_schmidt(self):
        num_vectors, vector_size = self.vectors.shape
        basis = np.zeros((num_vectors, vector_size))
        for i in range(num_vectors):
            basis[i] = self.vectors[i]
            for j in range(i):
                basis[i] -= np.dot(self.vectors[i], basis[j]) / np.dot(basis[j], basis[j]) * basis[j]
            basis[i] /= np.linalg.norm(basis[i])
        return basis

    def result(self):
        print("Vector original:")
        print(self.vectors)

        print("\nVectores ortogonales normalizados:")
        print(self.orthonormal_basis)

        self.storeVectors()

    def createDB(self):
        self.conn= sql.connect("vectores.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS vectors (original TEXT, orthonormal TEXT)')
        self.conn.commit()

    def storeVectors(self):
        self.cursor.execute('INSERT INTO vectors VALUES (?, ?)', (str(self.vectors), str(self.orthonormal_basis)))
        self.conn.commit()

al=algebra(Tk())
al.interfaz.mainloop()
