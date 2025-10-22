import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.086, -0.023).lineTo(0.008, -0.023).lineTo(0.008, -0.109).lineTo(0.086, -0.109).lineTo(0.086, -0.023).close()
solid=wp_sketch0.add(loop0).extrude(-0.20116742538339705)
