import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import sys
import os.path as pathlib

classes = ['A300', 'A310', 'A320', 'A330', 'A340', 'A380', 'ATR-42', 'ATR-72',
       'An-12', 'BAE 146', 'BAE-125', 'Beechcraft 1900', 'Boeing 707',
       'Boeing 717', 'Boeing 727', 'Boeing 737', 'Boeing 747', 'Boeing 757',
       'Boeing 767', 'Boeing 777', 'C-130', 'C-47', 'CRJ-200', 'CRJ-700',
       'Cessna 172', 'Cessna 208', 'Cessna Citation', 'Challenger 600',
       'DC-10', 'DC-3', 'DC-6', 'DC-8', 'DC-9', 'DH-82', 'DHC-1', 'DHC-6',
       'DR-400', 'Dash 8', 'Dornier 328', 'EMB-120', 'Embraer E-Jet',
       'Embraer ERJ 145', 'Embraer Legacy 600', 'Eurofighter Typhoon', 'F-16',
       'F/A-18', 'Falcon 2000', 'Falcon 900', 'Fokker 100', 'Fokker 50',
       'Fokker 70', 'Global Express', 'Gulfstream', 'Hawk T1', 'Il-76',
       'King Air', 'L-1011', 'MD-11', 'MD-80', 'MD-90', 'Metroliner', 'PA-28',
       'SR-20', 'Saab 2000', 'Saab 340', 'Spitfire', 'Tornado', 'Tu-134',
       'Tu-154', 'Yak-42']

def infer():
    path  = pathlib.abspath(sys.argv[1])
    image = cv2.resize(
        cv2.cvtColor(
            cv2.imread(path),
            cv2.COLOR_BGR2RGB
        ),
        (96,64)
    ) / 255
    model = tf.keras.models.load_model("./ckp/CNN_ckps")
    class_prob = model.predict(image.reshape(1,64,96,3))[0]
    
    plt.imshow(image)
    plt.title(f"Predicted Class : {classes[class_prob.argmax(-1)]}")
    plt.show()

if __name__ == "__main__":
    infer()