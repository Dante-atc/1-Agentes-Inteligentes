#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tarea_1.py
------------

Revisa el archivo README.md con las instrucciones de la tarea.

"""
__author__ = 'dante_tostado'

import entornos_f
import entornos_o

class NueveCuartos(entornos_o.Entorno):
    """
    Clase para un entorno de nueve cuartos.

    El estado se define como (robot, A, B, C, D, E, F, G, H, I)
    los cuartos del primer nivel son A, B, C
    los cuartos del segundo nivel son D, E, F
    los cuartos del tercer nivel son G, H, I
    donde robot puede tener los valores "A", "B", "C", "D", "E", "F", "G", "H", "I"
    A, B, C, D, E, F, G, H, I pueden tener los valores "limpio", "sucio"

    Las acciones válidas en el entorno son ("ir_Derecha", "ir_Izquierda", "subir", "bajar", "limpiar", "nada").
    La acción de "subir" solo es legal en los primeros dos pisos, en los cuartos de la derecha, 
    mientras que la acción de "bajar" solo es legal en los dos pisos de arriba de arriba y en el cuarto de la izquierda.
    Todas las demás acciones son válidas en todos los estados.

    Los sensores es una tupla (robot, limpio?)
    con la ubicación del robot y el estado de limpieza

    """
    def __init__(self, x0=["A", "sucio", "sucio", "sucio", "sucio", "sucio", "sucio", "sucio", "sucio", "sucio"]):
        """
        Por default inicialmente el robot está en A y los nueve cuartos están sucios
        
        """
        self.x = x0[:]
        self.costo = 0

    def accion_legal(self, accion):
        return accion in ("ir_Derecha", "ir_Izquierda", "subir", "bajar", "limpiar", "nada")

    def transicion(self, accion):
        if not self.accion_legal(accion):
            raise ValueError("La acción no es legal para este estado")
        
        robot = self.x[0]
        
        indice = " ABCDEFGHI".find(robot)
        
        # Costos
        costo_accion = 0
        if accion == "limpiar":
            costo_accion = 1  
        elif accion in ("ir_Derecha", "ir_Izquierda"):
            costo_accion = 2
        elif accion in ("subir", "bajar"):
            costo_accion = 3
        self.costo += costo_accion
        
        if accion == "limpiar":
            self.x[indice] = "limpio"
            
        elif accion == "ir_Derecha":
            # Si no esta en borde derecho (C, F, I son índices 3, 6, 9)
            if indice % 3 != 0: 
                # Moverse a la derecha es sumar 1 (A->B, D->E)
                self.x[0] = " ABCDEFGHI"[indice + 1]
                
        elif accion == "ir_Izquierda":
            # Si no esta en borde izquierdo (A, D, G son índices 1, 4, 7)
            if (indice - 1) % 3 != 0: 
                # Moverse a la izquierda es restar 1 (B->A, E->D)
                self.x[0] = " ABCDEFGHI"[indice - 1]
        
        elif accion == "subir":
            # Solo legal en pisos 1 y 2, cuartos derecha (C y F). Osea indices 3 y 6.
            if indice in (3, 6):
                # Subir de C a F es sumar 3.
                self.x[0] = " ABCDEFGHI"[indice + 3]
                
        elif accion == "bajar":
            # Solo legal en pisos 2 y 3, cuarto izquierda (D y G). Osea indices 4 y 7.
            if indice in (4, 7):
                # Bajar de D a A es restar 3.
                self.x[0] = " ABCDEFGHI"[indice - 3]

    def percepcion(self):
        return self.x[0], self.x[" ABCDEFGHI".find(self.x[0])]

# Requiere el modulo entornos_f.py o entornos_o.py
# Usa el modulo doscuartos_f.py para reutilizar código
# Agrega los modulos que requieras de python

