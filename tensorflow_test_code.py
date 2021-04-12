import tensorflow as tf 

print("[INFO] Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

print('Is build with cuda available ?')
print(f'[INFO] {tf.test.is_built_with_cuda()}')

print('Is gpu available ?')
print(f'[INFO] {tf.test.is_gpu_avaiable()}')

