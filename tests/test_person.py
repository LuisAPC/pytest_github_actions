from pytest_github_actions.person import Person


def test_init():
    person = Person("Luis Plancarte", 26, jobs=["Software Engineer"])
    assert person.name == "Luis Plancarte"
    assert person.age == 26
    assert person.jobs == ["Software Engineer"]
