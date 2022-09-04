from vapoursynth import core, RGBS, YUV, YUV444PS, GRAY
import lvsfunc as lvf

chicken = lvf.noise.chickendream(video_in.std.SetFrameProp(prop="_Matrix", intval=1), draft=True, rad=0.015)
chicken = lvf.deinterlace.vinverse(lvf.deinterlace.vinverse(chicken).std.Transpose()).std.Transpose()

chicken.set_output()
