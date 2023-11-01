{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNjMTJvRS8/P8pUixfmT9Mu",
      "include_colab_link": true
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
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nzamn/Tugas-DDP6/blob/main/While.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]\n",
        "i = 0\n",
        "while i <= len(numbers):\n",
        "  if numbers[i] % 2 != 0:\n",
        "   print(numbers[i])\n",
        "  if numbers[i] == 553:\n",
        "    break\n",
        "  i+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XajAa__d0Z8Y",
        "outputId": "c8d9bdcb-2f01-44c2-f17f-bd0c448fa2c2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "951\n",
            "651\n",
            "69\n",
            "319\n",
            "601\n",
            "485\n",
            "507\n",
            "725\n",
            "547\n",
            "615\n",
            "83\n",
            "165\n",
            "141\n",
            "501\n",
            "263\n",
            "617\n",
            "865\n",
            "575\n",
            "219\n",
            "105\n",
            "941\n",
            "47\n",
            "907\n",
            "375\n",
            "823\n",
            "597\n",
            "615\n",
            "953\n",
            "345\n",
            "399\n",
            "219\n",
            "237\n",
            "949\n",
            "687\n",
            "217\n",
            "815\n",
            "67\n",
            "767\n",
            "553\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 0\n",
        "for i in range(1,20,2):\n",
        "    x = x + i\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yuvRRFfr0rrz",
        "outputId": "464181d0-c13e-45ce-db59-95e7b7daabff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for m in range(0,int(input())):\n",
        "  for p in range(0,m+1):\n",
        "    print(\"*\", end=\" \")\n",
        "  print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OlB8JysC7bL_",
        "outputId": "ef0a5c96-5fdf-49fc-8068-8efb09cb76b9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "* \n",
            "* * \n",
            "* * * \n",
            "* * * * \n",
            "* * * * * \n"
          ]
        }
      ]
    }
  ]
}