from django.apps import AppConfig
import pkg_resources


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    loaded_plugins = []

    def ready(self):
        # self.loaded_plugins += load_plugins()
        # TODO: load plugins here :)
        pass


def load_plugins(group):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=group):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        print(p)
        plugin = p()
        plugins.append(plugin)
    return plugins
