# fincalc.py
# (cc) BY 2021-10-05 Pete Laric / www.PeteLaric.com
# A simple financial calculator for solving equations concerning compound
# interest, annuities, etc.  Created for Quantitative Methods in Finance at
# HSE University, Moscow, with Prof. Ayana Shelike.
#
# Definitions
# Annuity: Series of equal cash flows.
# Ordinary Annuity: Finite string of single payments.  Equal payments at END of
# each N periods.  Example: mortgage.  <-- N payments in total.
# Annuity Due: also finite string of equal payments.  Equal payments at the
# BEGINNING of each N periods.  Example: rent.  <-- N payments in total.
# Perpetuity: Just like ordinary annuity, but it is infinite.  Equal payments
# at the end of infinite number of periods.  Example: consol bonds.  <-- Inf
# payments in total.


import math

print('\n\n')
print('Compound Interest Calculator')
print('Select an option:')
print('*************************************** COMPOUND INTEREST ****************************************')
print('1. Compute final value from present value, rate, number of periods: FV_N = PV * (1 + r)^N')
print('2. Compute present value from final value, rate, number of periods: PV = FV_N / (1 + r)^N')
print('3. Compute rate from present value, future value, number of periods: r = (FV_N / PV) ^ (1/N) - 1')
print('4. Continuous compounding: FV = PV * e^(r*t)')
print('5. Compute effective annual rate (EAR) from stated rate (r_s) [continuous method]: EAR = e^r_s - 1')
print('6. Compute number of periods from present value, rate, future value: N = ln(FV_N / PV) / ln(1+r)')
print('**************************************** ORDINARY ANNUITY ****************************************')
print('7. Compute future value of ordinary annuity: FV_N = (A/r) * ((1 + r)^N - 1)')
print('8. Compute annuity payment necessary to reach some target: A = (FV_N * r) / ((1 + r)^N - 1)')
print('9. Compute present value of ordinary annuity: PV = FV_N / (1+r)^N')
print('10. Ordinary Annuity single formula: PVord_N = A * ((1+r)^N - 1) / (r * (1 + r)^N)')
print('****************************************** ANNUITY DUE *******************************************')
print('11. Compute future value of annuity due: FVdue_N = A * (((1 + r)^N - 1) / r) * (1 + r)')
print('12. Compute present value of annuity due: PV = FVdue_N / (1 + r)^N')
print('13. Compute payment amount of annuity due: A = FVdue_N / ((((1 + r)^N - 1) / r) * (1 + r))')
print('14. Compute present value of annuity due (one formula): PVdue_N = A * ((1 + r)^N - 1) / (r * (1 + r)^(N-1))')
print('************************************* ANNUITY IN PERPETUITY **************************************')
print('15. Annuity in Perpetuity: PVperp_N = A/r')
selection = int(input())
if (selection == 1):
    PV = float(input('present value (PV): '))
    r = float(input('rate (r): '))
    N = float(input('number of periods (N): '))
    FV_N = PV * (1 + r) ** N
    print('FV_N = ' + str(FV_N))
elif (selection == 2):
    FV = float(input('final value (FV): '))
    r = float(input('rate (r): '))
    N = float(input('number of periods (N): '))
    PV = FV / (1 + r) ** N
    print('PV = ' + str(PV))
elif (selection == 3):
    PV = float(input('present value (PV): '))
    FV = float(input('future value (FV): '))
    N = float(input('number of periods (N): '))
    r = ((FV / PV) ** (1.0/N)) - 1.0
    print('r = ' + str(r))
elif (selection == 4):
    PV = float(input('present value (PV): '))
    r = float(input('rate (r): '))
    t = float(input('time (t): '))
    FV = PV * math.exp(r * t)
    print('FV = ' + str(FV))
elif (selection == 5):
    r_s = float(input('stated rate (r_s): '))
    EAR = math.exp(r_s) - 1
    print('EAR = ' + str(EAR))
elif (selection == 6):
    PV = float(input('present value (PV): '))
    r = float(input('rate (r): '))
    FV = float(input('future value (FV): '))
    N = math.log(FV / PV) / math.log(1+r)
    print('N = ' + str(N))
elif (selection == 7):
    # future value of ordinary annuity
    A = float(input('annuity payment (A): '))
    r = float(input('rate (r): '))
    N = float(input('number of periods (N): '))
    FV_N = (A/r) * ((1 + r) ** N - 1)
    print('FV_N = ' + str(FV_N))
elif (selection == 8):
    # annuity payment necessary to reach some target
    # A = (FV_N * r) / ((1 + r)^N - 1)
    FV_N = float(input('future value (FV_N): '))
    r = float(input('rate (r): '))
    N = float(input('number of periods (N): '))
    A = (FV_N * r) / ((1 + r) ** N - 1)
    print('A = ' + str(A))
elif (selection == 9):
    # present value of ordinary annuity
    # PV = FV_N / (1+r)^N
    FV_N = float(input('future value (FV_N): '))
    r = float(input('rate (r): '))
    N = float(input('number of periods (N): '))
    #remming this (from 8), but it's probably useful!
    A = (FV_N * r) / ((1 + r) ** N - 1)
    PV = FV_N / (1+r)**N
    print('A = ' + str(A))
    print('PV = ' + str(PV))
elif (selection == 10):
    # present value of ordinary annuity (one formula)
    # PVord_N = A * ((1+r)^N - 1) / (r * (1 + r)^N)
    A = float(input('annuity payment (A): '))
    r = float(input('rate (r): '))
    N = float(input('number of periods (N): '))
    PVord_N = A * ((1+r)**N - 1) / (r * (1 + r)**N)
    print('PVord_N = ' + str(PVord_N))
elif (selection == 11):
    # future value of annuity due
    # FVdue_N = A * (((1 + r)^N - 1) / r) * (1 + r)
    A = float(input('annuity payment (A): '))
    r = float(input('rate (r): '))
    N = float(input('number of periods (N): '))
    FVdue_N = A * (((1 + r)**N - 1) / r) * (1 + r)
    print('FVdue_N = ' + str(FVdue_N))
elif (selection == 12):
    # present value of annuity due
    # PV = FVdue_N / (1 + r)^N
    FVdue_N = float(input('future value of annuity due (FVdue_N): '))
    r = float(input('rate (r): '))
    N = float(input('number of periods (N): '))
    PV = FVdue_N / (1 + r)**N
    print('PV = ' + str(PV))
elif (selection == 13):
    # payment amount of annuity due
    #  A = FVdue_N / ((((1 + r)^N - 1) / r) * (1 + r))
    FVdue_N = float(input('future value of annuity due (FVdue_N): '))
    r = float(input('rate (r): '))
    N = float(input('number of periods (N): '))
    A = FVdue_N / ((((1 + r)**N - 1) / r) * (1 + r))
    print('A = ' + str(A))
elif (selection == 14):
    # present value of annuity due (one formula)
    # PVdue_N = A * ((1 + r)^N - 1) / (r * (1 + r)^(N-1))
    A = float(input('annuity payment (A): '))
    r = float(input('rate (r): '))
    N = float(input('number of periods (N): '))
    PVdue_N = A * ((1 + r)**N - 1) / (r * (1 + r)**(N-1))
    print('PVdue_N = ' + str(PVdue_N))
elif (selection == 15):
    # Annuity in Perpetuity
    # PVperp_N = A/r
    A = float(input('annuity payment (A): '))
    r = float(input('rate (r): '))
    PVperp_N = A/r
    print('PVperp_N = ' + str(PVperp_N))
else:
    print('Invalid selection!')
print('\n\n')
