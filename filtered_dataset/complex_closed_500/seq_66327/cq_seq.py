import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0186, 0.03183).lineTo(0.0197, 0.03183).lineTo(0.0197, 0.02911).lineTo(-0.0186, 0.02911).lineTo(-0.0186, 0.03183).close()
solid=wp_sketch0.add(loop0).extrude(-0.04088379738190699)
