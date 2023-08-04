import pytest
from pytest_github_actions.person import Person


@pytest.fixture()
# fixture decorator allows to instantiate an object only once
def person():
    return Person("Luis Plancarte", 26, jobs=["Software Engineer"])


def test_init(person: Person):
    assert person.name == "Luis Plancarte"
    assert person.age == 26
    assert person.jobs == ["Software Engineer"]


def test_forename(person: Person):
    assert person.forename == "Luis"


def test_surname(person: Person):
    assert person.surname == "Plancarte"
