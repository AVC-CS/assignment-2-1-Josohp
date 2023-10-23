def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    mnum = int(input('enter number of male students: '))
    fnum = int(input('enter number of female students: '))
    total = mnum + fnum
    m_perc = mnum / total * 100
    f_perc = fnum / total * 100
    print (f'the percantage of male students is {m_perc:.2f}')
    print (f'the percantage of female students is {f_perc:.2f}')

    

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
