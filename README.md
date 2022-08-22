# Speech Recogniton Server for langauge disorders

## Requirements

* Numpy: `pip install numpy`
* Pytorch: Refer to [PyTorch website](http://pytorch.org/) to install the version w.r.t. your environment.   
* Pandas: `pip install pandas` 
* Matplotlib: `pip install matplotlib`
* librosa: `conda install -c conda-forge librosa` 
* torchaudio: `pip install torchaudio==0.6.0` 
* tqdm: `pip install tqdm`
* sentencepiece: `pip install sentencepiece` 
* warp-rnnt: `pip install warp_rnnt` 
* hydra: `pip install hydra-core==1.1`
* Flask: `pip install flask

## Example of POST Method on javascript

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
