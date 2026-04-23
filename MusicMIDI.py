import os
import torch
from basic_pitch.inference import predict_and_save

# 1. 根據你的 find 結果，直接寫死正確的模型路徑
# 注意：路徑是指向資料夾，不包含最後的 saved_model.pb
MODEL_PATH = "/Users/mariannalee/Desktop/python/musicMIDI/lib/python3.11/site-packages/basic_pitch/saved_models/icassp_2022/nmp"

# 2. 定義你的音檔路徑
audio_path = "/Users/mariannalee/Desktop/python/fpxt5-2jzf8.wav"
output_dir = "/Users/mariannalee/Desktop/python/output_midi"

# 確保輸出資料夾存在
os.makedirs(output_dir, exist_ok=True)

print(f"🚀 發現模型！正在從此路徑啟動: {MODEL_PATH}")
print(f"🎵 正在處理音檔: {audio_path}")

# 3. 執行轉換
try:
    predict_and_save(
        audio_path_list=[audio_path],
        output_directory=output_dir,
        save_midi=True,
        sonify_midi=False,
        save_model_outputs=False,
        save_notes=True,
        model_or_model_path=MODEL_PATH  # 餵入正確的路徑
    )
    print(f"轉換完成。")
    print(f"📂 MIDI 檔在: {output_dir}")
except Exception as e:
    print(f"❌ 還是出錯了: {e}")