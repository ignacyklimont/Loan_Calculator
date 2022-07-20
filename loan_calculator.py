import argparse
import math
import sys

parser = argparse.ArgumentParser(description="This is a program to calculate the loan)")
parser.add_argument("--type", choices=['annuity', 'diff'])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

elements = [args.type, args.payment, args.principal, args.periods, args.interest]

if args.type == 'annuity':
	if args.interest is None:
		print('Incorrect parameters')
	elif len(sys.argv) < 4:
		print('Incorrect parameters')
	else:
		if args.payment is None:
			loan_principal = float(args.principal)
			num_of_periods = float(args.periods)
			loan_interest = float(args.interest)
			nominal_interest = loan_interest / (12 * 100)
			annuity_payment = loan_principal * ((nominal_interest * ((1 + nominal_interest) ** num_of_periods)) / (
						(1 + nominal_interest) ** num_of_periods - 1))
			annuity_payment = math.ceil(annuity_payment)
			print(f'Your monthly payment = {int(annuity_payment)}!')
			print(f'Overpayment = {int(annuity_payment * num_of_periods - loan_principal)}')
		elif args.principal is None:
			annuity_payment = float(args.payment)
			num_of_periods = float(args.periods)
			loan_interest = float(args.interest)
			nominal_interest = loan_interest / (12 * 100)
			loan_principal = annuity_payment / ((nominal_interest * ((1 + nominal_interest) ** num_of_periods)) / (
						(1 + nominal_interest) ** num_of_periods - 1))
			loan_principal = math.ceil(loan_principal)
			print(f'Your loan principal = {int(loan_principal)}!')
			print(f'Overpayment = {int(annuity_payment *  num_of_periods - loan_principal)}')
		elif args.periods is None:
			loan_principal = float(args.principal)
			monthly_payment = float(args.payment)
			loan_interest = float(args.interest)
			nominal_interest = loan_interest / (12 * 100)
			num_of_months = math.log(monthly_payment / (monthly_payment - nominal_interest * loan_principal),
			                         1 + nominal_interest)
			num_of_months = math.ceil(num_of_months)
			if num_of_months % 12 == 0:
				if num_of_months / 12 == 1:
					print('It will take 1 year to repay this loan!')
				else:
					print(f'It will take {int(num_of_months / 12)} years to repay this loan!')
			else:
				if num_of_months / 12 < 1:
					print(f'It will take {int(num_of_months)} months to repay this loan!')
				else:
					print(
						f'It will take {int(num_of_months // 12)} years and {int(num_of_months % 12)} months to repay this loan!')
			print(f'Overpayment = {int(monthly_payment * num_of_months - loan_principal)}')

elif args.type == 'diff':
	if args.payment is not None:
		print('Incorrect parameters')
	elif len(sys.argv) < 4:
		print('Incorrect parameters')
	else:
		loan_principal = float(args.principal)
		num_of_periods = float(args.periods)
		loan_interest = float(args.interest)
		nominal_interest = loan_interest / (12 * 100)
		m = 1
		sum = 0
		while m <= num_of_periods:
			monthly_payment = loan_principal/num_of_periods + nominal_interest * (loan_principal - ((loan_principal * (m - 1))/num_of_periods))
			monthly_payment = math.ceil(monthly_payment)
			print(f'Month {m}: payment is {int(monthly_payment)}')
			sum += monthly_payment
			m += 1
		print(f'Overpayment = {int(loan_principal - sum)}')
else:
	print('Incorrect parameters')
