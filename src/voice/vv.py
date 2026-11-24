import sys, json
from voicevox_core.blocking import Onnxruntime, OpenJtalk, Synthesizer, VoiceModelFile
DL='/tmp/claude-0/vvdl'; VV='/tmp/claude-0/vvm/r/vvms/'
def make(models):
    ort=Onnxruntime.load_once(filename=DL+'/voicevox_onnxruntime-linux-x64-1.23.2/lib/libvoicevox_onnxruntime.so.1.23.2')
    syn=Synthesizer(ort, OpenJtalk(DL+'/open_jtalk_dic_utf_8-1.11'), cpu_num_threads=4)
    for m in models:
        with VoiceModelFile.open(VV+m) as f: syn.load_voice_model(f)
    return syn
def kata(s): return ''.join(chr(ord(c)+96) if 'ぁ'<=c<='ゖ' else c for c in s)
def moras(aps): return ''.join(m.text for ap in aps for m in ap.moras)
