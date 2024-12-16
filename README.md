# 구음장애인을 위한 음성인식 서비스
## Introduction
발음이 정확하지 않은 구음장애인의 데이터를 학습하여 구음장애인도 음성인식을 원활하게 활용할 수 있는 서비스를 제공합니다.  
언어모델 학습에는 deepspeech2 모델을 활용하였으며, 데이터 출처는 AI 허브의 구음장애 데이터셋입니다.  
구음장애 데이터 원본 및 피치를 조절한 데이터를 학습에 사용하였습니다.  
(dataset source: https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=608)

## Project Overview
구음장애란 말을 할 때 사용하는 근육의 경직, 불균형, 마비 따위로 인하여 나타나는 말을 구사하는 능력의 장애를 의미합니다.  
이러한 발화 장애를 가진 사람의 경우, 기존의 음성인식 서비스를 활용하기 어려운 문제점을 가지고 있습니다.  
국가통계포털 참조 결과, 구음 장애의 위험성을 지닌 인구는 약 104만명 입니다.  
다양한 곳에 활용되고 있는 음성인식 기술의 배리어프리를 실현하기 위해 본 프로젝트를 제안하였습니다.

## Preview
![image](https://github.com/user-attachments/assets/faad9b73-3dfe-400d-a8dd-20d4f195b41e)

[시연 동영상]
https://youtube.com/shorts/iKKSGWPGtTE

## Requirements
python version == 3.8

* Numpy: `pip install numpy`
* Pytorch: Refer to [PyTorch website](http://pytorch.org/) to install the version w.r.t. your environment.   
* Pandas: `pip install pandas` 
* Matplotlib: `pip install matplotlib`
* librosa: `conda install -c conda-forge librosa` 
* pydub `pip install pydub`
* torchaudio: `pip install torchaudio==0.6.0` 
* tqdm: `pip install tqdm`
* sentencepiece: `pip install sentencepiece` 
* warp-rnnt: `pip install warp_rnnt` 
* hydra: `pip install hydra-core==1.1`
* Flask: `pip install flask`
* ffmpeg: Refer to [ffmpeg website](https://ffmpeg.org/)
add model.pt and vocab dictionary csv file in root directory

## Example of POST Method on Expo/React-Native

```
const uploadAudio = async () => {
  const filename = uri.split('/').pop()
  let formData = new FormData()
  formData.append('file', {
    uri : uri,
    name : filename,
    type : 'audio/m4a'
  })
  let options = {
    method: "POST",
    body: formData,
    headers: {
      Accpet: "application/json",
      "Content-Type": "multipart/form-data"
    }
  }
  await fetch('url/upload',options)
```

## References
Kospeech: https://github.com/sooftware/kospeech  
Deepspeech2: https://arxiv.org/abs/1512.02595
![image](https://github.com/user-attachments/assets/71a6fdc1-3492-48ab-ad6b-778beb540062)

