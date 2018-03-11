from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os

file_path = '/Users/xiejiacheng/coding/alldata/test/10'
save_dir = '/Users/xiejiacheng/coding/Image_augmentation/test/10'
save_format = 'jpg'
def amplify(file_dir, save_dir, save_prefix, save_format = 'jpg'):
    datagen = ImageDataGenerator(
            rotation_range=100,
            width_shift_range=0.05,
            height_shift_range=0.05,
            shear_range=0.02,
            zoom_range=0.02,
            horizontal_flip=True,
            fill_mode='nearest')

    img = load_img(file_dir)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    # the .flow() command below generates batches of randomly transformed images
    # and saves the results to the `preview/` directory
    i = 0
    for batch in datagen.flow(x, batch_size=1,
        save_to_dir=save_dir, save_prefix=save_prefix, save_format=save_format):
        i += 1
        if i > 20:
            break  # otherwise the generator would loop indefinitely


def list_images(file_path, save_dir, save_format='jpg'):
    for parent_dir, dir_names, img_names in os.walk(file_path):
        print(file_path, parent_dir, dir_names)
        if(file_path == parent_dir):
            for img_name in img_names:
                print(img_name)
                amplify('{}/{}'.format(parent_dir, img_name), save_dir, img_name.split('.')[0])


if __name__ == '__main__':
    list_images(file_path, save_dir, save_format)
