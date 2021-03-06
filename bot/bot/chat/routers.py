from .models import *


class NotifyCategoryRouter(NotifyCategory):
    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, model, **hints):
        return 'default'

    class Meta:
        managed = False


class ChatRouter(Chat):
    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, model, **hints):
        return 'default'

    class Meta:
        managed = False


class ChatUpdateRouter(ChatUpdate):
    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, model, **hints):
        return 'default'

    class Meta:
        managed = False


class ChatContextRouter(Context):
    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, model, **hints):
        return 'default'

    class Meta:
        managed = False


class ChatCommandRouter(Command):
    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, model, **hints):
        return 'default'

    class Meta:
        managed = False
