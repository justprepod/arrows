syllable_words = [
 "а-фи-на",
 "пер-сей",
 "па-рис",
 "е-ле-на",
 "ар-го",
 "я-сон",
 "а-рес",
 "ру-но",
 "пар-фе-нон",
 "гар-пи-я",
 "цер-бер",
 "гид-ра",
 "гер-мес",
 "гек-тор",
 "ме-не-лай",
 "а-пол-лон",
 "де-мет-ра",
 "по-сей-дон",
 "ме-ду-за",
 "ди-о-нис",
 "кир-ка",
 "пе-гас",
 "кол-хи-да",
 "тро-я",
 "те-сей",
 "о-ра-кул",
 "си-ре-на",
 "пи-фи-я",
 "ор-фей",
 "ге-ра",
 "пар-нас",
]

from pydub import AudioSegment, silence
import os

from pydub import AudioSegment, silence
import os

# === INPUT ===
audio_path = "audio.wav"

# === STEP 1: Generate flat list of spoken items ===
spoken_items = []
for entry in syllable_words:
    word = entry.replace("-", "")
    syllables = entry.split("-")
    spoken_items.append(word)
    spoken_items.extend(syllables)

# === STEP 2: Load audio and detect silences ===
audio = AudioSegment.from_wav(audio_path)
silence_ranges = silence.detect_silence(audio, min_silence_len=400, silence_thresh=-40)

# Compute midpoints of silence intervals
cut_points = [0]  # start of audio
for start, end in silence_ranges:
    mid = (start + end) // 2
    cut_points.append(mid)
cut_points.append(len(audio))  # end of audio

# === STEP 3: Cut and export segments ===
used_names = {}
for i in range(len(cut_points) - 1):
    if i >= len(spoken_items):
        print(f"Warning: more audio chunks than names. Stopping at {i}.")
        break

    start = cut_points[i]
    end = cut_points[i + 1]
    chunk = audio[start:end]

    base_name = spoken_items[i]
    count = used_names.get(base_name, 0)
    if count > 0:
        name = f"{base_name}_{count}"
    else:
        name = base_name
    used_names[base_name] = count + 1

    chunk.export(f"output/{name}.wav", format="wav")

print("Done.")

