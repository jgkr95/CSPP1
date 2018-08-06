"""Credit card scam"""
def paying_debt_offinayear(balance, a_i_r, monthlypaymentrate):
    """This is function"""
    temp_p = balance
    i_i = 12
    while i_i >= 1:
        m_i_r = a_i_r / 12.0
        m_m_p = monthlypaymentrate * temp_p
        m_u_b = temp_p - m_m_p
        u_b_e_m = m_u_b + (m_u_b * m_i_r)
        temp_p = u_b_e_m
        i_i -= 1
    return round(temp_p, 2)
def main():
    """This is main method"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance:", paying_debt_offinayear(data[0], data[1], data[2]))
if __name__ == "__main__":
    main()
