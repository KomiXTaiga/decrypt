def decrypt_str(source, slug, s):
    """
    Given source and slug lists and encrypted string s,
    return the decrypted form of s.
    >>> z_slug = compute_slug('z')
    >>> decrypt_str(ALPHABET, z_slug, 'Zmc khjd z sgtmcdqanks gd ezkkr.\\n')
    'And like a thunderbolt he falls.\\n'
    """
    result_ch = ''
    for ch in s:
        if ch.isupper():  # if i is uppercase
            ch = ch.lower()  # makes each character lwoercase, not mutable
            if ch.isalpha():  # if the character in source is a letter
                slug_pos = slug.index(ch)  # finds index of the character in the slug
                e_char = source[slug_pos]  # returns source character at slug position
                e_char = e_char.upper()  # not mutable, replace w new version of itself
                result_ch += e_char

        elif ch.islower():  # if i is lowercase
            if ch.isalpha():  # if the character in source is a letter
                slug_pos = slug.index(ch)  # finds index of the source character
                e_char = source[slug_pos]  # returns slug character at ch_index
                result_ch += e_char  # appends the encrypted letter
        else:
            result_ch += ch
    return result_ch
