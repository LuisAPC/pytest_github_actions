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


def test_no_surname(person: Person):
    person.name = "Luis"
    assert not person.surname


def test_celebrate_birthday(person: Person):
    person.celebrate_birthday()
    assert person.age == 27


def test_add_job(person: Person):
    person.add_job("Zookeper")
    assert person.jobs == ["Software Engineer", "Zookeper"]
