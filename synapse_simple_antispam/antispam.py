class AntiSpamInvites(object):
    def __init__(self, config):
        self._block_invites_from = config["blocked_homeservers"]
        self._block_invites_to = config["blocked_channels"]

    def check_event_for_spam(self, event):
        return False # not spam

    def user_may_invite(self, inviter_user_id, invitee_user_id, room_id):
        _, inviter_user_hs = inviter_user_id
        return inviter_user_hs not in self._block_invites_from and room_id not in self._block_invites_to

    def user_may_create_room(self, user_id):
        return True # allowed

    def user_may_create_room_alias(self, user_id, room_alias):
        return True # allowed

    def user_may_publish_room(self, user_id, room_id):
        return True # allowed

    @staticmethod
    def parse_config(config):
        for block in ["blocked_homeservers", "blocked_channels"]:
            config[block] = {key: True for key in config.get(block, [])}
        return config # no parsing needed
