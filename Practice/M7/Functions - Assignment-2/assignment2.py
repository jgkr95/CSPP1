'''Credit card interest scam         '''
def payingdebtoffinayear(balance_, annualinterest_rate):
    '''This is function'''
    if balance_ < 0:
        return 0
    paid_ = 10
    while True:
        time_ = 0
        bala_ = balance_
        while time_ != 12:
            unpaidbal_ = bala_ - paid_
            bala_ = unpaidbal_ + (unpaidbal_*annualinterest_rate/12)
            time_ += 1
        if bala_ <= 0.5:
            break
        paid_ = paid_ + 10
    return paid_
def main():
    '''This is main methid'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", payingdebtoffinayear(data[0], data[1]))
if __name__ == "__main__":
    main()
