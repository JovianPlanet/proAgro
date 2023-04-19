import micasense.metadata as metadata
import micasense.image as image
import os, glob
import multiprocessing
import exiftool

panelNames = None
useDLS = True

exiftoolPath = None
if os.name == 'nt':
    exiftoolPath = os.environ.get('exiftoolpath')

bluePath = os.path.join('/media', 
                         'davidjm', 
                         'Disco_Compartido', 
                         'david', 
                         'datasets', 
                         'ProyectoAgro', 
                         'AGUACATE23noviembre', 
                         'BLUE', 
                         '000')

redPath = os.path.join('/media', 
                         'davidjm', 
                         'Disco_Compartido', 
                         'david', 
                         'datasets', 
                         'ProyectoAgro', 
                         'AGUACATE23noviembre', 
                         'RED', 
                         '000')

blueNames = glob.glob(os.path.join(bluePath,'IMG_0001_*.tif'))
redNames = glob.glob(os.path.join(redPath,'IMG_0001_*.tif'))
single = '/media/davidjm/Disco_Compartido/david/datasets/ProyectoAgro/AGUACATE23noviembre/test/IMG_0001_1.tif'

def print_captureIDs():
    for i in range(len(blueNames)):
        print(blueNames[i][-15:])
        # get image metadata
        blueMeta = metadata.Metadata(blueNames[i], exiftoolPath=exiftoolPath)
        print(f'Capture ID: {blueMeta.get_item("XMP:CaptureId")}')

        print(redNames[i][-15:])
        # get image metadata
        redMeta = metadata.Metadata(redNames[i], exiftoolPath=exiftoolPath)
        print(f'Capture ID: {redMeta.get_item("XMP:CaptureId")}\n')

def compare_captureIDs():
    for i in range(len(blueNames)):
        blueMeta = metadata.Metadata(blueNames[i], exiftoolPath=exiftoolPath)
        for j in range(len(redNames)):
            redMeta = metadata.Metadata(redNames[i], exiftoolPath=exiftoolPath)
            if blueMeta.get_item("XMP:CaptureId")==redMeta.get_item("XMP:CaptureId"):
                print(f'BLUE {blueNames[i][-15:]} == RED {redNames[i][-15:]}\n')


def change_captureID(ref, targets):
    refMeta = metadata.Metadata(ref, exiftoolPath=exiftoolPath)
    
    for target in targets:
        img = image.Image(target)
        #img.meta.capture_id() = 'hola'
        targetMeta = metadata.Metadata(target, exiftoolPath=exiftoolPath)
        print(img.meta.capture_id())
        #targetMeta.get_item("XMP:CaptureId") = refMeta.get_item("XMP:CaptureId")




#print_captureIDs()
#compare_captureIDs()
#change_captureID(os.path.join(bluePath,'IMG_0001_1.tif'), redNames)


with exiftool.ExifTool(exiftoolPath) as et:
    m = et.get_metadata(single)
    print(f'{et.get_metadata(single)}')
    print(f'{m["XMP:CaptureId"]}')
    m["XMP:CaptureId"] = 'hola'
    print(f'Despues de modificar = {m["XMP:CaptureId"]}')
    et.execute("-XMP:CaptureId=hola", single)


# class Metadata(object):
#     ''' Container for Micasense image metadata'''
#     def __init__(self, filename, exiftoolPath=None, exiftool_obj=None):
#         if exiftool_obj is not None:
#             self.exif = exiftool_obj.get_metadata(filename)
#             return
#         if exiftoolPath is not None:
#             self.exiftoolPath = exiftoolPath
#         elif os.environ.get('exiftoolpath') is not None:
#             self.exiftoolPath = os.path.normpath(os.environ.get('exiftoolpath'))
#         else:
#             self.exiftoolPath = None
#         if not os.path.isfile(filename):
#             raise IOError("Input path is not a file")
#         with exiftool.ExifTool(self.exiftoolPath) as exift:
#             self.exif = exift.get_metadata(filename)

'''
import tifffile
#import imageio as io
#import numpy as np

tiff = tifffile.TiffFile(os.path.join(bluePath,'IMG_0001_1.tif'))
print(tiff.pages.pages.index())
#tiff.pages[0].tags['XResolution'].overwrite(tiff, (97321972, 392185))
'''