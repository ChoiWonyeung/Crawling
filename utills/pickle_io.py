import pickle


def pickle_save(file, obj):
    with open(file, "wb") as f:
        pickle.dump(obj, f)


def pickle_load(file):
    with open(file, "rb") as f:
        obj = pickle.load(f)
        return obj
