import pretty_midi
import json
import collections

def export_to_tonnze_grouped(midi_path, output_json):
    # 讀取 MIDI 檔案
    midi_path = "/Users/mariannalee/Desktop/python/output_midi/fpxt5-2jzf8_basic_pitch.mid"
    pm = pretty_midi.PrettyMIDI(midi_path)
    
    # 使用字典來群組相同時間點的音符
    # Key 是時間，Value 是該時間點所有音符的清單
    time_groups = collections.defaultdict(list)

    for instrument in pm.instruments:
        for note in instrument.notes:
            # 將開始時間四捨五入到小數點後三位，避免微小誤差導致無法群組
            start_time = round(note.start, 3)
            time_groups[start_time].append({
                "midi": note.pitch,
                "name": pretty_midi.note_number_to_name(note.pitch),
                "vel": note.velocity
            })

    # 將字典轉換為排序後的清單
    tonnze_timeline = []
    for t in sorted(time_groups.keys()):
        tonnze_timeline.append({
            "time": t,
            "notes": time_groups[t] # 這裡現在是一個陣列了！
        })

    # 存成 JSON
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(tonnze_timeline, f, indent=4, ensure_ascii=False)

    print(f"✅ 轉換成功！共偵測到 {len(tonnze_timeline)} 個時間點。")
    print(f"📂 數據已存至: {output_json}")

# --- 執行 ---
midi_input = "/Users/mariannalee/Desktop/python/output_midi/fpxt5-2jzf8_basic_pitch.mid"
output_json = "/Users/mariannalee/Desktop/python/tonnze_grouped_data.json"
export_to_tonnze_grouped(midi_input, output_json)