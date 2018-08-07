"""
All you have to do is type return "hello edabit.com"; between the curly braces and click the Check button.
If everything went according to plan, the button will turn red and say SUBMIT FINAL. Click it and see what happens.
"""
function hello() {
	return "hello edabit.com";
}

"""
Create a function that takes two numbers as arguments and return their sum.

"""
function addition(a, b) {
	 return a+b ;
}
"""
Create a function that accepts an array and returns the last item in the array.
Examples
[1, 2, 3] ➞ 3

['cat', 'dog', 'duck'] ➞ 'duck'

[true, false, true] ➞ true
"""
function getLastItem(arr) {
	 return arr[arr.length - 1]
}

