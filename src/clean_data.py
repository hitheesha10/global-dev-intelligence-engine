from .load_data import load_raw_data, prepare_all_data

def build_clean_dataset(pop_path, fert_path, life_path, meta_path):
    pop, fert, life, meta = load_raw_data(pop_path, fert_path, life_path, meta_path)
    df = prepare_all_data(pop, fert, life, meta)
    return df