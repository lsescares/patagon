import tensorflow as tf
from tensorflow.python.client import device_lib
print('scrip ejecutado desde nodo slave')
print(device_lib.list_local_devices())


#print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print(tf.config.list_physical_devices('GPU'))
tf.debugging.set_log_device_placement(True)

#a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
#b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
#c = tf.matmul(a, b)
#print(c)

'''
import tensorflow as tf
tf.debugging.set_log_device_placement(True)

try:
  # Specify an invalid GPU device
  with tf.device('/device:GPU:0'):
    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    c = tf.matmul(a, b)
except RuntimeError as e:
  print(e)
'''
#print las gpus que keras ve desde el entorno del contenedor
from keras import backend as k
k.tensorflow_backend.get_available_gpus()
print(k.tensorflow_backend.get_available_gpus())
'''
