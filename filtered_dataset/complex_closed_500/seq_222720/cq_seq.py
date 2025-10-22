import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05498, 0.0905).lineTo(-0.0225, 0.0905).lineTo(-0.0225, 0.125).lineTo(-0.05498, 0.125).lineTo(-0.05498, 0.0905).close()
solid=wp_sketch0.add(loop0).extrude(0.0038148015576701167)
