import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01373, 0.02052).lineTo(-0.10084, 0.02052).lineTo(-0.10084, 0.0647).lineTo(-0.01373, 0.0647).lineTo(-0.01373, 0.02052).close()
solid=wp_sketch0.add(loop0).extrude(-0.2350463085749778)
