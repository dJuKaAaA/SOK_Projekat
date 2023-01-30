from django.apps import AppConfig
import pkg_resources


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    graph = None
    SIMPLE = "simple"
    COMPLEX = "complex"
    view = None
    loaded_plugins = {}

    def ready(self):
        fsp_plugins = load_plugins("fsp_plugin")
        svp_plugins = load_plugins("svp_plugin")
        cvp_plugins = load_plugins("cvp_plugin")
        twp_plugins = load_plugins("twp_plugin")
        self.loaded_plugins["fsp_plugin"] = fsp_plugins[0] if len(
            fsp_plugins) > 0 else None
        self.loaded_plugins["svp_plugin"] = svp_plugins[0] if len(
            svp_plugins) > 0 else None
        self.loaded_plugins["cvp_plugin"] = cvp_plugins[0] if len(
            cvp_plugins) > 0 else None
        self.loaded_plugins["twp_plugin"] = twp_plugins[0] if len(
            twp_plugins) > 0 else None


def load_plugins(group):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=group):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        print(p)
        plugin = p()
        plugins.append(plugin)
    return plugins
