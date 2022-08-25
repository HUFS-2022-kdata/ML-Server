# Speech Recogniton Server for langauge disorders

## Introduction
This is an end-to-end speech recognition server using deepspeech2 model trained by Hallym AI Data of Disorder from AI-Hub Korea

(dataset source: https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=608)

This project used Kospeech to train deepspeech2 model and to inference audio data

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

