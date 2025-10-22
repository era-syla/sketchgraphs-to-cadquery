import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(2.28, -0.93).lineTo(2.26, -0.93).lineTo(2.26, -0.91).lineTo(2.28, -0.91).lineTo(2.28, -0.93).close()
solid=wp_sketch0.add(loop0).extrude(-0.008179164385723954)
