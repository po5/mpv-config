from vapoursynth import core
import vsfieldkit

#vsfieldkit.fill_analog_frame_ends(video_in, luma_splash_radius=2, top_blank_width=0).set_output()
vsfieldkit.scan_interlaced(vsfieldkit.fill_analog_frame_ends(video_in.std.AssumeFPS(fpsnum=25, fpsden=1), luma_splash_radius=2, top_blank_width=0), tff=True, chroma_subsample_scanning="SCAN_UPSAMPLED", decay_factor=0.2).set_output()
