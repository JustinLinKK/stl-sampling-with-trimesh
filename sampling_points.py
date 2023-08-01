import numpy as np
import trimesh
import torch
from trimesh import sample

def sample_points_inside_mesh(stl_file, num_points, save_to_file=False, save_file_name="points_inside.txt"):
    '''
    Sample points inside a mesh
    Input:
        stl_file: the stl file of the mesh
        num_points: the number of points to sample
        save_to_file: whether to save the sampled points to a file
        save_file_name: the name of the file to save the sampled points
    Output:
        sample: the sampled points inside the mesh as a numpy array with shape (n, 3)
    '''
    # Load the STL file using trimesh
    mesh = trimesh.load_mesh(stl_file)
    
    # Generate random points within the bounding box of the mesh
    bbox = mesh.bounds
    
    # Convert the bounding box to a torch tensor
    # Check if cuda is available
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    random_points = torch.rand(num_points, 3).to(torch.float32).to(device)
    random_points[:, 0] = bbox[0, 0] + random_points[:, 0] * (bbox[1, 0] - bbox[0, 0])
    random_points[:, 1] = bbox[0, 1] + random_points[:, 1] * (bbox[1, 1] - bbox[0, 1])
    random_points[:, 2] = bbox[0, 2] + random_points[:, 2] * (bbox[1, 2] - bbox[0, 2])
    
    # Check if each point is inside the mesh and keep only those points
    points_inside = []
    for point in random_points:
        if mesh.contains([point.cpu().numpy()]):
            points_inside.append(point)
                
                
    sample = torch.stack(points_inside)
    sample = sample.cpu().numpy()
    # Add the "x,y,z" header to the file
    # Saparate the xyz coordinates by a comma
    if save_to_file:
        np.savetxt(save_file_name, sample, header="x,y,z", comments="", delimiter=",")
    
    # Return the points inside the mesh and add the "x,y,z" header to the numpy array
    # The points are returned as a numpy array with shape (n, 3)
    return sample

        
def sample_points_on_mesh(stl_file, num_points, save_to_file=False, save_file_name="points_on_boundary.txt"):
    '''
    Sample points on the boundary of a mesh
    Input:
        stl_file: the stl file of the mesh
        num_points: the number of points to sample
        save_to_file: whether to save the sampled points to a file
        save_file_name: the name of the file to save the sampled points
    Output:
        points: the sampled points on the boundary of the mesh as a numpy array with shape (n, 3)
    '''
    
    # Load the STL file using trimesh
    mesh = trimesh.load_mesh(stl_file)
    
    # Sample points on the mesh surface
    points, _ = sample.sample_surface(mesh, num_points)
    
    # Convert the points to a numpy array
    # Add a "x,y,z" header to the file
    # Separate the xyz coordinates by a comma
    samples = np.array(points)
    if save_to_file:
        np.savetxt(save_file_name, samples, header="x,y,z", comments="", delimiter=",")
    
    return points



# Example usage
# stl_file = "knot_mesh.stl"
# num_points = 50000
# sampled_points = sample_points_on_mesh(stl_file, num_points, save_to_file=True, save_file_name="points_boundary.txt")