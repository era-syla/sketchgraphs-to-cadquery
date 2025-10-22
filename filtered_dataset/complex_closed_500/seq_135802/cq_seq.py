import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.007, -0.011).lineTo(-0.007, 0.03142).lineTo(0.007, 0.03142).lineTo(0.007, -0.011).lineTo(-0.007, -0.011).close()
solid=wp_sketch0.add(loop0).extrude(0.1050812938926821)
