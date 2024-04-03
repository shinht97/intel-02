# Practice #1 - bert_question_answering_demo
## Model Downloader:
``` shell
omz_downloader --list models.lst --precision FP16
```

## Model Converter:
``` shell
omz_converter --list models.lst
```

## RUN
''' shell
 python3 bert_question_answering_demo.py \
 --vocab intel/bert-small-uncased-whole-word-masking-squad-0001/vocab.txt \
 --model intel/bert-small-uncased-whole-word-masking-squad-0001/FP16/bert-small-uncased-whole-word-masking-squad-0001.xml \
 --input_names="input_ids,attention_mask,token_type_ids" \
 --output_names="output_s,output_e" \
 --input="https://en.wikipedia.org/wiki/Bert_(Sesame_Street)" \
 -c
'''


# Practice #2 - interactive_face_detection_demo
## Model Downloader:
``` shell
omz_downloader --list models.lst --precision FP16
```

## Model Converter:
``` shell
omz_converter --list models.lst
```

## RUN
``` shell
/interactive_face_detection_demo -i 0 \
 -m intel/face-detection-adas-0001/FP16/face-detection-adas-0001.xml \
 --mag intel/age-gender-recognition-retail-0013/FP16/age-gender-recognition-retail-0013.xml \
 --mhp intel/head-pose-estimation-adas-0001/FP16/head-pose-estimation-adas-0001.xml \
 --mem intel/emotions-recognition-retail-0003/FP16/emotions-recognition-retail-0003.xml \
 --mlm intel/facial-landmarks-35-adas-0002/FP16/facial-landmarks-35-adas-0002.xml \
 --mam public/anti-spoof-mn3/FP16/anti-spoof-mn3.xml \
 -d CPU
```


# Practice #3 - gaze_estimation_demo
## Model Downloader:
``` shell
omz_downloader --list models.lst --precision FP16
```

## Model Converter:
``` shell
omz_converter --list models.lst
```

## RUN
``` shell
gaze_estimation_demo -i 0 -m intel/gaze-estimation-adas-0002/FP16/gaze-estimation-adas-0002.xml \
-m_fd intel/face-detection-adas-0001/FP16/face-detection-adas-0001.xml \
-m_hp intel/head-pose-estimation-adas-0001/FP16/head-pose-estimation-adas-0001.xml \
-m_lm intel/facial-landmarks-35-adas-0002/FP16/facial-landmarks-35-adas-0002.xml \
-m_es public/open-closed-eye-0001/FP16/open-closed-eye-0001.xml -d CPU
```


# Practice #4 - monodepth_demo
## Model Downloader:
``` shell
omz_downloader --list models.lst --precision FP16
```
## file Downloader:
``` shell
pip install tensorflow
pip install torch
pip install onnx
pip install torchvision
```

## Model Converter:
``` shell
omz_converter --list models.lst
```

## RUN
``` shell
python3 monodepth_demo.py -d GPU -i 0 -m public/midasnet/FP16/midasnet.xml 
```


# Practice #5 - object_detection_demo
## Model Downloader:
``` shell
omz_downloader --list models.lst --precision FP16
```

## Model Converter:
``` shell
omz_converter --list models.lst
```

## RUN
``` shell
multi_channel_object_detection_demo_yolov3 -i 0 \
-m intel/person-vehicle-bike-detection-crossroad-yolov3-1020/FP16/person-vehicle-bike-detection-crossroad-yolov3-1020.xml -d GPU
```

