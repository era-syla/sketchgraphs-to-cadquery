import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.015, 0.03).lineTo(-0.015, 0.03).lineTo(-0.015, 0.012).lineTo(0.015, 0.012).lineTo(0.015, 0.03).close()
solid=wp_sketch0.add(loop0).extrude(0.033871524370912016)
