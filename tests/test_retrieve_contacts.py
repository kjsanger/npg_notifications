import pytest

from npg_notify.db.mlwh import get_study_contacts, StudyNotFoundError


def test_retrieving_study_contacts(mlwh_test_session):
    with pytest.raises(
        StudyNotFoundError,
        match=r"Study with ID 666 is not found in mlwarehouse",
    ):
        get_study_contacts(mlwh_test_session, "666")

    for id in ["2", "5", "4"]:
        assert get_study_contacts(mlwh_test_session, id) == []

    users = ["owner", "user1", "user2", "user3"]
    assert get_study_contacts(mlwh_test_session, "3") == [
        f"{u}@sanger.ac.uk" for u in users
    ]
