## Practice #1 - bert_question_answering_demo
```
cd demos/bert_question_answering_demo/python

omz_downloader --list models.lst --precision FP16


python3 bert_question_answering_demo.py \
    --vocab intel/bert-small-uncased-whole-word-masking-squad-0001/vocab.txt \
    --model intel/bert-small-uncased-whole-word-masking-squad-0001/FP16/bert-small-uncased-whole-word-masking-squad-0001.xml \
    --input_names="input_ids,attention_mask,token_type_ids" \
    --output_names="output_s,output_e" \
    --input="https://en.wikipedia.org/wiki/Bert_(Sesame_Street)" \
    -c
```
   
## Practice #2 - interactive_face_detection_demo
```
omz_downloader --list models.lst --precision FP16

omz_converter --list models.lst

#!/bin/sh  <-- 쉘 파일 만들기
interactive_face_detection_demo -i 0 \
    -m intel/face-detection-adas-0001/FP16/face-detection-adas-0001.xml \
    --mag intel/age-gender-recognition-retail-0013/FP16/age-gender-recognition-retail-0013.xml \
    --mhp intel/head-pose-estimation-adas-0001/FP16/head-pose-estimation-adas-0001.xml \
    --mem intel/emotions-recognition-retail-0003/FP16/emotions-recognition-retail-0003.xml \
    --mlm intel/facial-landmarks-35-adas-0002/FP16/facial-landmarks-35-adas-0002.xml \
    --mam public/anti-spoof-mn3/FP16/anti-spoof-mn3.xml \
    -d CPU
```
    
## Practice #3 - gaze_estimation_demo

```
omz_downloader --list models.lst --precision FP16

omz_converter --list models.lst
    
#!/bin/sh  <-- 쉘 파일 만들기
gaze_estimation_demo -d CPU -i 0 -m intel/gaze-estimation-adas-0002/FP16/gaze-estimation-adas-0002.xml \
-m_fd intel/face-detection-adas-0001/FP16/face-detection-adas-0001.xml \
-m_hp intel/head-pose-estimation-adas-0001/FP16/head-pose-estimation-adas-0001.xml \
-m_lm intel/facial-landmarks-35-adas-0002/FP16/facial-landmarks-35-adas-0002.xml \
-m_es public/open-closed-eye-0001/FP16/open-closed-eye-0001.xml
```

## Practice #4 - monodepth_demo

```
omz_downloader --list models.lst --precision FP16

omz_converter --list models.lst

pip install tensorflow
pip install torch
pip install onnx
pip install torchvision

#!/bin/sh  <-- 쉘 파일 만들기

python3 monodepth_demo.py -d GPU -i 0 -m public/midasnet/FP16/midasnet.xml
``` 

## Practice #6 - multi_channel_object_detection_demo_yolov3

```
omz_downloader --list models.lst --precision FP16

omz_converter --list models.lst

./multi_channel_object_detection_demo_yolov3 -m <path_to_model>/model.xml -d CPU -i 0
```



