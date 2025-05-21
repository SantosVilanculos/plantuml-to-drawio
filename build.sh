#!/usr/bin/env bash

WORKDIR=$(dirname $(realpath "$0"))
NAME="plantuml-to-drawio"

if [[ "$OSTYPE" == cygwin* || "$OSTYPE" == msys* ]]; then
  pyivf-make_version \
    --source-format yaml \
    --metadata-source "$WORKDIR/metadata.yml" \
    --outfile "$WORKDIR/metadata.rc"

  pyinstaller "$WORKDIR/src/main.py" \
    --noconfirm \
    --clean \
    --onefile \
    --specpath "$WORKDIR/build" \
    --name="$NAME" \
    --add-data="$WORKDIR/plantuml-mit-1.2025.2.jar:." \
    --windowed \
    --icon="$WORKDIR/icon.png" \
    --disable-windowed-traceback \
    --version-file="$WORKDIR/metadata.rc" \
    --uac-admin

elif [[ "$OSTYPE" == darwin* ]]; then
  pyinstaller "$WORKDIR/src/main.py" \
    --noconfirm \
    --clean \
    --onefile \
    --specpath "$WORKDIR/build" \
    --name="$NAME" \
    --add-data="$WORKDIR/plantuml-mit-1.2025.2.jar:." \
    --windowed \
    --icon="$WORKDIR/icon.png" \
    --disable-windowed-traceback

else
  pyinstaller "$WORKDIR/src/main.py" \
    --noconfirm \
    --clean \
    --onefile \
    --specpath "$WORKDIR/build" \
    --name="$NAME" \
    --add-data="$WORKDIR/plantuml-mit-1.2025.2.jar:."
fi
