# program for generated images in a folder
from keras.preprocessing.image import ImageDataGenerator
from skimage import io

#creating an ImageDataGenerator instance by initiating some parameters
datagen = ImageDataGenerator(
        rotation_range=30,     #random rotation between 0 and 30
        width_shift_range=0.2,   
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')    #constant, reflect, wrap
 

#Directory Structure->
#    MAIN_DIR/
#      -IMAGES_1_DIR/
#      -IMAGES_2_DIR/
#      -IMAGES_3_DIR/
#      -AUGMENTED_DIR/

#number of generated images will be i=20 for each images in each directory into 1 single directory(AUGMENTED_DIR)
i = 0
for batch in datagen.flow_from_directory(directory='MAIN_DIR/', 
                                         batch_size=16,  
                                         target_size=(800, 600),
                                         color_mode="rgb",
                                         save_to_dir='MAIN_DIR/AUGMENTED_DIR', 
                                         save_prefix='aug', 
                                         save_format='png'):
    i += 1
    if i > 20:
        break
