import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.1, 0.1).lineTo(0.9, 0.1).lineTo(0.9, 0.9).lineTo(0.1, 0.9).lineTo(0.1, 0.1).close()
solid=wp_sketch0.add(loop0).extrude(1.752143379326514)
