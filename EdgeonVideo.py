import cv2
cap = cv2.VideoCapture('<<< Give input Video File Name with the path in System >>>')
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # Try MPV4 for higher quality encoding
out = cv2.VideoWriter('output_vid.avi',fourcc, 30.0,(int(cap.get(3)),int(cap.get(4))),False)

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #edge detection job here
    edges = cv2.Canny(frame, 70, 220)    # Lower and Higher Threshold
    out.write(edges)    
    if ret==True:
        cv2.imshow('frame',edges)
        if cv2.waitKey(1) & 0xFF == ord('q'):   # Press q to exit
            break
    else:
        break


# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()