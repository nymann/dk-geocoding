ARG DEBIAN_VERSION=bookworm

FROM nymann/debian-python3-dev:$DEBIAN_VERSION AS compile-image
COPY --chown=$USERNAME:$USERNAME . .
RUN make install

FROM nymann/debian-python3:$DEBIAN_VERSION
EXPOSE 80
USER $USERNAME
COPY --from=compile-image --chown=$USERNAME:$USERNAME "$VENV" "$VENV"
CMD uvicorn dk_geocoding.asgi:api --workers 2 --port 80 --host 0.0.0.0
