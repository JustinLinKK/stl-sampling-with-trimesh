<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Stl Scan" />

  &#xa0;

  <!-- <a href="https://stlscan.netlify.app">Demo</a> -->
</div>

<h1 align="center">Stl Scan with Trimesh and PyTorch</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/JustinLinKK/stl-sampling-with-trimesh?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/JustinLinKK/stl-sampling-with-trimesh?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/JustinLinKK/stl-sampling-with-trimesh?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/JustinLinKK/stl-sampling-with-trimesh?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/stl-sampling-with-trimesh?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/stl-sampling-with-trimesh?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/stl-sampling-with-trimesh?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Stl Scan 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-example result">Example Result</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/JustinLinKK" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

This is a python library used for the 3D points sampling form the stl files. Aimed for the fast 3D model dataset creation. The newest function please visit the example.py

## :sparkles: Features ##

:heavy_check_mark: CUDA boost for precise interior stl points sampling;\
:heavy_check_mark: Output the points as numpy array or files;

## :rocket: Technologies ##

The following tools were used in this project:

- [pytorch](https://torch.org/)
- [Trimesh](https://trimsh.org/trimesh.html)


## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python 3.10 +](https://www.python.org/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/JustinLinKK/stl-sampling-with-trimesh

# Access
$ cd stl-sampling-with-trimesh

# Install dependencies
$ pip install -r requirements.txt
# Install pytorch with CUDA (CUDA is optional)
$ pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
$ pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Run the project
$ python example.py

```

## :checkered_flag: Example Result ##
<p align="center">
 <img text="Example Result of boundary sampling" src="https://github.com/JustinLinKK/stl-sampling-with-trimesh/blob/main/Boundary_sampling.png">
 <img text="Example Result of interior sampling" src="https://github.com/JustinLinKK/stl-sampling-with-trimesh/blob/main/Interior_Sampling.png">
</p>


## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/JustinLinKK" target="_blank">JustinLinKK</a>

&#xa0;

<a href="#top">Back to top</a>
