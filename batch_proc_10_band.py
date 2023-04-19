#from ipywidgets import FloatProgress, Layout
#from IPython.display import display
import micasense.imageset as imageset
import micasense.capture as capture
import micasense.metadata as metadata
import os, glob
import multiprocessing

panelNames = None
useDLS = True

exiftoolPath = None
if os.name == 'nt':
    exiftoolPath = os.environ.get('exiftoolpath')

# imagePath = os.path.expanduser(os.path.join('~','Downloads','DualCam-Farm','farm_only'))
# panelNames = glob.glob(os.path.join(imagePath,'IMG_0002_*.tif'))

imagePath = os.path.join('/media', 'davidjm', 'Disco_Compartido', 'david', 'datasets', 'ProyectoAgro', 'AGUACATE23noviembre', 'test')
panelNames = glob.glob(os.path.join(imagePath,'IMG_0001_*.tif'))

for name in panelNames:
    #print(name)
    # get image metadata
    ImageMeta = metadata.Metadata(name, exiftoolPath=exiftoolPath)
    print(f'Capture ID: {ImageMeta.get_item("XMP:CaptureId")}')

outputPath = os.path.join(imagePath,'stacks')
thumbnailPath = os.path.join(outputPath, 'thumbnails')

overwrite = False # Set to False to continue interrupted processing
generateThumbnails = True

# Allow this code to align both radiance and reflectance images; bu excluding
# a definition for panelNames above, radiance images will be used
# For panel images, efforts will be made to automatically extract the panel information
# but if the panel/firmware is before Altum 1.3.5, RedEdge 5.1.7 the panel reflectance
# will need to be set in the panel_reflectance_by_band variable.
# Note: radiance images will not be used to properly create NDVI/NDRE images below.
if panelNames is not None:
    panelCap = capture.Capture.from_filelist(panelNames)
else:
    panelCap = None

if panelCap is not None:
    if panelCap.panel_albedo() is not None:
        panel_reflectance_by_band = panelCap.panel_albedo()
    else:
        panel_reflectance_by_band = [0.65]*len(panelCap.images) #inexact, but quick
    print(panel_reflectance_by_band)
    panel_irradiance = panelCap.panel_irradiance(panel_reflectance_by_band)    
    img_type = "reflectance"
else:
    if useDLS:
        img_type='reflectance'
    else:
        img_type = "radiance"




