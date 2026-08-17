# Voice Architecture

## V1 interaction
- User can pause lesson and start voice tutor.
- Tutor receives lesson ID, timestamp/segment, jurisdiction, current example/tool state and learner context.
- Barge-in/interruption is supported.
- Live transcript is displayed and persisted according to consent/privacy settings.
- Tool calls are server-authorized.

## Architecture options
A provider adapter supports either direct speech-to-speech realtime sessions or a chained STT -> text agent -> TTS pipeline. Keep both behind a stable application interface.

## Founder voice
Founder voice cloning is an optional licensed voice asset. Store provider voice IDs/secrets server-side, keep explicit usage permissions, and support fallback professional voices.

## Arabic
Use approved Arabic glossary and terminology rules. Store teaching language separately from source-language regulation.
