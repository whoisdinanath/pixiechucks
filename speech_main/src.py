import requests
import base64
import json
import time
subscriptionKey = "39a38c7fa1344942af96e828789e0f0c"
region = "southeastasia"

WaveHeader16K16BitMono = bytes([82, 73, 70, 70, 78, 128, 0, 0, 87, 65, 86, 69, 102, 109, 116, 32, 18,
                               0, 0, 0, 1, 0, 1, 0, 128, 62, 0, 0, 0, 125, 0, 0, 2, 0, 16, 0, 0, 0, 100, 97, 116, 97, 0, 0, 0, 0])

# reads audio data chunk by chunk
# the audio_source can be audio file, microphone, memory stream, etc.

# pronunciation assessment parameters
# test1
# referenceText = "Good morning."
# test2
# referenceText = "This is an apple."
# test3
# referenceText = "Pass me that book."
# test4
# referenceText = "He is doing great."
# test5
# referenceText = "Work like a professional."
# test6
#referenceText = "Very long sentences are often overstuffed."
# test7
#referenceText = "Would you like to have some coffee."
# test8
#referenceText = "Paragraph should never be longer. It should be short and sweet and hello."


def get_chunk(audio_source, chunk_size=1024):
    yield WaveHeader16K16BitMono
    while True:
        time.sleep(chunk_size / 32000)  # to simulate human speaking rate
        chunk = audio_source.read(chunk_size)
        if not chunk:
            global uploadFinishTime
            uploadFinishTime = time.time()
            break
        yield chunk


def get_url(reference_text):
    pronAssessmentParamsJson = "{\"ReferenceText\":\"%s\",\"GradingSystem\":\"HundredMark\",\"Dimension\":\"Comprehensive\"}" % reference_text
    pronAssessmentParamsBase64 = base64.b64encode(
        bytes(pronAssessmentParamsJson, 'utf-8'))
    pronAssessmentParams = str(pronAssessmentParamsBase64, "utf-8")

    # build request
    url = "https://%s.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-us" % region
    headers = {'Accept': 'application/json;text/xml',
               'Connection': 'Keep-Alive',
               'Content-Type': 'audio/wav; codecs=audio/pcm; samplerate=16000',
               'Ocp-Apim-Subscription-Key': subscriptionKey,
               'Pronunciation-Assessment': pronAssessmentParams,
               'Transfer-Encoding': 'chunked',
               'Expect': '100-continue'}
    return url, headers


def main_func(reference_text, audio_file):
    url, headers = get_url(reference_text)
    response = requests.post(
        url=url, data=get_chunk(audio_file), headers=headers)
    getResponseTime = time.time()
    result_json = json.loads(response.text)
    latency = getResponseTime - uploadFinishTime
    return result_json
