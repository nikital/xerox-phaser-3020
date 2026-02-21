IMAGE := $(shell podman build -q .)
$(if $(filter-out 0,$(.SHELLSTATUS)),$(error Dockerfile build failed))


.PHONY: rpm
rpm:
	mkdir -p out/
	podman run --rm --security-opt label=disable \
		-v .:/root/work:ro -v ./out:/root/work/out \
		-w /root/work "${IMAGE}" ./build.sh
