from twttr import convert_twttr


def main():
    test_twttr()

def test_twttr():
    try:
        assert convert_twttr("TOMORROW") == "tmttw"
        assert convert_twttr("TWitter") == "twttr"

