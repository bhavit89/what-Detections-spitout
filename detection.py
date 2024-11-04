results = [
    {
        "boxes": [
            {"cls": 0, "conf": 0.95, "xyxy": [10, 20, 50, 80]}, # Object 1
            {"cls": 1, "conf": 0.85, "xyxy": [60, 100, 120, 160]},  # Object 2
            {"cls": 0, "conf": 0.78, "xyxy": [130, 200, 180, 260]},  # Object 3
            {"cls": 2, "conf": 0.92, "xyxy": [300, 400, 350, 450]}   # Object 4
        ],
        "names": {0: "person", 1: "car", 2: "dog"}  # Class ID to name mapping
    }
]


detection = results[0]
print("RESULT", len(detection))

for i in  range(len(detection["boxes"])):
    bb = detection["boxes"][i]
    clsId = bb['cls']
    confidence = bb['conf']
    LABEL = detection['names'][clsId]
    LABEL = f"confidence-{confidence} className--{LABEL} classId--{clsId}"
    x1,y1,x2,y2 = bb["xyxy"]
    
    
    
    # print(f"BOXES,{bb}")
    # print(f"classId ,{clsId}")
    # print(f"confidence {confidence}")
    print(bb)
    print(f"Label--------------------------> {LABEL}")
    print("cordinates ---------------------------------",x1,y2,x2,y2)