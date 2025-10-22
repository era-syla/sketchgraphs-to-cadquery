import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.03, -0.0).lineTo(-0.03, 0.05804).lineTo(0.0, 0.05).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.045011885590134616)
