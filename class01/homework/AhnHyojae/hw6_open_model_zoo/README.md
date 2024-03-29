이하 모든 시동 디렉터리는 /open_model_zoo/demos의 하위 디렉터리에 존재

# Bert Question Answering Demo @ /bert_question_answering_demo/python

### 실행 코드

```shell
python3 bert_question_answering_demo.py --vocab intel/bert-small-uncased-whole-word-masking-squad-0001/vocab.txt --model intel/bert-small-uncased-whole-word-masking-squad-0001/FP16/bert-small-uncased-whole-word-masking-squad-0001.xml --input_names="input_ids,attention_mask,token_type_ids" --output_names="output_s,output_e" --input="https://en.wikipedia.org/wiki/Bert_(Sesame_Street)" -c -d AUTO
```

# Interactive Face Detection Demos

코드 실행 전에 실행 위치에 omz_downloader --list models.lst --precision FP16 실행 후 omz_converter --list models.lst를 실행해야 한다.


## @ /intreactive_face_detection_demo/cpp

### 실행 코드

```shell
interactive_face_detection_demo -i 0 -m intel/face-detection-adas-0001/FP16/face-detection-adas-0001.xml --mag intel/age-gender-recognition-retail-0013/FP16/age-gender-recognition-retail-0013.xml --mhp intel/head-pose-estimation-adas-0001/FP16/head-pose-estimation-adas-0001.xml --mem intel/emotions-recognition-retail-0003/FP16/emotions-recognition-retail-0003.xml --mlm intel/facial-landmarks-35-adas-0002/FP16/facial-landmarks-35-adas-0002.xml --mam public/anti-spoof-mn3/FP16/anti-spoof-mn3.xml -d CPU
```

## Gaze Estimation @ /gaze_estimation_demo/cpp

### 실행 코드 

```shell
gaze_estimation_demo -d CPU -i 0 -m intel/gaze-estimation-adas-0002/FP16/gaze-estimation-adas-0002.xml -m_fd intel/face-detection-adas-0001/FP16/face-detection-adas-0001.xml -m_hp intel/head-pose-estimation-adas-0001/FP16/head-pose-estimation-adas-0001.xml -m_lm intel/facial-landmarks-35-adas-0002/FP16/facial-landmarks-35-adas-0002.xml -m_es public/open-closed-eye-0001/FP16/open-closed-eye-0001.xml
```

## Monodepth Demo @ /monodepth_demo/python

### 실행 코드

```shell
python3 monodepth_demo.py -d GPU -i 0 -m public/midasnet/FP16/midasnet.xml
```

## Multi-Channel Object Detection Yolov3 demo @ /multi_channel_object_detection_demo_yolov3/cpp

### 실행 코드

```shell
multi_channel_object_detection_demo_yolov3 -i 0 -m intel/person-vehicle-bike-detection-crossroad-yolov3-1020/FP16/person-vehicle-bike-detection-crossroad-yolov3-1020.xml
```

## Segmentation Demo

### Camera 실행 코드 @ /segmentation_demo/python 

```shell
python3 segmentation_demo.py -d AUTO -i 0 -at segmentation -m intel/semantic-segmentation-adas-0001/FP16/semantic-segmentation-adas-0001.xml
```

### Images 실행 코드 @ /segmentation_demo/python 

```shell
python3 segmentation_demo.py -i ~/다운로드/ss-honoka001.jpg -d AUTO -at segmentation -m intel/semantic-segmentation-adas-0001/FP16/semantic-segmentation-adas-0001.xml --loop
```

### Camera 실행 코드 @ /segmentation_demo/python
```shell
segmentation_demo -d CPU -i 0 -m intel/semantic-segmentation-adas-0001/FP16/semantic-segmentation-adas-0001.xml
```

### Images 실행 코드 @ /segmentation_demo/python
```shell
segmentation_demo -d CPU -i ~/다운로드/ss-honoka001.jpg -m intel/semantic-segmentation-adas-0001/FP16/semantic-segmentation-adas-0001.xml -loop
```
