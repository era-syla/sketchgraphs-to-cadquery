import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0265, -0.033).lineTo(-0.0265, -0.033).lineTo(-0.0265, 0.033).lineTo(0.0265, 0.033).lineTo(0.0265, -0.033).close()
solid=wp_sketch0.add(loop0).extrude(-0.002978126134217556)
