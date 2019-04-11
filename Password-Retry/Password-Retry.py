# Set your password here.
password = 'password'

# Password verification.
def TryPassword(InputPassword):
    if InputPassword == password:
        print('Password correct.')
        c = 1
        return c
    else:
        print('Password error.')
        c = 0
        return c

# Main program.
if __name__ == '__main__':
    count = 3
    c = 0
    while count > 0:
        if count > 1:
            print('You have ', count, 'more chance(s).')
            InputPassword = input('Please enter your password:')
            c = TryPassword(InputPassword)
            if c == 1:
                break
            else:
                count -= 1
        elif count == 1:
            print('You have ', count, 'more chance(s).')
            InputPassword = input('Please enter your password:')
            TryPassword(InputPassword)
            break