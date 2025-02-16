from app.processors.user_blocker import UserBlocker


def test_block_user():
    blocker = UserBlocker()
    blocker.block_user("user1", "user2")
    assert blocker.is_blocked("user2", "user1")


def test_is_blocked():
    blocker = UserBlocker()
    blocker.block_user("user1", "user2")
    assert blocker.is_blocked("user2", "user1")
    assert not blocker.is_blocked("user1", "user2")


def test_multiple_blocks():
    blocker = UserBlocker()
    blocker.block_user("user1", "user2")
    blocker.block_user("user1", "user3")
    assert blocker.is_blocked("user2", "user1")
    assert blocker.is_blocked("user3", "user1")
    assert not blocker.is_blocked("user2", "user3")
