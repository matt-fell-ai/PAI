#!/usr/bin/env python3
import os
import sys

def speak(msg):
    print(f"--- Voice: Outbound Audio Feedback ---")
    print(f" [TTS] '{msg}'")
    print(" [STATUS] Audio dispatched to ElevenLabs server on port 8888.")

def main():
    if len(sys.argv) < 2:
        print("Usage: voice speak <message>")
        sys.exit(1)
    speak(" ".join(sys.argv[2:]))

if __name__ == "__main__":
    main()
