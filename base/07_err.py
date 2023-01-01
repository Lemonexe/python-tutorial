def nacti_cislo():
    """ error handling of input """
    while True:
        odpoved = input('Zadej číslo: ')
        num = 0
        try:
            num = int(odpoved)
        except ValueError:
            print('value error')
            # raise ValueError(f'input "{odpoved}" is not numerical')

        except Exception: # will catch all errors
            # there is a hierarchy tree of Errors
            print('yeah that was some kind of an erorr')
            # the first block that can handle the error is used, otherwise error bubbles on

        else:
            print('there was no error :)')
        
        finally:
            print(f'finally, {num} ')
            return num

nacti_cislo()
