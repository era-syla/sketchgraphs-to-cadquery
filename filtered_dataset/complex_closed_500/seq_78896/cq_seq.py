import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.038, 0.054).lineTo(-0.0185, 0.054).lineTo(-0.0143, 0.05225).lineTo(0.0, 0.038).lineTo(0.0, 0.0034).lineTo(-0.006, 0.0).lineTo(-0.036, -0.0).lineTo(-0.042, 0.0034).lineTo(-0.042, 0.05).lineTo(-0.038, 0.054).close()
solid=wp_sketch0.add(loop0).extrude(0.08185795807590508)
