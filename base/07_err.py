def nacti_cislo():
    """ error handling of input """
    while True:
        odpoved = input('Zadej číslo: ')
        num = 0
        try:
            num = int(odpoved)
            # NOTE: if we had return int(odpoved), with some other return in the except block,
            # it would catch to the except block in case of error.. BUT else & finally would be unreachable!
            # obviously, duh.. But I spent a good half an hour or so debugging this xD
        except ValueError:
            print('value error')
            # rethrow the error:
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
