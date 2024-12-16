# 구음장애인을 위한 음성인식 서비스

## Introduction
발음이 정확하지 않은 구음장애인의 데이터를 학습하여 구음장애인도 음성인식을 원활하게 활용할 수 있는 서비스를 제공합니다.
언어모델 학습에는 deepspeech2 모델을 활용하였으며, 데이터 출처는 AI 허브의 구음장애 데이터셋입니다.
Kospeech 코드를 활용하여 자연어처리 결과를 전송하는 서버를 구현하였습니다.
구음장애 데이터 원본 및 피치 구음장애인을 위한 음성인식 서비스

## Introduction
발음이 정확하지 않은 구음장애인의 데이터를 학습하여 구음장애인도 음성인식을 원활하게 활용할 수 있는 서비스를 제공합니다.  
언어모델 학습에는 deepspeech2 모델을 활용하였으며, 데이터 출처는 AI 허브의 구음장애 데이터셋입니다.
구음장애 데이터 원본 및 피치를 조절한 데이터를 학습에 사용하였습니다.
(dataset source: https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=608)

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

