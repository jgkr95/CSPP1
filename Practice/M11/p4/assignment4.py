'''We are now ready to begin writing the code that interacts with the player.
 We'll be implementing the playHand function.
This function allows the user to play out a single hand. First, though,
you'll need to implement the helper calculateHandlen function,
 which can be done in under five lines of code.'''
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    hand_length = 0
    for iterate in hand:
        hand_length += hand[iterate]
    return hand_length
def main():
    '''This is main functoin '''
    n_n = input()
    adict_ = {}
    for i_i in range(int(n_n)):
        data_ = input()
        l_l = data_.split()
        adict_[l_l[0]] = int(l_l[1])
        i_i = i_i
    print(calculate_handlen(adict_))
if __name__ == "__main__":
    main()
