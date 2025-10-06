# Simulasikan fungsionalitas utama yang akan diuji
def some_data_preprocessing_function(data):
    """Fungsi dummy untuk diuji."""
    if data:
        return True
    return False

# Unit Test
def test_preprocessing_success():
    """Memastikan fungsi preprocessing mengembalikan True untuk data yang ada."""
    assert some_data_preprocessing_function([1, 2, 3]) == True

def test_preprocessing_failure():
    """Memastikan fungsi preprocessing mengembalikan False untuk data kosong."""
    assert some_data_preprocessing_function([]) == False