{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNCTo8e+lNPS6jSsfPF1RyJ"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "StYiLzoI_nft"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "OzlT8cqBjgpE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4bddee40-41a9-4ea6-d929-5816d781fb5b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "---  Bienvenido a CineStar  ---\n",
            "Sala  1 :  Batman\n",
            "Sala  2 :  Avatar\n",
            "Sala  3 :  Spiderman\n",
            "Sala  4 :  Mario Bros\n",
            "cuantos años tienes? : 10\n",
            "selecciona la película : 4\n",
            "Cuantas entradas quieres? : 2\n",
            "Por último, ¿Qué día es hoy?Viernes\n",
            "********** TICKET DE CINE **********\n",
            "Película:  4\n",
            "Cantidad:  2  entradas\n",
            "Total a pagar: 15.0\n",
            "************************************\n"
          ]
        }
      ],
      "source": [
        "def mostrar_cartelera(lista_peliculas, salas_disponibles, mensaje_bienvenida):\n",
        "    print(\"--- \",mensaje_bienvenida,\" ---\")\n",
        "\n",
        "    for i in range(salas_disponibles):\n",
        "        print(\"Sala \", i + 1, \": \",lista_peliculas[i])\n",
        "\n",
        "def calcular_precio(edad, cantidad, dia_semana):\n",
        "    precio = 10.0 * cantidad\n",
        "\n",
        "    if edad < 12 or edad > 60:\n",
        "        precio= precio -3.0\n",
        "\n",
        "    if dia_semana == \"viernes\" or dia_semana == \"Viernes\":\n",
        "        precio= precio-2.0\n",
        "\n",
        "    return precio\n",
        "\n",
        "def imprimir_ticket(pelicula, cantidad_boletos, costo_total):\n",
        "    print(\"********** TICKET DE CINE **********\")\n",
        "    print(\"Película: \",pelicula)\n",
        "    print(\"Cantidad: \",cantidad_boletos, \" entradas\")\n",
        "    print(\"Total a pagar:\", costo_total)\n",
        "    print(\"************************************\")\n",
        "\n",
        "peliculas = [\"Batman\", \"Avatar\", \"Spiderman\", \"Mario Bros\"]\n",
        "mostrar_cartelera(peliculas, 4, \"Bienvenido a CineStar\")\n",
        "\n",
        "user_edad= int(input(\"cuantos años tienes? : \"))\n",
        "user_peli= int(input(\"selecciona la película : \"))\n",
        "user_entradas= int(input(\"Cuantas entradas quieres? : \"))\n",
        "día= str(input(\"Por último, ¿Qué día es hoy?\"))\n",
        "\n",
        "precio_unitario = calcular_precio(user_edad, user_entradas, día)\n",
        "imprimir_ticket(user_peli, user_entradas, precio_unitario)"
      ]
    }
  ]
}