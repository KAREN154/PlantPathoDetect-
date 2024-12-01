import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy as np

IMG_SIZE = 180

# Sequential model for resizing and rescaling
resize_and_rescale = keras.Sequential([
    layers.Resizing(IMG_SIZE, IMG_SIZE),
    layers.Rescaling(1./255)
])

def augment_image(image, rotation_range=20, width_shift_range=0.2, height_shift_range=0.2,
                  horizontal_flip=True, vertical_flip=False, zoom_range=0.2,
                  brightness_range=[0.8, 1.2]):
    # Random rotation
    image = tf.image.rot90(image, k=np.random.randint(0, 4)) if rotation_range > 0 else image
    
    # Random width and height shift
    if width_shift_range or height_shift_range:
        image = tf.image.random_crop(
            image, 
            size=[int(image.shape[0] * (1 - height_shift_range)), int(image.shape[1] * (1 - width_shift_range)), 3]
        )
    
    # Random horizontal and vertical flip
    if horizontal_flip:
        image = tf.image.random_flip_left_right(image)
    if vertical_flip:
        image = tf.image.random_flip_up_down(image)

    # Random zoom
    if zoom_range:
        scales = [1.0 - zoom_range, 1.0 + zoom_range]
        scale = np.random.uniform(scales[0], scales[1])
        image = tf.image.central_crop(image, central_fraction=scale)
        image = tf.image.resize(image, [IMG_SIZE, IMG_SIZE])

    # Random brightness
    image = tf.image.random_brightness(image, max_delta=(brightness_range[1] - brightness_range[0]))

    # Fill mode (nearest neighbor)
    image = tf.clip_by_value(image, 0, 1)  # Ensure pixel values remain in [0, 1]

    return image

def preview_augmentations(image, num_augmentations=5):
    augmented_images = [augment_image(image) for _ in range(num_augmentations)]

    plt.figure(figsize=(2 * (num_augmentations + 1), 4))
    plt.subplot(1, num_augmentations + 1, 1)
    plt.imshow(image.numpy().astype("uint8"))
    plt.title("Original")
    plt.axis("off")

    for i, img in enumerate(augmented_images):
        plt.subplot(1, num_augmentations + 1, i + 2)
        plt.imshow(img.numpy().astype("uint8"))
        plt.title(f"Augmented {i + 1}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()

# # Example usage
# image = tf.io.read_file('path/to/image.jpg')  # Replace with your image path
# image = tf.image.decode_jpeg(image, channels=3)
# image = resize_and_rescale(image)

# preview_augmentations(image)
