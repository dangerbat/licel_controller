from unittest import mock

from licel_controller.interface import Controller


def test_licel_controller(event_loop, monkeypatch):
    with mock.patch("multiprocessing.pool.Pool.map") as mocked_result:
        mocked_result.return_value = ["Command executed!", ]
        c = Controller()
        c.select(1, 2, 3)
        assert c.run() == ["Command executed!", ]
