import tensorflow as tf
from tensorflow.python.platform import gfile

with tf.Session() as sess:
    model_filename = 'Saved_model/combined_model.pb'

    # 读取保存的模型文件，并将文件解析成对于的GraphDef Protocol Buffer
    '''
    def __init__(self, name, mode='r'):
        mode = mode.replace('b', '')
        super(FastGFile, self).__init__(name=name, mode=mode)
    这里的b没有作用
    '''
    with gfile.FastGFile(model_filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    result = tf.import_graph_def(graph_def, return_elements=["add:0"])
    print(sess.run(result))