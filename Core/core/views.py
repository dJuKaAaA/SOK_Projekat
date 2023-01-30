from django.shortcuts import redirect, render
from django.apps.registry import apps
import pkg_resources


def get_fs(request):
  path = request.GET.get("path")
  fsp = apps.get_app_config('core').loaded_plugins["fsp_plugin"]
  graph = fsp.load(path)
  apps.get_app_config('core').graph = graph
  return redirect("/")

def search(request):
  term = request.GET.get("term")
  graph = apps.get_app_config('core').graph
  searched_graph = graph.search(term)
  apps.get_app_config('core').graph = searched_graph
  return redirect("/")

def filter(request):
  query = request.GET.get("query")
  graph = apps.get_app_config('core').graph
  filtered_graph = graph.filter(query)
  apps.get_app_config('core').graph = filtered_graph
  return redirect("/")


def index(request):
  graph = apps.get_app_config('core').graph
  view_type = apps.get_app_config('core').view
  plugins = apps.get_app_config('core').loaded_plugins

  context = {
    "title": "Index",
    "code": ""
  }

  for plugin in plugins:
    context[plugin] = plugins[plugin]

  if graph is None or view_type is None:
    return render(request, "index.html", context)


  return render(request, "index.html", context)