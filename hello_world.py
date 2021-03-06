try:
    import unzip_requirements
except ImportError:
    pass

import numpy as np
import tensorflow as tf


def handler(event, context):
    helloworld = tf.constant("hello, TensorFlow")
    return {'Tensor': helloworld.numpy().decode("utf-8"), 'Value': str(np.shape([1, 2, 3, 4]))}
