def samitleri_al(cumle):
    samitler = set()
    for harf in cumle:
        if harf.lower() in 'aeiou ':
            continue
        samitler.add(harf.lower())
    return samitler
