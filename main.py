#CS454 Final Project


def flip_bits(binary_string):
    if(len(binary_string) == 1):
        if binary_string == "0":
            return "1"
        else:
            return "0"

    noflip = '0' * len(binary_string)
    flip = '1' + '0' * (len(binary_string) - 1)

    noflip_switches = list(noflip)
    flip_switches = list(flip)

    noflip_bulbs = list(binary_string)
    flip_bulbs = list(binary_string)

    #print("Before switch:",flip_bulbs)

    #first index switched
    if flip_bulbs[0] == '0':
        flip_bulbs[0] = '1'
    else:
        flip_bulbs[0] = '0'

    #second index switched
    if flip_bulbs[1] == '0':
        flip_bulbs[1] = '1'
    else:
        flip_bulbs[1] = '0'

    #print("After switch:", flip_bulbs)


    # iterate over flip bulb set
    for i in range(1, len(flip_bulbs)):

        # if prev bit is 0
        if flip_bulbs[i - 1] == '0':
            flip_switches[i] = '1'
            flip_bulbs[i - 1] = '1'
            if flip_bulbs[i] == '0':
                flip_bulbs[i] = '1'
            else:
                flip_bulbs[i] = '0'
            # if not at the end @@@
            if i < len(flip_bulbs)-1:
                if flip_bulbs[i+1] == '0':
                    flip_bulbs[i+1] = '1'
                else:
                    flip_bulbs[i+1] = '0'

    for i in range(1, len(noflip_bulbs)):
        #print(noflip_bulbs)

        # if prev bit is 0
        if noflip_bulbs[i - 1] == '0':
            noflip_switches[i] = '1'
            noflip_bulbs[i - 1] = '1'
            if noflip_bulbs[i] == '0':
                noflip_bulbs[i] = '1'
            else:
                noflip_bulbs[i] = '0'
            # if not at the end @@@
            if i < len(noflip_bulbs) - 1:
                if noflip_bulbs[i + 1] == '0':
                    noflip_bulbs[i + 1] = '1'
                else:
                    noflip_bulbs[i + 1] = '0'






    # convert the list back to a string
    flip_bulbs_result = ''.join(flip_bulbs)
    noflip_bulbs_result = ''.join(noflip_bulbs)

    #print("flip switches", flip_switches)
    #print("noflip switches", noflip_switches)


    if noflip_bulbs_result[len(noflip_bulbs_result)-1] == '1':
        print("Bulbs result:", noflip_bulbs_result)
        return ''.join(noflip_switches)
    if flip_bulbs_result[len(flip_bulbs_result)-1] == '1':
        print("Bulbs result:", flip_bulbs_result)
        return ''.join(flip_switches)
    else:
        return "Does not exist"

    #return flip_bulbs_result, noflip_bulbs_result

if __name__ == '__main__':

    test_string = '11'
    print("Switches pressed:", flip_bits(test_string))




