from flask import Flask,render_template,request
import cv2
import datetime



app=Flask(__name__)

@app.route("/")
def main():
    return render_template('app.html')

@app.route("/calculate", methods=['POST'])
def webcam():
    import cv2

    cap = cv2.VideoCapture(0)
    
    #storing logs in a file
    with open("logs.txt",'a') as myfile:
        ct=datetime.datetime.now()
        myfile.write(f" Opened {str(ct)} ")
        

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    
    

    while True:
        
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)
        frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
        

        # describe the type of font
        # to be used.
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        #writing text
        cv2.putText(frame, "Press esc to quit", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (199,21,133))
        
        cv2.imshow('Webcam', frame)
        
        
             
        
        c = cv2.waitKey(1) #add 0 for frame pic when you stroke any key
        if c == 27:
            break
        
            
    
    cap.release()
    cv2.destroyAllWindows()
    #storing logout in a file
    with open("logs.txt",'a') as myfile:
        ct=datetime.datetime.now()
        myfile.write(f"Closed {str(ct)} \n")
        
    return render_template("app.html")