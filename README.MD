# Image to Ascii Converter
Converts images to ascii characters.


## Requirements
- Install python3. Python 3.7 required.
- Optional: pipenv
    > pip install pipenv
- Or you can just install `pillow`.
    > pip install Pillow

## Usage
- At first, if you are using pipenv, automatically install dependencies using `pipenv install`. To install dependencies. Then run pipenv shell to activate venv.
- Put an image to be converted inside `image/` directory. We store the image inside a default directory to minimize path finding.
- On the terminal, run `python3 ascii-art.py --img {image name with extension}`. (e.g.) `python3 ascii-art.py --img cat.jpg`
