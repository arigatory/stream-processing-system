from utils.json_handler import JsonHandler


class UserBlocker:
    def __init__(self):
        self.blocked_users = JsonHandler("blocked_users.json")

    def block_user(self, blocker, blocked):
        if blocker not in self.blocked_users.data:
            self.blocked_users.data[blocker] = []
        self.blocked_users.data[blocker].append(blocked)
        self.blocked_users.save()

    def is_blocked(self, sender, recipient):
        return (
            recipient in self.blocked_users.data
            and sender in self.blocked_users.data[recipient]
        )
