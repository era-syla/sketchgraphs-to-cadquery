import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(2.286, 0.0).lineTo(2.286, 0.7112).lineTo(-0.0, 0.7112).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(1.6091149961766553)
