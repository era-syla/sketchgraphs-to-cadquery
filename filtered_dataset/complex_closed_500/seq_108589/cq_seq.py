import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.036, -0.01025).lineTo(0.056, -0.01025).lineTo(0.056, -0.02125).lineTo(0.036, -0.02125).lineTo(0.036, -0.01025).close()
solid=wp_sketch0.add(loop0).extrude(-0.01416902674353285)
