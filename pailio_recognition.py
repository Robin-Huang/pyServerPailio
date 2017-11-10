import tensorflow as tf

class PailioRecog(object):
    def __init__(self):
        self.graph_file = 'models/papilionidae_graph_4000.pb'
        self.label_file = 'models/papilionidae_chinese_labels.txt'

    def load_model(self):
        # Load label data
        self.labels = []
        for label in tf.gfile.GFile(self.label_file):
            self.labels.append(label.rstrip())

        # Load cnn model
        with tf.gfile.FastGFile(self.graph_file, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')

    def start_recognition(self, image_file):

        self.image = tf.gfile.FastGFile(image_file, 'rb').read() # read image

        with tf.Session() as sess:
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            predict = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': self.image})

            # Sort the label by probability
            top = predict[0].argsort()[-len(predict[0]):][::-1]

            # for index in top:
            #     human_string = labels[index]
            #     score = predict[0][index]
            #     print(human_string, score)

            self.recogClass = self.labels[top[0]]
            self.top_score  = ("%.2f" % (predict[0][top[0]]*100))
            # second_score = predict[0][1]

