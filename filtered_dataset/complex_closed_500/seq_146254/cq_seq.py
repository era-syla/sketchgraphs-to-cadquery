import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.8, 2.35).lineTo(0.5869, 2.35).lineTo(0.5869, 0.0).lineTo(-0.8, 0.0).lineTo(-0.8, 2.35).close()
solid=wp_sketch0.add(loop0).extrude(7.02112422066229)
