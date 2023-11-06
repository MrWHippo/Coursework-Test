def check_straight(hand, count=1, prev=None):
    if hand == []:
        return False
    
    if count == 5:
        return True

    if prev is None or hand[0] == prev + 1:
        return check_straight(hand[1:], count + 1, hand[0])
    else:
        return check_straight(hand[1:], 1, hand[0])

# Example usage:
sorted_list = [1, 2, 3, 5, 6, 7, 8]
result = check_straight(sorted_list)
print(result)  # True

sorted_list = [1, 2, 3, 5, 6, 8, 9]
result = check_straight(sorted_list)
print(result)  # False

