def test_model_properties(baker):
    model = baker.make('example_app.ExampleModel', name='Ivan')

    assert model.id > 0
    assert model.name == 'Ivan'


def test_model_str(factory):
    model = factory.example_model()

    assert model.name == str(model)
