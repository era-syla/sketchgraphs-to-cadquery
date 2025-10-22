import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.007).lineTo(0.01, 0.007).lineTo(0.01, 0.0).lineTo(-0.05, 0.0).lineTo(-0.05, 0.005).lineTo(0.0, 0.005).lineTo(0.0, 0.007).close()
solid=wp_sketch0.add(loop0).extrude(0.06537019899670281)
