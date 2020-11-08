{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number of chances you want:1\n",
      "Enter your GUESS:2\n",
      "Enter a higher number than 2 number\n",
      "You have lost,The number was8\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "input_number=random.randint(1,9)\n",
    "chances=0\n",
    "times=int(input(\"Enter number of chances you want:\"))\n",
    "\n",
    "while(chances<times):\n",
    "    guess_number=int(input(\"Enter your GUESS:\"))\n",
    "    \n",
    "    if(guess_number==input_number):\n",
    "        print(\"YOUR GUESS WAS RIGHT:\")\n",
    "        chances=chances+1\n",
    "        break\n",
    "    elif(guess_number<input_number):\n",
    "        print(\"Enter a higher number than {} number\".format(guess_number))\n",
    "        chances=chances+1\n",
    "        \n",
    "    elif(guess_number>input_number):\n",
    "        print(\"Enter a Lower number than {} number\".format(guess_number))\n",
    "        chances=chances+1\n",
    "           \n",
    "    if not(chances<times):\n",
    "        print(\"You have lost,The number was {}\".format(input_number))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
