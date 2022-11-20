import sys
import time
import cv2
from kafka import KafkaProducer

topic = "topic1"
server_url = "localhost:9092"

def stream():
    producer = KafkaProducer(bootstrap_servers=[server_url])    
    camera = cv2.VideoCapture(0)
    try:
        while(True):
            _, frame = camera.read()        
            _, buffer = cv2.imencode('.jpg', frame)
            producer.send(topic, buffer.tobytes())            
            time.sleep(0.001)

    except:
        print("\nSaindo.")
        sys.exit(1)   

if __name__ == '__main__':
    stream()