from vapoursynth import core, RGBS, YUV, YUV444PS, YUV444P16, GRAY

chicken = core.resize.Bicubic(video_in, format=RGBS, matrix_in=1, dither_type="error_diffusion").std.Limiter()
chicken = chicken.fmtc.transfer(transs="srgb", transd="linear", bits=32)
chicken = chicken.resize.Bicubic(format=YUV444PS, matrix=1, dither_type="error_diffusion")
chickeny = chicken.std.ShufflePlanes(0, colorfamily=GRAY)
chickeny = chickeny.chkdr.grain(draft=True, rad=0.015)
chicken = core.std.ShufflePlanes([chickeny, chicken], planes=[0, 1, 2], colorfamily=YUV)
chicken = chicken.resize.Bicubic(format=RGBS)
chicken = core.fmtc.transfer(chicken, transs="linear", transd="srgb")
chicken = chicken.resize.Bicubic(format=YUV444P16, matrix=1, dither_type="error_diffusion")

chicken.set_output()
