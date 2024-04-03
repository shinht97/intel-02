### 이가원 실습

### Bert Question Answering Demo
실행 코드
```
python3 bert_question_answering_demo.py \
--vocab intel/bert-small-uncased-whole-word-masking-squad-0001/vocab.txt \
--model intel/bert-small-uncased-whole-word-masking-squad-0001/FP16/bert-small-uncased-whole-word-masking-squad-0001.xml \
--input_names="input_ids,attention_mask,token_type_ids" \
--output_names="output_s,output_e" \
--input="https://en.wikipedia.org/wiki/Bert_(Sesame_Street)" -c
```
### Interactive Face Detection Demos


### Gaze Estimation Demo
실행 코드
```
gaze_estimation_demo -d CPU -i 0 -m intel/gaze-estimation-adas-0002/FP16/gaze-estimation-adas-0002.xml \
-m_fd intel/face-detection-adas-0001/FP16/face-detection-adas-0001.xml \
-m_hp intel/head-pose-estimation-adas-0001/FP16/head-pose-estimation-adas-0001.xml \
-m_lm intel/facial-landmarks-35-adas-0002/FP16/facial-landmarks-35-adas-0002.xml \
-m_es public/open-closed-eye-0001/FP16/open-closed-eye-0001.xml 
```
### Monodepth Demo
omz convert 실행시 필요 파일. --- 설치 할 때 오래걸림.
``` 
pip install tensorflow
pip install torch
pip install onnx
pip install torchvision
```
실행 코드
```
python3 monodepth_demo.py -d GPU -i 0 -m public/midasnet/FP16/midasnet.xml 
```
### Multi-Channel Object Detection Yolov3 demo

실행 코드
```
multi_channel_object_detection_demo_yolov3 -i 0 \
-m intel/person-vehicle-bike-detection-crossroad-yolov3-1020/FP16/person-vehicle-bike-detection-crossroad-yolov3-1020.xml -d GPU
```
