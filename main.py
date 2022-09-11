import pubchempy as pcp
import pandas as pd

COMPOUND_LIST = ["Adenosine", "Adenocard", "BG8967", "Bivalirudin", "BAYT006267", "diflucan", "ibrutinib", "PC-32765"]


def get_upper_name(input_name):
    compounds = pcp.get_compounds(input_name, namespace='name')

    if len(compounds):
        return compounds[0].synonyms[0].upper()
    else:
        raise ValueError(f'{input_name} not found')


def get_normed_names(input_names):
    normed_names = []

    for input_name in input_names:
        if not input_name:
            continue
        normed_names.append(get_upper_name(input_name))

    return pd.DataFrame({'org_form': input_names, 'normed_form': normed_names})


print(get_normed_names(COMPOUND_LIST))
