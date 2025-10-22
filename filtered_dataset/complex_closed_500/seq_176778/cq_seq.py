import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.068).lineTo(-0.0024, 0.068).lineTo(-0.0024, 0.058).lineTo(0.0, 0.058).lineTo(0.0, 0.068).close()
solid=wp_sketch0.add(loop0).extrude(-0.020138984876931637)
