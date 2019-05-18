# Search methods
import search

ab = search.GPSProblem('A', 'B'
                           , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.ordenar_path(ab).path())
print(search.ramificacion_y_acotacion_subestimacion(ab).path())

#https://uniwebsidad.com/libros/algoritmos-python/capitulo-7/ordenar-listas
#http://www.cs.us.es/~fsancho/?e=62

#Ana Cosas que no sirven
"""amplitud = search.ordenar_path(ab).path()
for e in amplitud:
    print(e.path_cost)"""

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
