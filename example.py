import numpy as np
from sampling_points import sample_points_inside_mesh, sample_points_on_mesh

nr_points = 100000 # number of points to sample

stl_file = "knot_mesh.stl"


# Sample points inside the mesh
points_inside = sample_points_inside_mesh(stl_file, nr_points, save_to_file=True, save_file_name="points_inside.txt")
# Sample points on the mesh
points_on_boundary = sample_points_on_mesh(stl_file, nr_points, save_to_file=True, save_file_name="points_on_boundary.txt")
