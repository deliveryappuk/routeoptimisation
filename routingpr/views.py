from django.shortcuts import render
from .optimize_routes import OptimizeRoutes
def my_view(request):
    optimize_routes = OptimizeRoutes()
    json_data = optimize_routes.get_json_data()
    json_optimized=optimize_routes.optimize_stops(json_data)
    return render(request, 'request.html', {'jsonData': json_data,'jsonResponse': json_optimized})
def index(request):
    return render(request, 'index.html')
