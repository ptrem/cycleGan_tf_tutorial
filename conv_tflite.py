# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:34:15 2020

@author: ptrem
"""
import tensorflow as tf
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True,
                    help='path to Tensorflow Lite object detection model.')
    parser.add_argument('--output', required=True,
                    help='File path of the output image.')
    args = parser.parse_args()
    
    
    model = tf.keras.models.load_model(args.model)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    open (args.output , "wb").write(tflite_model)

main()
