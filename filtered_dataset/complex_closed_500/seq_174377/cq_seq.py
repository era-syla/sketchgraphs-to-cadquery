import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.003, -0.987).lineTo(0.003, -0.98799).lineTo(0.00385, -0.98749).lineTo(0.003, -0.987).close()
solid=wp_sketch0.add(loop0).extrude(0.0011911300006030119)
