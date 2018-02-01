# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = -2, denominator = 1, return "-2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Given numerator = 5, denominator = 2, return "2.5".

def divide(numerator, denominator):
	n, remainder = divmod(abs(numerator), abs(denominator))
	if numerator * denominator < 0:
		sign = '-'
	else:
		sign = ''

	result = [sign + str(n), '.']
	stack = []
	while remainder not in stack:
		stack.append(remainder)
		n, remainder = divmod(remainder * 10, abs(denominator))
		result.append(str(n))

	idx = stack.index(remainder)
	result.insert(idx + 2, '(')
	result.append(')')

	return ''.join(result).replace('(0)', '').rstrip('.')