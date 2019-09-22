class AntiSpamInvites(object):
    def __init__(self, config):
        self._block_invites_from = config["blocked_homeservers"]

    def check_event_for_spam(self, event):
        return False # not spam

    def user_may_invite(self, inviter_user_id, invitee_user_id, room_id):
        _, inviter_user_hs = inviter_user_id
        return inviter_user_hs not in self._block_invites_from

    def user_may_create_room(self, user_id):
        return True # allowed

    def user_may_create_room_alias(self, user_id, room_alias):
        return True # allowed

    def user_may_publish_room(self, user_id, room_id):
        return True # allowed

    @staticmethod
    def parse_config(config):
        config["blocked_homeservers"] = {hs: True for hs in config.get("blocked_homeservers", [])}
        return config # no parsing needed
