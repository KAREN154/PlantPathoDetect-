# data_preprocessing.py
import numpy as np
from sklearn.preprocessing import LabelEncoder
# from keras.utils import to_categorical
import tensorflow as tf

# from tensorflow.keras.utils import to_categoricalpip

class DataPreprocessor:
    def __init__(self):
        self.label_encoder = LabelEncoder()
        
    def preprocess_data(self, train_images, train_labels, test_images, test_labels, val_images, val_labels):
        """
        Preprocess the image data and labels for training
        
        Parameters:
        -----------
        train_images, test_images, val_images: numpy arrays of image data
        train_labels, test_labels, val_labels: numpy arrays of corresponding labels
        
        Returns:
        --------
        Preprocessed images and labels for train, test, and validation sets
        """
        # 1. Process Labels
        processed_labels = self._process_labels(train_labels, test_labels, val_labels)
        
        # 2. Process Images
        processed_images = self._process_images(train_images, test_images, val_images)
        
        return processed_images, processed_labels
    
    def _process_labels(self, train_labels, test_labels, val_labels):
        """Process and encode labels"""
        # Encode labels to numerical format
        train_labels_encoded = self.label_encoder.fit_transform(train_labels)
        test_labels_encoded = self.label_encoder.transform(test_labels)
        val_labels_encoded = self.label_encoder.transform(val_labels)
        
        # Get number of classes
        self.num_classes = len(np.unique(train_labels))
        print(f"Number of classes: {self.num_classes}")
        
        # Convert to categorical
        # train_labels_cat = to_categorical(train_labels_encoded, self.num_classes)
        # test_labels_cat = to_categorical(test_labels_encoded, self.num_classes)
        # val_labels_cat = to_categorical(val_labels_encoded, self.num_classes)

        train_labels_cat = tf.one_hot(train_labels_encoded, depth=self.num_classes)
        test_labels_cat = tf.one_hot(test_labels_encoded, depth=self.num_classes)
        val_labels_cat = tf.one_hot(val_labels_encoded, depth=self.num_classes)
                
        # Print class distribution
        self._print_class_distribution(train_labels, "Training")
        self._print_class_distribution(test_labels, "Testing")
        self._print_class_distribution(val_labels, "Validation")
        
        return {
            'train': train_labels_cat,
            'test': test_labels_cat,
            'val': val_labels_cat
        }
    
    def _process_images(self, train_images, test_images, val_images):
        """Process and normalize images"""
        # Normalize pixel values to range [0,1]
        train_images_norm = train_images / 255.0
        test_images_norm = test_images / 255.0
        val_images_norm = val_images / 255.0
        
        # Print image statistics
        self._print_image_statistics(train_images_norm, "Training")
        self._print_image_statistics(test_images_norm, "Testing")
        self._print_image_statistics(val_images_norm, "Validation")
        
        return {
            'train': train_images_norm,
            'test': test_images_norm,
            'val': val_images_norm
        }
    
    def _print_class_distribution(self, labels, dataset_name):
        """Print distribution of classes in the dataset"""
        unique, counts = np.unique(labels, return_counts=True)
        print(f"\n{dataset_name} Set Class Distribution:")
        for class_name, count in zip(unique, counts):
            print(f"{class_name}: {count} images")
    
    def _print_image_statistics(self, images, dataset_name):
        """Print basic statistics about the image data"""
        print(f"\n{dataset_name} Set Image Statistics:")
        print(f"Shape: {images.shape}")
        print(f"Min pixel value: {images.min():.3f}")
        print(f"Max pixel value: {images.max():.3f}")
        print(f"Mean pixel value: {images.mean():.3f}")
        print(f"Std pixel value: {images.std():.3f}")

 
# if __name__ == "__main__":
#     # Initialize preprocessor
#     preprocessor = DataPreprocessor()
    
#     # Process the data
#     processed_images, processed_labels = preprocessor.preprocess_data(
#         train_images, train_labels,
#         test_images, test_labels,
#         val_images, val_labels
#     )