{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2ef89d1a-c3f4-4008-91ff-515600eb0811",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Q1. Create one variable containing following type of data:\n",
    "''' (i) string\n",
    "    (ii) list\n",
    "    (iii) float\n",
    "    (iv) tuple'''\n",
    "\n",
    "#solution'\n",
    "var_string='i am learn data science'\n",
    "var_list=['python','mysql','machine learning']\n",
    "var_float=10.10\n",
    "var_tuple=('python','mysql','machine learning')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "fccec509-d708-4448-83dd-70c6c02cd3ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "<class 'str'>\n",
      "<class 'list'>\n",
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "#Q2. Given are some following variables containing data:\n",
    "''' (i) var1 = ''\n",
    "    (ii) var2 = '[ DS , ML , Python]'\n",
    "    (iii) var3 = [ 'DS' , 'ML', 'Python' ]\n",
    "     (iv) var4 = 1.\n",
    "What will be the data type of the above given variable. '''\n",
    "\n",
    "#solutuon\n",
    "\n",
    "var1 = ''\n",
    "var2 = '[ DS , ML , Python]'\n",
    "var3 = [ 'DS' , 'ML', 'Python' ]\n",
    "var4 = 1.\n",
    "print(type(var1))\n",
    "print(type(var2))\n",
    "print(type(var3))\n",
    "print(type(var4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32e08963-030a-43b1-9d8e-bd396eea7f3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "Q3. Explain the use of the following operators using an example:\n",
    "(i) /\n",
    "(ii) %\n",
    "(iii) //\n",
    "(iv) **\n",
    "'''\n",
    "#Solution\n",
    "i>The division operator / is used to divide one number by another and returns a floating-point result\n",
    "result = 10 / 3\n",
    "print(result)  # Output: 3.3333333333333335\n",
    "ii> Modulus (%)\n",
    "The modulus operator % returns the remainder of the division of one number by another.\n",
    "remainder = 10 % 3\n",
    "print(remainder)  # Output: 1\n",
    "\n",
    "iii>Floor Division (//)\n",
    "The floor division operator // divides one number by another and returns the largest integer less than or equal to the result.\n",
    "floor_result = 10 // 3\n",
    "print(floor_result)  # Output: 3\n",
    "(iv) **\n",
    "The exponentiation operator ** raises the first number to the power of the second number.\n",
    "power = 2 ** 3\n",
    "print(power)  # Output: 8\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "87294b93-f5ed-4b13-b00f-de0c1c3810cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Element: 10, Type: <class 'int'>\n",
      "Element: 3.14, Type: <class 'float'>\n",
      "Element: Hello, Type: <class 'str'>\n",
      "Element: True, Type: <class 'bool'>\n",
      "Element: None, Type: <class 'NoneType'>\n",
      "Element: [1, 2, 3], Type: <class 'list'>\n",
      "Element: {'a': 1, 'b': 2}, Type: <class 'dict'>\n",
      "Element: (4, 5), Type: <class 'tuple'>\n",
      "Element: {1, 2, 3}, Type: <class 'set'>\n",
      "Element: b'byte', Type: <class 'bytes'>\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the\n",
    "element and its data type.\n",
    "'''\n",
    "# Creating a list of length 10 with multiple types of data\n",
    "mixed_list = [10, 3.14, \"Hello\", True, None, [1, 2, 3], {'a': 1, 'b': 2}, (4, 5), {1, 2, 3}, b'byte']\n",
    "\n",
    "# Using a for loop to print each element and its data type\n",
    "for element in mixed_list:\n",
    "    print(f\"Element: {element}, Type: {type(element)}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "817f876a-0a88-41b0-b30a-5b47fb57d7f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number can be divided 2 times.\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many\n",
    "times it can be divisible.\n",
    "'''\n",
    "# Initialize the numbers A and B\n",
    "A = 100\n",
    "B = 2\n",
    "\n",
    "# Initialize a count variable to count how many times A can be divided by B\n",
    "count = 0\n",
    "\n",
    "# Using a while loop to check divisibility and count the number of times\n",
    "while A % B == 0:\n",
    "    A = A // B\n",
    "    count += 1\n",
    "\n",
    "# Print the result\n",
    "print(f\"The number can be divided {count} times.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "00da074a-2a81-4094-b2ca-a966aa4033d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 is not divisible by 3.\n",
      "2 is not divisible by 3.\n",
      "3 is divisible by 3.\n",
      "4 is not divisible by 3.\n",
      "5 is not divisible by 3.\n",
      "6 is divisible by 3.\n",
      "7 is not divisible by 3.\n",
      "8 is not divisible by 3.\n",
      "9 is divisible by 3.\n",
      "10 is not divisible by 3.\n",
      "11 is not divisible by 3.\n",
      "12 is divisible by 3.\n",
      "13 is not divisible by 3.\n",
      "14 is not divisible by 3.\n",
      "15 is divisible by 3.\n",
      "16 is not divisible by 3.\n",
      "17 is not divisible by 3.\n",
      "18 is divisible by 3.\n",
      "19 is not divisible by 3.\n",
      "20 is not divisible by 3.\n",
      "21 is divisible by 3.\n",
      "22 is not divisible by 3.\n",
      "23 is not divisible by 3.\n",
      "24 is divisible by 3.\n",
      "25 is not divisible by 3.\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is\n",
    "divisible b\n",
    "'''\n",
    "#Solution\n",
    "# Create a list containing 25 integers\n",
    "int_list = [i for i in range(1, 26)]  # This creates a list with numbers from 1 to 25\n",
    "\n",
    "# Loop through the list and check if each element is divisible by 3\n",
    "for number in int_list:\n",
    "    if number % 3 == 0:\n",
    "        print(f\"{number} is divisible by 3.\")\n",
    "    else:\n",
    "        print(f\"{number} is not divisible by 3.\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "735b617e-e61f-425d-bd72-b0c0dd88f57c",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "Q7. What do you understand about mutable and immutable data types? Give examples for both showing\n",
    "this property.\n",
    "'''\n",
    "Mutable Data Types\n",
    "Mutable data types are those whose values can be changed in place after they are created. This means that you can modify the content of the data type without creating a new object.\n",
    "\n",
    "Examples of Mutable Data Types:\n",
    "\n",
    "Lists\n",
    "Dictionaries\n",
    "Sets\n",
    "# Example with a list\n",
    "my_list = [1, 2, 3]\n",
    "print(\"Original list:\", my_list)\n",
    "\n",
    "# Modifying the list\n",
    "my_list[0] = 10\n",
    "print(\"Modified list:\", my_list)\n",
    "# Example with a list\n",
    "my_list = [1, 2, 3]\n",
    "print(\"Original list:\", my_list)\n",
    "\n",
    "# Modifying the list\n",
    "my_list[0] = 10\n",
    "print(\"Modified list:\", my_list)\n",
    "# Example with a string\n",
    "my_string = \"Hello\"\n",
    "print(\"Original string:\", my_string)\n",
    "\n",
    "# Modifying the string\n",
    "my_string = my_string + \" World\"\n",
    "print(\"Modified string:\", my_string)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
