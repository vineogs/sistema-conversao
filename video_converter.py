import ffmpeg

def video_converter(input, output, width=720, height=480):
    try:
        (
            ffmpeg
            .input(input)
            .output(
                output,
                vcodec="libx264",
                acodec="aac",
                vf=f"scale={width}:{height}",
            )
            .run()
        )
        print(f"Conversão bem sucedida para {output}")
    except Exception as e:
        print(f"Erro ao converter {input} para {output}: {e}")

video_converter("teste.MOV", "teste.mp4")