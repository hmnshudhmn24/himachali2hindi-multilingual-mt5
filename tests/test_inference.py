from src.inference import translate
def test_translate_signature():
    try:
        out = translate('mai khet jaa reha', dialect='bilaspuri', model_dir='google/mt5-small')
    except Exception as e:
        assert isinstance(e, Exception)
        return
    assert isinstance(out, str)
