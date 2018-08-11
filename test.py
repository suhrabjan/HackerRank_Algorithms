from BulkImageResizer.BulkImageResizer import BulkImageResizer

sourcePath = '/Users/SK/Desktop/sourceFolder/'
exportPath = '/Users/SK/Desktop/newFolder/'

test1 = BulkImageResizer(sourcePath, exportPath)

test1.imageResize(600, 400, aspectRatio=True)
