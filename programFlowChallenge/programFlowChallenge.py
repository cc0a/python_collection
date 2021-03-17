ipAddress = input("Please enter an IP address: ")

segment = 1
segment_length = 0
char = ""

for char in ipAddress:
    if char == '.':  # loop STOPS at each period, SO, this goes segment-by-segment
        print("segment {} contains {} characters".format(segment, segment_length)) # pulls+prints values from each var
        segment += 1  # 1 segments total, starting at 1, note that unlike segment_length, this is not reset
        segment_length = 0  # sets segment length to 0 before counting chars in new segment
    else:  # if the character isn't a period, we iterate/count the number of characters in a segment
        segment_length += 1  # this is where the number of characters within a segment are counted


# unless the final character in the string was a . then we haven't printed the last segment
if char != '.':  # this kicks in after the third period, moves on to final character in 4th segment
    print("segment {} contains {} characters".format(segment, segment_length))
