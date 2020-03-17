import numpy as np
import tflite_runtime.interpreter as tflite
from PIL import Image

interpreter = None


def load_labels(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


def handler(event, context):
    global interpreter
    if interpreter is None:
        interpreter = tflite.Interpreter("./mobilenet_v1_1.0_224_quant.tflite")
        interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # check the type of the input tensor
    floating_model = input_details[0]['dtype'] == np.float32

    # NxHxWxC, H:1, W:2
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]
    img = Image.open("./grace_hopper.bmp").resize((width, height))

    # add N dim
    input_data = np.expand_dims(img, axis=0)

    if floating_model:
        input_data = (np.float32(input_data) - 127.5) / 127.5

    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    results = np.squeeze(output_data)
    top_k = results.argsort()[-5:][::-1]
    labels = load_labels("./labels.txt")
    for i in top_k:
        if floating_model:
            return '{:08.6f}: {}'.format(float(results[i]), labels[i])
    else:
        return '{:08.6f}: {}'.format(float(results[i] / 255.0), labels[i])
